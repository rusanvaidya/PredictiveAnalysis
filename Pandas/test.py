import pandas as pd

srs1 = pd.Series([81.99, 72.44, 62.02, 63.0, 74.11], index=['CN', 'NP', 'MMS', 'BPIT', 'INTS'])

# srs.name = "Marks"
# srs.index.name = "SUBJECT"
# print(srs.index.values)
# print(srs.values)
# print(srs)

srs2 = pd.Series([74.11, 44.01, 89.88, 81.99, 85.43], index=['INTS', 'IS', 'CG', 'CN', 'OODM'])
srs = srs1/srs2
srs.name = "Marks"
srs.index.name = "SUBJECT"
print(srs)

print("\n The indexes that are assigned ‘True’ are Null:")
print(pd.isnull(srs))

print("\n The indexes that are assigned ‘True’ are not Null:")
print(pd.notnull(srs))

print("\nIndexes that satisfy the condition are:")
print(srs[srs == 1.0])
