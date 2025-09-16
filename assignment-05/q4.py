import numpy as np

# ------------------------------- Q1: Verify Unitary Matrix -------------------------------

# Define the sigma_x and sigma_y eigenvectors
sigma_x_plus = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])  # |+>
sigma_x_minus = np.array([1 / np.sqrt(2), -1 / np.sqrt(2)])  # |->

sigma_y_plus_i = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)])  # |+i>
sigma_y_minus_i = np.array([1 / np.sqrt(2), -1j / np.sqrt(2)])  # |-i>

# Define the Unitary matrix U for transformation from sigma_y to sigma_x eigenbasis
U = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# Verify the transformation of |+i> and |-i> to |+> and |->
result_plus = U @ sigma_y_plus_i
result_minus = U @ sigma_y_minus_i

print("Q1: Verifying Unitary Matrix")
print("U|+i> = ", result_plus)
print("U|-i> = ", result_minus)
print()

# ------------------------------- Q2: Verify Completeness of Eigenvectors -------------------------------

# Compute the outer products of the eigenvectors of sigma_x
outer_plus = np.outer(sigma_x_plus, sigma_x_plus.conj())
outer_minus = np.outer(sigma_x_minus, sigma_x_minus.conj())

# Compute the sum of the outer products
completeness_check = outer_plus + outer_minus

print("Q2: Verifying Completeness of Eigenvectors")
print("Sum of outer products = \n", completeness_check)
print("Identity matrix = \n", np.eye(2))
print()

# ------------------------------- Q3: Verify Construction of sigma_x -------------------------------
# Construct sigma_x using its eigenvalues and eigenvectors without scaling by 1/2
sigma_x_constructed = np.outer(sigma_x_plus, sigma_x_plus.conj()) - np.outer(
    sigma_x_minus, sigma_x_minus.conj()
)

# Define the standard sigma_x matrix
sigma_x_standard = np.array([[0, 1], [1, 0]])

print("Q3: Verifying Construction of sigma_x")
print("Constructed sigma_x = \n", sigma_x_constructed)
print("Standard sigma_x = \n", sigma_x_standard)
