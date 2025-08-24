import numpy as np

# Define sigma_y and basis states
sigmay = np.array([[0, -1j], [1j, 0]], dtype=complex)

ket0 = np.array([[1.0], [0.0]])  # |0>
bra0 = ket0.conj().T  # <0|

# σ_y |0>
ket_result = sigmay @ ket0
print("σ_y |0> =\n", ket_result)  # expect [[0],[ i]]

# <0| σ_y
bra_result = bra0 @ sigmay
print("<0| σ_y =\n", bra_result)  # expect [[0, -i]]

print("Are σ_y|0> and <0|σ_y equal? ->", np.allclose(ket_result, bra_result))

# Check the Hermitian-conjugate relation:
lhs = ket_result.conj().T  # (σ_y |0>)^†
rhs = bra_result  # <0| σ_y
print("Are (σ_y|0>)^† and <0|σ_y equal? ->", np.allclose(lhs, rhs))
