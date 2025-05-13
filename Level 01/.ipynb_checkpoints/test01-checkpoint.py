import qiskit

circuit = qiskit.QuantumCircuit(2)

circuit.h(0)

creg = qiskit.ClassicalRegister(2, name ='c')

circuit.add_register(creg)

circuit.measure([0,1], [creg[0],creg[1]])

simulator = qiskit.Aer.get_backend('qasm_simulator')

result = qiskit.execute(circuit , simulator).result()

count = result.get_counts()
print(count)