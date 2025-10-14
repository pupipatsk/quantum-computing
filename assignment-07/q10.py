from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# Create SWAP gate circuit with |11> input
qc = QuantumCircuit(2)
qc.x(0)
qc.x(1)
qc.cx(0, 1)
qc.cx(1, 0)
qc.cx(0, 1)
qc.measure_all()

# Use Aer simulator
sim = AerSimulator()
t_qc = transpile(qc, sim)
result = sim.run(t_qc).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
