import numpy as np

# Define basis states
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# Define |+> and |-> states
ket_plus = (ket0 + ket1) / np.sqrt(2)
ket_minus = (ket0 - ket1) / np.sqrt(2)

# Define Z-gate
Z = np.array([[1, 0], [0, -1]])

# Apply Z to |->
result = Z @ ket_minus

print("Z|-> =", result)
print("Should equal |+> =", ket_plus)
print("Is equal? ->", np.allclose(result, ket_plus))
