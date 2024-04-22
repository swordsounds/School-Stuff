import pandas as pd

import numpy as np



data = np.array([1, 2, 3, np.nan, 5])

series = pd.Series(data)

print(data)
print(series)