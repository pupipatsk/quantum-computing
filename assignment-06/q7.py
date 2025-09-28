import numpy as np

X = np.array([[0, 1], [1, 0]])
U = np.kron(X, X)
print(np.allclose(U.conj().T @ U, np.eye(4)))
