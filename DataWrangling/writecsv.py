import pandas as pd

# df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# df.to_csv("abc.csv")

df = pd.read_csv("abc.csv", header=None)
print(df)