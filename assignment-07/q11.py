from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.x(1)  # prepare |10> (MSB/bottom wire = 1)
qc.cx(0, 1)
qc.cx(1, 0)
qc.cx(0, 1)
qc.measure_all()

sim = AerSimulator()
res = sim.run(transpile(qc, sim), shots=1024).result()
print(res.get_counts())  # expect {'01': 1024}
