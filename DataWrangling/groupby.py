import numpy as np
import pandas as pd

df = pd.DataFrame({'p1':['A','A','B','B','C','C'],'p2':['G1','G2','G1','G2','G1','G2'],
    'val_1':np.arange(1,7,1),'val_2':np.arange(7,13,1)})

print("The original DataFrame")
print(df, '\n*******************************************')

print("DataFrame after using groupby on p1 & p2 and Summing their values")
print(df.groupby(['p1','p2']).sum(), '\n*******************************************')
