import os
import pandas as pd

def detect_csv_files_and_report_structure(folder_path):

    files_in_folder = os.listdir(folder_path)
    csv_files = [file for file in files_in_folder if file.lower().endswith('.csv')]

    if len(csv_files) != 3:
        print("Expected three CSV files: input1.csv, input2.csv, and output.csv. Please check the folder.")
        return

    input1 = None
    input2 = None
    output = None

    # Iterate through each CSV file and read them
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        
        try:
            df = pd.read_csv(file_path)

            # Store DataFrames in respective variables based on the file name
            if 'input1' in csv_file.lower():
                input1 = df
            elif 'input2' in csv_file.lower():
                input2 = df
            elif 'output' in csv_file.lower():
                output = df

            # Report the structure of each file
            print(f"Structure of file: {csv_file}")
            print(f"Columns: {list(df.columns)}")
            print(f"Data types:\n{df.dtypes}")
            print(f"First few rows:\n{df.head()}\n")
        
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

    if input1 is not None and input2 is not None and output is not None:
        print("All required DataFrames have been successfully loaded.")
    else:
        print("One or more required DataFrames were not found.")

    return input1, input2, output

folder_path = 'workbench' 
input1, input2, output = detect_csv_files_and_report_structure(folder_path)
