import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=['A', 'B', 'C'], columns=['a', 'b', 'c', 'd'])
print(df)
print(".....................................")
print(df[df['d'] > 6])

print(".....................................")
print(df.loc['C'])

print(".....................................")
print(df.drop('B'))

print(".....................................")
print(df.drop('b', axis=1))
# dropping in column requires axis=1 while dropping not necessarily requires axis=0

