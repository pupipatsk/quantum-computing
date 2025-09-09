import numpy as np

sigmax = np.array([[0, 1], [1, 0]])
sigmay = np.array([[0, -1j], [1j, 0]])
sigmaz = np.array([[1, 0], [0, -1]])

print("det(σ_x) =", np.linalg.det(sigmax))
print("det(σ_y) =", np.linalg.det(sigmay))
print("det(σ_z) =", np.linalg.det(sigmaz))
