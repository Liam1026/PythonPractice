import pandas as pd
# merge how = ['left', 'right', 'outer', 'inner'],default is 'inner'

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print('<' * 10, '>' * 10)
print(right)
print('<' * 10, '>' * 10)

# res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
# print(res)
# print('<' * 10, '>' * 10)
# res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
# print(res)

# res = pd.merge(left, right, on=['key1', 'key2'], how='left')
# print(res)
# print('<' * 10, '>' * 10)
# res = pd.merge(left, right, on=['key1', 'key2'], how='right')
# print(res)

# indicator=True会将合并的记录放在新的一列

