import pandas as pd
import numpy as np

# # concatenating
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

# res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# print(res)

# # join ['inner','outer']
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

# print(df1)
# print(df2)
# res = pd.concat([df1,df2],join='outer')
# print(res)
# res1 = pd.concat([df1,df2],join='inner')
# print(res1)

# # res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])  # didn't work anymore
res = pd.concat([df1,df2],axis=1)
res = res.reindex(df1.index)
print(res)


