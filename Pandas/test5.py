# sorting is done by using sort_index()

import numpy as np
import pandas as pd

# df = pd.DataFrame(np.arange(16).reshape(4, 4), index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
# here datframe is 2-D array no sorting is possible so we assume series which is 1-D array

# srs = pd.Series([14, 18, 1, 7], index=['A', 'C', 'D', 'B'])
# print(srs.sort_index())
# print(srs.sort_values())
# print(srs.rank())

"""----------------------------------------------------------"""

# deal with missing data

null_value = np.nan
# srs = pd.Series([null_value, 12, 34, null_value])
# print(srs)
# print(srs.isnull())

#dropping null values
print("-------------------------")
# print(srs.dropna())
# print(srs.dropna(how = 'all'))

# df = pd.DataFrame([[11, 2, 73], [45, 65, 19], [null_value, 16, 18]])
# print(df.dropna(axis=1))
# print(df.dropna(thresh=1))

# fill data in NaN
# print(df.fillna(45))
# print(df)
# print(df.sum(axis=1))
# print(df.sum(axis=0))

# print(df.min(axis=0))
# print(df.max(axis=1))

# print(df.idxmax(axis=1))
# print(df.idxmin(axis=1))
