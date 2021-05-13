# dataframe -> 2-D array
# series -> 1-D array

import pandas as pd

df = pd.read_csv("stats.csv")
# print("\n This is dataframe head \n", df.head())
# print("\n This is dataframe tail \n", df.tail())
#
# print("\n", df['Sex'].head())

# print(df.columns)
new_df = pd.DataFrame(df, columns=['Sex', 'Under 1'])
# # print(new_df)
# print(df.loc[1])
# print(df)
# print(df(columns='Females'))
# new_df['Under 1'] = 70
print(new_df)

# import pandas as pd
#
# srs1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# srs2 = pd.Series([4, 5, 6], index=['C', 'D', 'B'])
# print(srs1 + srs2)