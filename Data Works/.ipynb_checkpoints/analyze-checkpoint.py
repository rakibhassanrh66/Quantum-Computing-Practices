import pandas as pd


df = pd.read_excel('test.xlsx', engine='openpyxl')


print(df.head())

print(df.info())

print(df.describe())
