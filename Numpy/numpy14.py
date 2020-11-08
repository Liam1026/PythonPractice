import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )

data = data.cumsum()
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()