import pandas as pd

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

res = pd.merge(boys, girls, on='k', suffixes=['_boys', 'girls'], how='inner')
print(res)