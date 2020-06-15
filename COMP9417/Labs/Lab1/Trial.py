import matplotlib.pyplot as plt
import numpy as np

N = 100
data_x = np.arange(N)
rdm = (np.random.rand(N) - 0.5)
data_y1 = data_x + rdm*data_x
plt.scatter(data_x, data_y1, color = "blue")
plt.plot(data_x, data_x, "r-")
plt.show()