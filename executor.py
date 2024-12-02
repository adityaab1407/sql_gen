import sqlite3
import pandas as pd

conn1 = sqlite3.connect('/Users/adityaab14/Documents/Projects/sql_gen/workbench/db1.sqlite')

conn1.execute("ATTACH DATABASE '/Users/adityaab14/Documents/Projects/sql_gen/workbench/db2.sqlite' AS db2")

with open('/Users/adityaab14/Documents/Projects/sql_gen/workbench/query.sql', 'r') as file:
    query = file.read()

result = pd.read_sql_query(query, conn1)

result.to_csv('/Users/adityaab14/Documents/Projects/sql_gen/workbench/sources_combined.csv', index=False)

print("Query executed successfully. Output saved to 'output_combined.csv'.")

conn1.close()
