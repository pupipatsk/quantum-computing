import numpy as np

# Original vector in |0>,|1> basis
v1 = np.array([[1], [2]])

# Normalize
v1_norm = v1 / np.linalg.norm(v1)

# Probability of measuring |0>
prob_0 = abs(v1_norm[0, 0]) ** 2

print("Normalized vector:\n", v1_norm)
print("Probability of |0>:", prob_0 * 100, "%")
