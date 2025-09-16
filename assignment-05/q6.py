import numpy as np

# Define the three vectors
f = np.array([0, 1])  # |f>
g = (1 / np.sqrt(2)) * np.array([1, 1j])  # |g>
h = np.array([0, 1])  # |h>

# Compute the tensor product of the three vectors
tensor_f_g = np.kron(f, g)  # |f> ⊗ |g|
tensor_f_g_h = np.kron(tensor_f_g, h)  # (|f> ⊗ |g>) ⊗ |h|

# Print the result and the dimension of the resulting space
print("Q6: Verifying Tensor Product of Three Vectors")
print("Tensor product |f> ⊗ |g> ⊗ |h> = \n", tensor_f_g_h)
print("Dimension of the resulting space: ", tensor_f_g_h.shape[0])
