from qiskit import QuantumCircuit, ClassicalRegister, transpile
from qiskit.transpiler import assemble


# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate
qc.measure(0, 0)  # Measure qubit into classical bit

# Use the Aer simulator
simulator = Aer.get_backend('qasm_simulator')

# Transpile and assemble
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Run the simulation
result = simulator.run(qobj).result()
counts = result.get_counts()

# Print and plot the results
print("Measurement results:", counts)
qc.draw('mpl')  # Show the circuit diagram
plt.show()
