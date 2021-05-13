import pandas as pd
import random

df = pd.DataFrame({'Animals': [random.choice(['Dog', 'Cat', 'Hamster', 'Fish'])for i in range(1, 16)],
                   'age': [random.choice(range(1,4)) for i in range(1, 16)],
                   'gender': [random.choice(['Male', 'Female']) for i in range(1, 16)]})

print(df)
Aw = df.groupby('Animals')

print("*******************MEAN***********************")
print(Aw.agg('mean'))

print("*******************VARIANCE***********************")
print(Aw.agg('var'))

print("*******************STANDARD DEVIATION***********************")
print(Aw.agg('std'))

print("*******************MAX/MIN***********************")
print(Aw.agg('max'))

print("*******************FIRST/LAST***********************")
print(Aw.agg('last'))

print("*******************COUNT***********************")
print(Aw.agg('count'))

print("*******************SIZE***********************")
print(Aw.agg('size'))

print("*******************DESCRIBE***********************")
print(Aw.agg('describe'))
