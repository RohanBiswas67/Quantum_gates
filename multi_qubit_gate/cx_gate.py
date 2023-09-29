import numpy as np
from qiskit import *
import time as t

class Quantum_CNOT_operation:
    def __init__(self, num_qubits=2):
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(self.num_qubits, 'q')
        self.cr = ClassicalRegister(self.num_qubits, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)

    def classic(self):
        # Define classical operations for the CNOT gate
        # For a 2-qubit system, CNOT gate acts as an identity gate on the classical states.
        zero_state_classical = np.array([[1], [0], [0], [0]])  # |00>
        one_state_classical = np.array([[0], [1], [0], [0]])   # |01>
        two_state_classical = np.array([[0], [0], [1], [0]])   # |10>
        three_state_classical = np.array([[0], [0], [0], [1]])  # |11>

        # Apply CNOT gate classically
        CNOT_operator = np.array([[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 0, 1],
                                  [0, 0, 1, 0]])

        out_zero_classical = np.dot(CNOT_operator, zero_state_classical)
        out_one_classical = np.dot(CNOT_operator, one_state_classical)
        out_two_classical = np.dot(CNOT_operator, two_state_classical)
        out_three_classical = np.dot(CNOT_operator, three_state_classical)

        # Print classical results
        print("Classically:")
        print(f"Before CNOT gate |00>:\n{zero_state_classical}")
        print(f"Before CNOT gate |01>:\n{one_state_classical}")
        print(f"Before CNOT gate |10>:\n{two_state_classical}")
        print(f"Before CNOT gate |11>:\n{three_state_classical}")
        print(f"After CNOT gate |00>:\n{out_zero_classical}")
        print(f"After CNOT gate |01>:\n{out_one_classical}")
        print(f"After CNOT gate |10>:\n{out_two_classical}")
        print(f"After CNOT gate |11>:\n{out_three_classical}")
        
        return

    def quantum(self):
        # Initialize a quantum circuit with the specified number of qubits
        simulator = Aer.get_backend('statevector_simulator')
        # Initialize a state vector for all basis states: |00>, |01>, |10>, |11>
        initial_states = [
            [1, 0, 0, 0],  # |00>
            [0, 1, 0, 0],  # |01>
            [0, 0, 1, 0],  # |10>
            [0, 0, 0, 1]   # |11>
        ]

        quantum_results = []

        for initial_state in initial_states:
            self.qc.initialize(initial_state)
        
            # Apply CNOT gate quantum operation
            self.qc.cx(1,0)  # Apply CNOT gate to the second qubit
        
            result = execute(self.qc, simulator).result()
            statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
            quantum_results.append(statevector.real)

        # Print quantum results for all basis states
        print("\nQuantum:")
        basis_states = ['|00>', '|01>', '|10>', '|11>']
        for i, initial_state in enumerate(initial_states):
            print(f"Before CNOT gate {basis_states[i]}:\n{initial_state}")
        for i, initial_state in enumerate(initial_states):
            print(f"After CNOT gate {basis_states[i]}:\n{quantum_results[i]}")
            
        return



# Create an instance of the Quantum_CNOT_operation class with 2 qubits
quantum_cnot = Quantum_CNOT_operation(2)

# Call the classic and quantum methods
print("This is for the Controlled-X Gate (CNOT Gate)\n")
quantum_cnot.classic()  # Call the classical CNOT gate operation
quantum_cnot.quantum()  # Call the quantum CNOT gate operation
