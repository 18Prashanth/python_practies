# Data Frames

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

# print(myvar)
# print(myvar.loc[0])  # This statement prints the oth row of the table
# print(myvar.loc[[0, 1]])

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
