import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data = data.cumsum()

# plot methods: 'bar','hist','box','kds',area,scatter, hexbin, pie

data.plot()
plt.show()

