import subprocess
import pandas as pd

def generate_sql(query):
    # LLM Simulation: For now, just echoing the input query
    generated_sql = f"SELECT * FROM table WHERE description LIKE '%{query}%'"
       
    return generated_sql, query

def run_source_detector():
    result = subprocess.run(
        ['python3', '/Users/adityaab14/Documents/Projects/sql_gen/source_detector.py'],
        capture_output=True, text=True
    )

    input1_df = pd.read_csv('/Users/adityaab14/Documents/Projects/sql_gen/workbench/source1.csv')
    input2_df = pd.read_csv('/Users/adityaab14/Documents/Projects/sql_gen/workbench/source2.csv')
    return input1_df, input2_df

def run_executor():
    result = subprocess.run(
        ['python3', '/Users/adityaab14/Documents/Projects/sql_gen/executor.py'],
        capture_output=True, text=True
    )

    output_df = pd.read_csv('/Users/adityaab14/Documents/Projects/sql_gen/workbench/sources_combined.csv')
    return output_df
