"""MULTILEVELED INDEXING"""

import numpy as np
import pandas as pd

# srs = pd.Series(np.arange(5), index=[['A','A','B','B','B'],[1,2,3,4,5]])
# print(srs)
# print(srs['A'])

df = pd.DataFrame(np.arange(25).reshape(5,5), index=[['A','A','A','B','B'], [1,2,3,4,5]],
                        columns=[['USA', 'Pak', 'Pak', 'UK','Ind'], ['Day', 'Day','Night', 'Night', 'Night']])
print(df)
