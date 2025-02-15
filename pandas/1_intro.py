# introduction to pandas

import pandas as pd
# a = [1, 7, 2]

# myvar = pd.Series(a, index=["x", "y", "z"])

fruites = {"apple": 20, "orange": 30, "banana": 20}

fruit_tabel = pd.Series(fruites, index=["apple", "orange"])
print(fruit_tabel)
