import numpy as np

sigmaz = np.array([[1, 0], [0, -1]])
print(np.matmul(sigmaz, sigmaz))
