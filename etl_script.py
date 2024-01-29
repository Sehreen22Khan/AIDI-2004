import sqlite3
import pandas as pd

def extract_data(file_path):
    data = pd.read_csv(file_path)
    return data

def transform_data(data):
    data['date_column'] = pd.to_datetime(data['date_column'])
    data = data.dropna()
    data['new_column'] = data['column1'] * data['column2']
    return data

def load_data(data, destination_table):
    conn = sqlite3.connect('example.db')
    data.to_sql(destination_table, conn, if_exists='replace', index=False)
    conn.close()

def main():
    source_file = 'data.csv'
    extracted_data = extract_data(source_file)
    transformed_data = transform_data(extracted_data)
    destination_table = 'transformed_data'
    load_data(transformed_data, destination_table)
    print("ETL process completed successfully!")

if __name__ == "__main__":
    main()
