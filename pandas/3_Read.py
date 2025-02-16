import pandas as pd

df = pd.read_csv('D:\ALL IN ONE\Msc AI\Python\pandas\iris.csv')

# print(df)

# By using the above statements we can see only firts 5 and last 5 rows
# if we have large number of data so to see all data use the to_string() method or function

dataframes = pd.read_csv('D:\ALL IN ONE\Msc AI\Python\pandas\iris.csv')
print(dataframes.to_string())
