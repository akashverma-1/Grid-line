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

def clean_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Handle missing values
    df = handle_missing_values(df)

    # Remove duplicates
    df = remove_duplicates(df)

    # Transform data
    df = transform_data(df)

    return df

if __name__ == "__main__":
    cleaned_df = clean_data('your_data.csv')
    print("Cleaned Data:")
    print(cleaned_df)
