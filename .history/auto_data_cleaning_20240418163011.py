import numpy as np
import pandas as pd

data = pd.read_csv("your_dataset.csv")

print("Original dataset:")
print(data.head())

missing_values = data.isnull().sum()
print("\nMissing values:")
print(missing_values)

numeric_columns = data.select_dtypes(include=['number']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

data.dropna(subset=['categorical_column'], inplace=True)

data = pd.get_dummies(data, columns=['categorical_column'])

data['date_column'] = pd.to_datetime(data['date_column'])

from scipy import stats
data = data[(np.abs(stats.zscore(data.select_dtypes(include=['number']))) < 3).all(axis=1)]

print("\nCleaned dataset:")
print(data.head())

data.to_csv("cleaned_dataset.csv", index=False)

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
