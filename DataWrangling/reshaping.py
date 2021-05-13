import numpy as np
import pandas as pd

# df = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
#
# print(df.pivot('A', 'B', 'C'))
#
# stacked_df = df.stack()
#
# print(stacked_df)
#
# print(stacked_df.unstack())
#
# print(df.pivot())

# ddf = pd.DataFrame({'Company': ['Google', 'Microsoft', 'Apple'],
#                     'Product': ['Smartphone', 'Software', 'Iphone'],
#                     'Price': ['20000', '100000', '200000']})
# print(ddf)
#
# print(ddf.pivot('Company', 'Product', 'Price'))

# dict_map = {'Google': 'Sundar Pichai', 'Microsoft': 'Bill Gates', 'Apple': 'Tim Cook'}
#
# ddf['Owner'] = ddf['Company'].map(dict_map)
#
# print(ddf)

# df = pd.DataFrame({'Col1':['A', 'B', 'A', 'C', 'B', 'C'],
#                     'Col2': [1, 2, 7, 3, 4, 3]})

# print(df.duplicated())
# df_new = df.drop_duplicates()
# Only same index and value is considered as a duplicate value
# print(df_new)

df = pd.Series([1, 2, 2, 3, 4, 5, 6, 7, 8], index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
df1 = pd.read_csv("this.csv")
# print(df1)
# print(df.replace(1, 8))
# print(df1.rename(index=str.lower))
print(df.rename(index={'A': 'helloA'}))
