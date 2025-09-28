import numpy as np

CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)

# Check U^† U = I
print(np.allclose(CNOT.conj().T @ CNOT, np.eye(4)))
# -> True

# (Optional) verify action on basis
basis = np.eye(4)
print((CNOT @ basis).round(0))
