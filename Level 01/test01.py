from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import Aer

circuit = QuantumCircuit(2)

circuit.h(0)

creg = ClassicalRegister(2, name='c')
circuit.add_register(creg)

# Measure both qubits
circuit.measure([0, 1], [0, 1])  # Simplified measurement syntax

# Get simulator and run
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(circuit, shots=1024)
result = job.result()

# Get counts
counts = result.get_counts()
print(counts)