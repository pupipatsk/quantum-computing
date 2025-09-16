import numpy as np

sigma = np.array([[0, -1j], [1j, 0]])
print(f"sigma: {sigma}")

eigvalue, eigvector = np.linalg.eig(sigma)
print(f"eigvalue: {eigvalue}")
print(f"eigvector: {eigvector}")
print(f"eigvalue[0]: {eigvalue[0]}")
print(f"eigvector[0]: {eigvector[0]}")
print(f"eigvalue[1]: {eigvalue[1]}")
print(f"eigvector[1]: {eigvector[1]}")
