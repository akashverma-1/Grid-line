import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

sales_by_month = data.groupby('Month')['Revenue'].sum()
top_products = data.groupby('Product')['Units Sold'].sum().nlargest(5)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
sales_by_month.plot(kind='bar', color='skyblue')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Revenue')

plt.subplot(2, 1, 2)
top_products.plot(kind='bar', color='salmon')
plt.title('Top 5 Products')
plt.xlabel('Product')
plt.ylabel('Units Sold')

plt.tight_layout()

plt.savefig('sales_report.png')

report_text = f"Sales by Month:\n{sales_by_month}\n\nTop 5 Products:\n{top_products}"

with open('sales_report.txt', 'w') as file:
    file.write(report_text)

plt.show()
