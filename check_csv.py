import pandas as pd

d = pd.read_csv('employees.csv')

series = pd.isnull(d['Gender'])
missing_gender_count = d[series]
print(missing_gender_count)