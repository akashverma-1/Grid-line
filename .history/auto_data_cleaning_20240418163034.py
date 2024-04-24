import numpy as np
import pandas as pd



def handle_missing_values(df):
    # Drop rows with missing values
    df_cleaned = df.dropna()
    return df_cleaned

def remove_duplicates(df):
    # Remove duplicate rows
    df_cleaned = df.drop_duplicates()
    return df_cleaned

def transform_data(df):
    # Example: Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def main():
    # Load the data
    df = pd.read_csv('your_data.csv')

    # Handle missing values
    df = handle_missing_values(df)

    # Remove duplicates
    df = remove_duplicates(df)

    # Transform data
    df = transform_data(df)

    # Display the cleaned data
    print("Cleaned Data:")
    print(df)

if __name__ == "__main__":
    main()
