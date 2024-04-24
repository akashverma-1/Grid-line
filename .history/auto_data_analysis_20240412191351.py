import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("your_dataset.csv")


print("Dataset shape:", data.shape)
print("Columns:", data.columns)
print("Data types:\n", data.dtypes)
print("Summary statistics:\n", data.describe())


plt.figure(figsize=(10, 6))
sns.histplot(data['numeric_column'], bins=20, kde=True)
plt.title("Histogram of Numeric Column")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

sns.pairplot(data)
plt.title("Pairplot of Variables")
plt.show()