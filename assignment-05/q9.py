import numpy as np

# Define the quantum states |f>, |e>, |g>, and |k>
f = np.array([1, 1])  # |f>
e = np.array([0, 1])  # |e>
g = np.array([1j, 1j])  # |g>
k = np.array([1j, 1])  # |k>

# Set n1 = n2 = 1 as given in the problem
n1 = 1
n2 = 1

# Compute the tensor products
tensor_f_g = np.kron(f, g)  # |f> ⊗ |g>
tensor_e_k = np.kron(e, k)  # |e> ⊗ |k>

# Compute the inner product of tensor products
inner_product = np.dot(tensor_f_g.conj(), tensor_e_k)  # <f| ⊗ <g| and |e> ⊗ |k>

# Print the result
print("Q9: Verifying Inner Product of Tensor Products")
print("Inner product ⟨f| ⊗ ⟨g| and |e> ⊗ |k> = ", inner_product)
