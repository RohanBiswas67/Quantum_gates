import numpy as np
from qiskit import *
import time as t

class Quantum_CCNOT_operation:
    def __init__(self, num_qubits=3):
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(self.num_qubits, 'q')
        self.cr = ClassicalRegister(self.num_qubits, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)

    def classic(self):
        # Define classical operations for the CCNOT gate
        zero_state_classical = np.array([[1], [0], [0], [0], [0], [0], [0], [0]])  # |000>
        one_state_classical = np.array([[0], [1], [0], [0], [0], [0], [0], [0]])   # |001>
        two_state_classical = np.array([[0], [0], [1], [0], [0], [0], [0], [0]])   # |010>
        three_state_classical = np.array([[0], [0], [0], [1], [0], [0], [0], [0]])  # |011>
        four_state_classical = np.array([[0], [0], [0], [0], [1], [0], [0], [0]])  # |100>
        five_state_classical = np.array([[0], [0], [0], [0], [0], [1], [0], [0]])  # |101>
        six_state_classical = np.array([[0], [0], [0], [0], [0], [0], [1], [0]])  # |110>
        seven_state_classical = np.array([[0], [0], [0], [0], [0], [0], [0], [1]])  # |111>

        # Apply CCNOT gate classically
        CCNOT_operator = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],  # |000>
            [0, 1, 0, 0, 0, 0, 0, 0],  # |001>
            [0, 0, 1, 0, 0, 0, 0, 0],  # |010>
            [0, 0, 0, 1, 0, 0, 0, 0],  # |011>
            [0, 0, 0, 0, 1, 0, 0, 0],  # |100>
            [0, 0, 0, 0, 0, 1, 0, 0],  # |101>
            [0, 0, 0, 0, 0, 0, 0, 1],  # |110>
            [0, 0, 0, 0, 0, 0, 1, 0],  # |111>
        ])

        out_zero_classical = (np.dot(CCNOT_operator, zero_state_classical))
        out_one_classical = (np.dot(CCNOT_operator, one_state_classical))
        out_two_classical = (np.dot(CCNOT_operator, two_state_classical))
        out_three_classical = (np.dot(CCNOT_operator, three_state_classical))
        out_four_classical = (np.dot(CCNOT_operator, four_state_classical))
        out_five_classical = (np.dot(CCNOT_operator, five_state_classical))
        out_six_classical = (np.dot(CCNOT_operator, six_state_classical))
        out_seven_classical = (np.dot(CCNOT_operator, seven_state_classical))

        # Print classical results
        print("Classically:")
        print(f"Before CCNOT gate |000>:\n{zero_state_classical}")
        print(f"Before CCNOT gate |001>:\n{one_state_classical}")
        print(f"Before CCNOT gate |010>:\n{two_state_classical}")
        print(f"Before CCNOT gate |011>:\n{three_state_classical}")
        print(f"Before CCNOT gate |100>:\n{four_state_classical}")
        print(f"Before CCNOT gate |101>:\n{five_state_classical}")
        print(f"Before CCNOT gate |110>:\n{six_state_classical}")
        print(f"Before CCNOT gate |111>:\n{seven_state_classical}")
        print(f"After CCNOT gate |000>:\n{out_zero_classical}")
        print(f"After CCNOT gate |001>:\n{out_one_classical}")
        print(f"After CCNOT gate |010>:\n{out_two_classical}")
        print(f"After CCNOT gate |011>:\n{out_three_classical}")
        print(f"After CCNOT gate |100>:\n{out_four_classical}")
        print(f"After CCNOT gate |101>:\n{out_five_classical}")
        print(f"After CCNOT gate |110>:\n{out_six_classical}")
        print(f"After CCNOT gate |111>:\n{out_seven_classical}")
        
        return

    def quantum(self):
        # Initialize a quantum circuit with the specified number of qubits
        simulator = Aer.get_backend('statevector_simulator')
        # Initialize a state vector for all basis states: |000>, |001>, |010>, |011>, |100>, |101>, |110>, |111>
        initial_states = [
            [1, 0, 0, 0, 0, 0, 0, 0],  # |000>
            [0, 1, 0, 0, 0, 0, 0, 0],  # |001>
            [0, 0, 1, 0, 0, 0, 0, 0],  # |010>
            [0, 0, 0, 1, 0, 0, 0, 0],  # |011>
            [0, 0, 0, 0, 1, 0, 0, 0],  # |100>
            [0, 0, 0, 0, 0, 1, 0, 0],  # |101>
            [0, 0, 0, 0, 0, 0, 1, 0],  # |110>
            [0, 0, 0, 0, 0, 0, 0, 1],  # |111>
        ]

        quantum_results = []

        for initial_state in initial_states:
            self.qc.initialize(initial_state)
        
            # Apply CCNOT gate quantum operation
            self.qc.ccx(2,1,0)  # Apply CCNOT gate to the three qubit
        
            result = execute(self.qc, simulator).result()
            statevector = np.asarray(result.get_statevector())  # Cast to NumPy array
            quantum_results.append(statevector.real)

        # Print quantum results for all basis states
        print("\nQuantum:")
        basis_states = ['|000>', '|010>', '|010>', '|011>', '|100>', '|101>', '|110>', '|111>']
        for i, initial_state in enumerate(initial_states):
            print(f"Before CCNOT gate {basis_states[i]}:\n{initial_state}")
        print("\n")
        for i, initial_state in enumerate(initial_states):
            print(f"After CCNOT gate {basis_states[i]}:\n{quantum_results[i]}")
            
        return



# Create an instance of the Quantum_CCNOT_operation class with 3 qubits
quantum_ccnot = Quantum_CCNOT_operation(3)

# Call the classic and quantum methods
print("This is for the Toffoli Gate (CCNOT Gate)\n")
quantum_ccnot.classic()  # Call the classical CCNOT gate operation
quantum_ccnot.quantum()  # Call the quantum CCNOT gate operation
