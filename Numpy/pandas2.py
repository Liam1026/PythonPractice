import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print(df)
print('-'*20)
# print(df['A'], df.A)
# print(df[0:3], df['20130102':'20130104'])

# select by label:loc
# print(df.loc['20130102'])
# print(df.loc[:, ['A','B']])
# print('^'*20)
# print(df.loc['20130102',['A','B']])
 
# select by position:iloc
# print(df.iloc[3:5,1:3])
# print(df.iloc[[1,3,5],1:3])

# mixed selection : ix
# print(df.ix[:3, ['A','C']])

# print(df[df.A>8])

# df.iloc[2,2] = 1111
# print(df)

# df.loc['20130101','B'] = 2222
# print(df)
# df[df.A>4] = 0
# print(df)

# df.A[df.A>4] = 0
# print(df)
# df['F'] = np.nan
# print(df)
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print(df)




