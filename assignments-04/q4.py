import numpy as np

# Basis projectors for σ_z
P0 = np.array([[1, 0], [0, 0]], dtype=complex)  # |0><0|
P1 = np.array([[0, 0], [0, 1]], dtype=complex)  # |1><1|

# σ_x and its eigenvectors (columns)
sigmax = np.array([[0, 1], [1, 0]], dtype=complex)
evals, evecs = np.linalg.eig(sigmax)
# evecs[:,0] ~ |+>, evecs[:,1] ~ |-> (up to a global phase)

# Ensure column vectors (kets)
ket_plus = evecs[:, [0]]  # shape (2,1)
ket_minus = evecs[:, [1]]  # shape (2,1)

# Bras are conjugate-transposes
bra_plus = np.transpose(ket_plus.conj())  # <+|
bra_minus = np.transpose(ket_minus.conj())  # <-|

# Probabilities via projectors: <ψ|P|ψ>
p_up_plus = np.dot(bra_plus, np.dot(P0, ket_plus))  # scalar 1x1
p_down_plus = np.dot(bra_plus, np.dot(P1, ket_plus))
p_up_minus = np.dot(bra_minus, np.dot(P0, ket_minus))
p_down_minus = np.dot(bra_minus, np.dot(P1, ket_minus))

print("Eigenvalues of σ_x:", evals)
print("P(up) for |+>:", np.real_if_close(p_up_plus[0, 0]))
print("P(down) for |+>:", np.real_if_close(p_down_plus[0, 0]))
print("P(up) for |->:", np.real_if_close(p_up_minus[0, 0]))
print("P(down) for |->:", np.real_if_close(p_down_minus[0, 0]))
