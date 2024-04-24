import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Sales': [100, 200, 150, 120, 220],
    'Profit': [10, 20, 15, 12, 22]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Explore the DataFrame
print("First few rows of the DataFrame:")
print(df.head())
print()

print("Data types of each column:")
print(df.dtypes)
print()

print("Missing values:")
print(df.isnull().sum())
print()

# Perform Data Analysis
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
average_sales = df['Sales'].mean()
average_profit = df['Profit'].mean()

# Display the results
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", average_sales)
print("Average Profit:", average_profit)
print()

# Visualize the Data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
