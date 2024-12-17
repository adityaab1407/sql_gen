import subprocess
import pandas as pd
from huggingface_hub import InferenceClient
from config import HF_API_KEY

def generate_sql(query):
    input1_df, input2_df = run_source_detector()
    input1_str = input1_df.to_string(index=False) 
    input2_str = input2_df.to_string(index=False)  
    sql_query = generate_model_call(query, input1_str, input2_str)
    print(sql_query)
    
    file_path = 'workbench/query.sql'
    with open(file_path, 'w') as file:
        file.write(sql_query)

    return sql_query

def run_source_detector():
    result = subprocess.run(
        ['python3', 'scripts/source_detector.py'],
        capture_output=True, text=True
    )

    input1_df = pd.read_csv('workbench/source1.csv')
    input2_df = pd.read_csv('workbench/source2.csv')
    return input1_df, input2_df

def run_executor():
    result = subprocess.run(
        ['python3', 'scripts/executor.py'],
        capture_output=True, text=True
    )

    output_df = pd.read_csv('workbench/sources_combined.csv')
    return output_df

def generate_model_call(query, input1, input2):
    client = InferenceClient(api_key=HF_API_KEY)

    system_message = f"""
    You are a SQL generator tasked with creating SQL queries based on a user's task description. 
    Two datasets (CSV files) are available in the workspace for analysis:

    File 1 (df1):
    Structure:
    - [column names and descriptions of columns in file 1]

    File 2 (df2):
    Structure:
    - [column names and descriptions of columns in file 2]

    Your task is to generate an SQL query based on the task description provided by the user. 
    The query should involve operations such as selecting data, joining tables, and possibly filtering results.

    Instructions:
    - The user will provide two datasets and describe the SQL task they want to perform.
    - Based on the user's description and the available datasets, you need to generate the correct SQL query.
    - The SQL query should select all columns (`SELECT *`) from both datasets and use appropriate operations like JOIN.
    - The generated SQL query should be returned with no explanation or additional text.

    Note: Ensure that you use the relevant columns from the two datasets to build your SQL query.
    """

    user_message = f"""
    Query: {query}

    File 1 (df1):
    {input1}

    File 2 (df2):
    {input2}
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct", 
        messages=messages, 
        temperature=0.5,
        max_tokens=2048,
        top_p=0.7
    )

    return response.choices[0].message['content']