import numpy as np

# 1. Tensor Product of Operators
# Define two operators A and B (Example: Pauli-X and Pauli-Z matrices)
A = np.array([[0, 1], [1, 0]])  # Pauli-X operator (σ_x)
B = np.array([[1, 0], [0, -1]])  # Pauli-Z operator (σ_z)

# Compute the tensor product of operators A and B
tensor_product = np.kron(A, B)
print("Tensor product of A and B (A ⊗ B):")
print(tensor_product)
print()

# 2. Partial Measurement (Partial Trace)
# We want to compute the partial trace of a composite system described by the tensor product of operators A and B.
# In this case, we compute the partial trace over subsystem B (trace over the second subsystem).


# Function to compute the partial trace of a tensor product
def partial_trace(tensor):
    # Partial trace over the second subsystem (B)
    # For a 2x2 system, we trace out the second subsystem, reducing the 4x4 matrix to a 2x2 matrix.

    # The matrix is 4x4, so we want to sum over the diagonal elements that correspond to subsystem A.
    # We'll iterate through the 2x2 blocks in the 4x4 matrix and take the trace of each block.

    # Initialize partial trace result
    trace_result = np.zeros((2, 2))

    # Compute partial trace by summing over the diagonal blocks
    for i in range(2):
        for j in range(2):
            trace_result[i, j] = tensor[i * 2, j * 2] + tensor[i * 2 + 1, j * 2 + 1]

    return trace_result


# Compute partial trace over subsystem B (trace over the second subsystem)
partial_trace_result = partial_trace(tensor_product)
print("Partial trace over subsystem B:")
print(partial_trace_result)
print()

# 3. Matrix Representation of an Operator in a Given Basis
# Define the computational basis states |0> and |1>
basis_0 = np.array([1, 0])  # |0>
basis_1 = np.array([0, 1])  # |1>

# Now, let's compute the matrix elements of the operator A (Pauli-X) in the computational basis
O_matrix = np.array(
    [
        [np.dot(basis_0.T, np.dot(A, basis_0)), np.dot(basis_0.T, np.dot(A, basis_1))],
        [np.dot(basis_1.T, np.dot(A, basis_0)), np.dot(basis_1.T, np.dot(A, basis_1))],
    ]
)

print("Matrix representation of operator A (Pauli-X) in the computational basis:")
print(O_matrix)
print()

# 4. Boolean Comparison to Check if Partial Trace and Tensor Product Give the Same Result
# Check if partial trace and tensor product match
comparison_result = np.allclose(partial_trace_result, tensor_product[:2, :2])

print("Do the partial trace and tensor product give the same result?")
print(comparison_result)
