from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# --- Build the circuit ---
qc = QuantumCircuit(2)
qc.x(0)  # prepare |01>
qc.swap(0, 1)  # single SWAP gate
qc.measure_all()

# --- Simulate locally ---
sim = AerSimulator()
t_qc = transpile(qc, sim)
result = sim.run(t_qc, shots=1024).result()
counts_sim = result.get_counts()

print("Simulation:", counts_sim)
plot_histogram(counts_sim)
