import numpy as np

# Define the quantum states |f>, |g>, and |h>
f = np.array([0, 1])  # |f>
g = np.array([1, 0])  # |g>
h = np.array([0, 1])  # |h>

# Compute the tensor products
lhs_1 = np.kron(f, (g + h))  # |f> ⊗ (|g> + |h>)
rhs_1 = np.kron(f, g) + np.kron(f, h)  # |f> ⊗ |g> + |f> ⊗ |h>

lhs_2 = np.kron((f + g), h)  # (|f> + |g>) ⊗ |h>
rhs_2 = np.kron(f, h) + np.kron(g, h)  # |f> ⊗ |h> + |g> ⊗ |h>

# Print the results and check if the two sides are the same
print("Q7: Verifying Distribution Laws")

# Law 1: |f> ⊗ (|g> + |h>) = |f> ⊗ |g> + |f> ⊗ |h>
print("Law 1: |f> ⊗ (|g> + |h>) = |f> ⊗ |g> + |f> ⊗ |h>")
print("Left-hand side (|f> ⊗ (|g> + |h>)) = ", lhs_1)
print("Right-hand side (|f> ⊗ |g> + |f> ⊗ |h>) = ", rhs_1)

# Law 2: (|f> + |g>) ⊗ |h> = |f> ⊗ |h> + |g> ⊗ |h>
print("\nLaw 2: (|f> + |g>) ⊗ |h> = |f> ⊗ |h> + |g> ⊗ |h>")
print("Left-hand side ((|f> + |g>) ⊗ |h>) = ", lhs_2)
print("Right-hand side (|f> ⊗ |h> + |g> ⊗ |h>) = ", rhs_2)
