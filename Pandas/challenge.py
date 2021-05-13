import numpy as np
import pandas as pd

def Sum_Swap(df):
    minm_r = np.min(df, axis=1)  # Get minimum elements from all rows

    maxm_r = np.max(df, axis=1)  # Get maximum elements from all rows

    df['row_sum'] = minm_r + maxm_r  # Add the min & max values and assign them to new column

    minm_c = np.min(df, axis=0)  # Get minimum elements from all columns

    maxm_c = np.max(df, axis=0)  # Get maximum elements from all columns

    df.loc['col_sum'] = minm_c + maxm_c  # Add the min & max values and assign them to new row

    a, b = df['row_sum'].copy(), df.loc['col_sum'].copy()  # Store values of row and column in temparory variables

    df['row_sum'], df.loc['col_sum'] = b, a  # Interchange the values

    return df


df = pd.DataFrame(np.random.randint(1, 100, 25).reshape(5, 5))

df_res = Sum_Swap(df.copy())

print(df_res)