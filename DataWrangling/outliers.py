import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(900,3))

quantiles_df = (df.quantile([0.25,0.75]))

Q1 = quantiles_df[0][0.25]
Q3 = quantiles_df[0][0.75]

iqr = Q3 - Q1

lower_bound = (Q1 - (iqr * 1.5))
upper_bound = (Q3 + (iqr * 1.5))

col1 = df[0]

print("The outliers in the first column below the lower bound:")
print(col1[(col1 < lower_bound)], '\n*******************************************')

print("The outliers in the first column above the upper bound:")
print(col1[(col1 > upper_bound)], '\n*******************************************')

col1[(col1 < lower_bound)] = lower_bound

col1[(col1 > upper_bound)] = upper_bound

print("After Dealing with Outliers\n")

print("The outliers in the first column below the lower bound:")
print(col1[(col1 < lower_bound)], '\n*******************************************')

print("The outliers in the first column above the upper bound:")
print(col1[(col1 > upper_bound)], '\n*******************************************')