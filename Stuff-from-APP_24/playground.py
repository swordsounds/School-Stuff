import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 
               4, 5, 6,
               7, 8, 9])
y = np.array([1, 2, 3,
              4, 5, 6,
              7, 8, 9])

fig, axes = plt.subplots(figsize=(20, 4), nrows=1, ncols=6)
plt.tight_layout()

axes[0].plot(x, y)
axes[1].plot(x, y)
plt.show()