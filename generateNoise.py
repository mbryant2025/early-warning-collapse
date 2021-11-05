import numpy as np
from matplotlib import pyplot as plt

arr = np.random.normal(loc=0.0, scale=1.0, size=150) * 2.09

for _ in range(5):
    arr *= np.random.normal(loc=0.0, scale=1.0, size=150) * 2.09

plt.plot(arr)
plt.show()
