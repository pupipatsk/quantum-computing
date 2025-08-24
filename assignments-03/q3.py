import numpy as np

sigmay = np.array([[0, -1j], [1j, 0]])
print(np.matmul(sigmay, sigmay))
