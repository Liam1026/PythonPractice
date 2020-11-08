import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
print(data)
print('<>' * 20)
# print(data.cumsum())

data = data.cumsum()
data.plot()
plt.show()


