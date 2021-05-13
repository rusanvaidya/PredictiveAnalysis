import pandas as pd
import numpy as np

df1 = pd.DataFrame({'pointer': ['A', 'B', 'C', 'B', 'A', 'D'], 'value_df1': [0, 1, 2, 3, 4, 5]})
df2 = pd.DataFrame({'pointer': ['B', 'C', 'B', 'D'], 'value_df2': [6, 7, 8, 9]})

#To merge the rows of two or more DataFrames based on a common column between them
# df3 = pd.merge(df1, df2)

#The left merge returns a DataFrame, which has all rows of the DataFrame placed on the left side of the merge() function.
# df3 = pd.merge(df1, df2, how='left')

# The right merge returns a DataFrame that has all the rows of the DataFrame placed on the right side of the merge() function.
# df3 = pd.merge(df1, df2, how='right')

# This function returns all the rows of both the DataFrames given in the merge() function.
# df3 = pd.merge(df1, df2, how='outer')

# print(df3)

"""Merge on multiple columns """

# df1 = pd.DataFrame({'column1':['Pak', 'USA', 'Pak', 'UK', 'Ind','None'], #Column 1
#                     'column2':['A', 'B', 'C', 'B', 'A', 'D'],            #Column 2
#                     'value_df1':[0,1,2,3,4,5]})
#
# df2 = pd.DataFrame({'column1':['USA', 'UK', 'None', 'USA', 'Pak','Ind'], #Column 1
#                     'column2':['B', 'Z', 'C', 'B','D','E'],              #Column 2
#                     'value_df2':[6,7,8,9,10,11]})
#
# print("Outer Merged DataFrame on Multiple Columns\n")
# print(pd.merge(df1, df2, on = ['column1', 'column2'], how = 'outer'))


"""MERGE ON INDEX"""
df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame(np.arange(10,13,1), index = ['A', 'B','C'], columns = ['values'])
print(df2)
print("Merged on index\n")
print(pd.merge(df1, df2, left_on='pointer', right_index=True))

