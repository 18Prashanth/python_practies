import pandas as pd

data = pd.read_csv('D:\ALL IN ONE\Msc AI\Python\pandas\data.csv')
data.dropna(inplace=True)
data.fillna(130, inplace=True)
print(data.to_string())
