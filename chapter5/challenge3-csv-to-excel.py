# You need to install pandas before running the code
# pip install pandas

import csv
import pandas as pd

def convert_csv_to_excel(csv_file_path, excel_file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Write DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)

csv_file_path = 'path/to/your/input.csv'
excel_file_path = 'path/to/your/output.xlsx'

convert_csv_to_excel(csv_file_path, excel_file_path)

print(f"CSV file '{csv_file_path}' successfully converted to Excel file '{excel_file_path}'.")
