import pandas as pd

df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

print(df1)
print('<' * 10, '>' * 10)
print(df2)
print('<' * 10, '>' * 10)

# 依据col1进行合并，并启用indicator=True
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
print('<' * 10, '>' * 10)
# 自定indicator column的名称
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indictor_column')
print(res)