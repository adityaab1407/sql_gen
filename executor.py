import pandas as pd
import pandasql as ps

def execute_query_from_file(input_csv1, input_csv2, output_csv, query_file_path):
    # Load the CSV files into pandas DataFrames
    df1 = pd.read_csv(input_csv1)
    df2 = pd.read_csv(input_csv2)

    # Read the SQL query from the file
    with open(query_file_path, 'r') as file:
        query = file.read()

    # Combine the DataFrames by adding them as tables in pandasql
    # Create a query and pass the dataframes to pandasql using the locals()
    query_result = ps.sqldf(query, locals())

    # Save the result of the query to a new CSV file
    query_result.to_csv(output_csv, index=False)

    print(f"Query executed successfully. Output saved to '{output_csv}'.")

# Example usage:
input_csv1 = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/source1.csv'
input_csv2 = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/source2.csv'
output_csv = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/sources_combined.csv'
query_file_path = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/query.sql'

execute_query_from_file(input_csv1, input_csv2, output_csv, query_file_path)
