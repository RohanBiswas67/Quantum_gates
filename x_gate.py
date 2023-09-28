import numpy as np
from qiskit import *
import time as t

class Quantum_x_operation:
    def __init__(self):
        self.num_qubits = 1
        self.qr = QuantumRegister(self.num_qubits, 'q')
        self.cr = ClassicalRegister(self.num_qubits, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)

    def classic(self):
        # Define classical operations for the X-gate
        zero_state_classical = np.array([[1], [0]])  # Zero state
        one_state_classical = np.array([[0], [1]])   # One state
        X_operator = np.array([[0, 1], [1, 0]])  # X Operator

        # Apply X-gate classically
        out_zero_classical = np.dot(X_operator, zero_state_classical)
        out_one_classical = np.dot(X_operator, one_state_classical)

        # Print classical results
        print("Classically:")
        print(f"Before X-gate zero state:\n{zero_state_classical}")
        print(f"Before X-gate one state:\n{one_state_classical}")
        print(f"After X-gate zero state:\n{out_zero_classical}")
        print(f"After X-gate one state:\n{out_one_classical}")
        
        return

    def quantum(self):
        # Initialize a quantum circuit with one qubit
        self.qc.initialize([1, 0], 0)
        simulator = Aer.get_backend('statevector_simulator')

        # Apply X-gate quantum operation to the zero state
        self.qc.x(0)
        result = execute(self.qc, simulator).result()
        statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
        zero_after_quantum = statevector.real

        # Reset the qubit, then apply X-gate to the one state
        self.qc.reset(0)
        self.qc.initialize([0, 1], 0)
        self.qc.x(0)
        result = execute(self.qc, simulator).result()
        statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
        one_after_quantum = statevector.real

        # Print quantum results
        print("\nQuantum:")
        print(f"Before X-gate zero state:\n[1, 0]")  # Initial state
        print(f"Before X-gate one state:\n[0, 1]")  # Initial state
        print(f"After X-gate zero state:\n{zero_after_quantum}")
        print(f"After X-gate one state:\n{one_after_quantum}")
        
        return

# Create an instance of the Quantum_x_operation class
quantum_ops = Quantum_x_operation()

# Call the classic and quantum methods
print("This is for One Single Qubit Gate (X-gate)\n")
quantum_ops.classic()  # Call the classical X-gate operation
quantum_ops.quantum()  # Call the quantum X-gate operation