# Superstore Sales Analysis
import pandas as pd

df = pd.read_csv('SampleSuperstore.csv')
print(df.head())

# Profit by Category
print(df.groupby('Category')['Profit'].sum())

# Sales by Region
print(df.groupby('Region')['Sales'].sum())
