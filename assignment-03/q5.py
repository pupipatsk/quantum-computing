import numpy as np

sigmay = np.array([[0, -1j], [1j, 0]], dtype=complex)

sigmay_dagger = sigmay.conj().T

print("σ_y:\n", sigmay)
print("\nσ_y^†:\n", sigmay_dagger)
print("\nHermitian? ->", np.allclose(sigmay, sigmay_dagger))
