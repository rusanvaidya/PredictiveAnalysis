import pandas as pd

# srs = pd.Series([81.99, 72.44, 62.02, 63.0, 74.11], index=['CN', 'NP', 'MMS', 'BPIT', 'INTS'])

# srs1 = srs.reindex(['TC', 'NP', 'MMS', 'BPIT', 'ICTPM'], fill_value=0)
# print(srs1)

# srs1 = srs.reindex(['TC', 'NP', 'MMS', 'BPIT', 'ICTPM'])
# print(srs1.ffill())

import numpy as np

# df = pd.DataFrame(np.arange(16).reshape(4, 4), index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd'])
#
# redf = df.reindex(['A', 'B', 'C', 'D', 'E'], columns=['a', 'b', 'c', 'd', 'e'])
#
# print(redf.ffill(axis=0))
# print(redf.ffill(axis=1))

df2 = pd.Series(np.arange(9), index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

# print("--------------------------")
# print(df2)
# print("--------------------------")
# print("\n B : ", df2['B'])

""" 
dataframe -> 2-D array
series -> 1-D array
"""

print("--------------------------")
print(df2[4:])
# print(df2 >= 4)
print(df2.drop('H'))