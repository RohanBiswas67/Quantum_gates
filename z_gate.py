import numpy as np
from qiskit import *
import time as t

class Quantum_z_operation:
    def __init__(self):
        self.num_qubits = 1
        self.qr = QuantumRegister(self.num_qubits, 'q')
        self.cr = ClassicalRegister(self.num_qubits, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)

    def classic(self):
        # Define classical operations for the Z-gate
        zero_state_classical = np.array([[1], [0]])  # Zero state
        one_state_classical = np.array([[0], [1]])   # One state
        z_operator = np.array([[1,0], [0,-1]])  # Z Operator

        # Apply Z-gate classically
        out_zero_classical = np.dot(z_operator, zero_state_classical)
        out_one_classical = np.dot(z_operator, one_state_classical)

        # Print classical results
        print("Classically:")
        print(f"Before Z-gate zero state:\n{zero_state_classical}")
        print(f"Before Z-gate one state:\n{one_state_classical}")
        print(f"After Z-gate zero state:\n{out_zero_classical}")
        print(f"After Z-gate one state:\n{out_one_classical}")
        
        return

    def quantum(self):
        
        zero_before=[1,0]
        one_before=[0,1]
        # Initialize a quantum circuit with one qubit
        self.qc.initialize(zero_before, 0)
        simulator = Aer.get_backend('statevector_simulator')

        # Apply Z-gate quantum operation to the zero state
        self.qc.z(0)
        result = execute(self.qc, simulator).result()
        statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
        zero_after_quantum = np.column_stack([statevector.real])

        # Reset the qubit, then apply Z-gate to the one state
        self.qc.reset(0)
        self.qc.initialize(one_before, 0)
        self.qc.z(0)
        result = execute(self.qc, simulator).result()
        statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
        one_after_quantum = np.column_stack([statevector.real])

        zero_before=np.column_stack([zero_before])
        one_before=np.column_stack([one_before])
        
        # Print quantum results
        print("\nQuantum:")
        print(f"Before Z-gate zero state:\n{zero_before}")  # Initial state 
        print(f"Before Z-gate one state:\n{one_before}")  # Initial state
        print(f"After Z-gate zero state:\n{zero_after_quantum}")
        print(f"After Z-gate one state:\n{one_after_quantum}")
        
        return

# Create an instance of the Quantum_z_operation class
quantum_ops = Quantum_z_operation()

# Call the classic and quantum methods
print("This is for One Single Qubit Gate (Z-gate)\n")
quantum_ops.classic()  # Call the classical Z-gate operation
quantum_ops.quantum()  # Call the quantum Z-gate operation