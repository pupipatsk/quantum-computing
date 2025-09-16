import numpy as np

g = np.array([[0], [1]])
h = np.array([[1 / np.sqrt(2)], [1j / np.sqrt(2)]])
print(np.kron(g, h))
print(np.kron(h, g))
print(np.kron(g, h) == np.kron(h, g))
