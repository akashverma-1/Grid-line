import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load the data from a CSV file
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None

def generate_sales_report(df):
    try:
        # Group data by month and calculate total sales
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period('M')
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Plot monthly sales
        plt.figure(figsize=(10, 6))
        monthly_sales.plot(kind='bar', color='skyblue')
        plt.title('Monthly Sales Report')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error generating sales report:", e)

def main():
    # Load the data
    file_path = '(https://www.kaggle.com/datasets'  # Replace with your file path
    df = load_data(file_path)

    if df is not None:
        # Generate sales report
        generate_sales_report(df)

if __name__ == "__main__":
    main()
