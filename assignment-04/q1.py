import numpy as np

sigmax = np.array([[0, 1], [1, 0]])
print(sigmax)
eigenvalues, eigenvectors = np.linalg.eig(sigmax)
print(eigenvalues)
print(eigenvectors)
