from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.x(1)  # NOT on MSB
qc.cx(1, 0)  # CNOT
qc.measure([0, 1], [0, 1])

sim = AerSimulator()
compiled_circuit = transpile(qc, sim)
result = sim.run(compiled_circuit, shots=1000).result()
print(result.get_counts())
