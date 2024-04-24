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
