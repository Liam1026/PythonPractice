import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

# res = df1.append(df2, ignore_index=True)
# print(res)

# res = df1.append([df2, df3], ignore_index=True)
# print(res)

res = df1.append(s1, ignore_index=True)
print(res)