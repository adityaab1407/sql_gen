import pandas as pd
import pandasql as ps

def execute_query_from_file(input_csv1, input_csv2, output_csv, query_file_path):
    df1 = pd.read_csv(input_csv1)
    df2 = pd.read_csv(input_csv2)

    with open(query_file_path, 'r') as file:
        query = file.read()
    # Combine the DataFrames by adding them as tables in pandasql
    # Create a query and pass the dataframes to pandasql using the locals()
    query_result = ps.sqldf(query, locals())
    query_result.to_csv(output_csv, index=False)

    print(f"Query executed successfully. Output saved to '{output_csv}'.")

input_csv1 = 'workbench/input1.csv'
input_csv2 = 'workbench/input2.csv'
output_csv = 'workbench/output.csv'
query_file_path = 'workbench/query.sql'

execute_query_from_file(input_csv1, input_csv2, output_csv, query_file_path)
