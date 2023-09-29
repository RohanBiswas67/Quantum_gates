from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

class Quantum_SWAP_operation:
    def __init__(self, num_qubits=2):
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(self.num_qubits, 'q')
        self.cr = ClassicalRegister(self.num_qubits, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)
        
        
    def classical_swap(self):
        # Define classical operations for the SWAP gate
        zero_state_classical = np.array([[1], [0], [0], [0]])  # |00>
        one_state_classical = np.array([[0], [1], [0], [0]])   # |01>
        two_state_classical = np.array([[0], [0], [1], [0]])   # |10>
        three_state_classical = np.array([[0], [0], [0], [1]])  # |11>

        # Apply SWAP gate classically
        SWAP_operator = np.array([[1, 0, 0, 0],
                               [0, 0, 1, 0],
                               [0, 1, 0, 0],
                               [0, 0, 0, 1]])

        out_zero_classical = np.dot(SWAP_operator, zero_state_classical)
        out_one_classical = np.dot(SWAP_operator, one_state_classical)
        out_two_classical = np.dot(SWAP_operator, two_state_classical)
        out_three_classical = np.dot(SWAP_operator, three_state_classical)

        # Print classical results
        print("Classically:")
        print(f"Before SWAP gate |00>:\n{zero_state_classical}")
        print(f"Before SWAP gate |01>:\n{one_state_classical}")
        print(f"Before SWAP gate |10>:\n{two_state_classical}")
        print(f"Before SWAP gate |11>:\n{three_state_classical}\n")
        print(f"After SWAP gate |00>:\n{out_zero_classical}")
        print(f"After SWAP gate |01>:\n{out_one_classical}")
        print(f"After SWAP gate |10>:\n{out_two_classical}")
        print(f"After SWAP gate |11>:\n{out_three_classical}")

        return

    
    
    def quantum_swap(self):
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

            # Apply the built-in swap gate to exchange qubit states
            self.qc.swap(0, 1)

            result = execute(self.qc, simulator).result()
            statevector = result.get_statevector()

            # Convert statevector to the desired format
            quantum_result_list = np.asarray(statevector).tolist()
            quantum_results.append([complex(round(val.real, 3), round(val.imag, 3)) for val in quantum_result_list])

        # Print quantum results for all basis states
        print("\nQuantum (Swap Gate):")
        basis_states = ['|00>', '|01>', '|10>', '|11>']
        for i, initial_state in enumerate(initial_states):
            print(f"Before Swap {basis_states[i]}: {initial_state}")
        for i, initial_state in enumerate(initial_states):
            print(f"After Swap {basis_states[i]}: {quantum_results[i]}\n")

# Create an instance of the Quantum_SWAP_operation class with 2 qubits
quantum_swap = Quantum_SWAP_operation(2)

# Call the quantum_swap method
print("This is for the SWAP Gate.\n")
quantum_swap.classical_swap()
quantum_swap.quantum_swap()  # Call the quantum swap gate operation