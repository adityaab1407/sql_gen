import sqlite3
import pandas as pd

source1_csv = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/source1.csv'
source2_csv = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/source2.csv'

db1_path = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/db1.sqlite'
db2_path = '/Users/adityaab14/Documents/Projects/sql_gen/workbench/db2.sqlite'

conn1 = sqlite3.connect(db1_path)
try:
    source1 = pd.read_csv(source1_csv)
    source1.to_sql('source1', conn1, index=False, if_exists='replace')
    print("Table 'source1' created successfully in db1.sqlite.")
except Exception as e:
    print(f"Error loading source1.csv: {e}")
finally:
    conn1.close()


conn2 = sqlite3.connect(db2_path)
try:
    source2 = pd.read_csv(source2_csv)
    source2.to_sql('source2', conn2, index=False, if_exists='replace')
    print("Table 'source2' created successfully in db2.sqlite.")
except Exception as e:
    print(f"Error loading source2.csv: {e}")
finally:
    conn2.close()
