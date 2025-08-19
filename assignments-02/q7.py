import numpy as np

v1 = np.array([[3 / 2**0.5], [-1 / 2**0.5]])
print(f"v1: {v1}")

v2 = v1 / np.linalg.norm(v1)
print(f"v2: {v2}")
