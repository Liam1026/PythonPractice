import pandas as pd

data = pd.read_csv('./Numpy/student.csv')
print(data)

data.to_pickle('./Numpy/student.pickle')

