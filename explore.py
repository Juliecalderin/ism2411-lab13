# Self-Assessment
# 1. A boolean filter checks every row against a condition and gives back True or
#    False for each one. Then it keeps only the rows that came back True.
#
# 2. df["revenue"] gives me one column as a Series. df[["revenue"]] gives me a
#    DataFrame that has just that one column. It matters when a function needs
#    a DataFrame (like .shape or to_csv) versus a single column of numbers.
#
# 3. pandas can filter, sort, and calculate across all 5,000 rows with one line
#    of code, and I can rerun it any time instead of redoing it by hand in Excel.

import pandas as pd

# Exercise 1: Load it
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2: Filter by region
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# Exercise 3: Top 5 by revenue
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)

# Exercise 4: Two-condition filter
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

# Exercise 5: A new column
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6: Unique values
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7: Select columns
subset = df[['region', 'product', 'revenue']]
print(subset.shape)

# Exercise 8: Save
df.to_csv('data/explored.csv', index=False)
