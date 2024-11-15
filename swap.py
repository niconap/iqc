'''
Cirq: Exercise 4 - Implementing SWAP
Name: Nico Nap
UvAnetID: 14259338

This file contains an implementation of the SWAP circuit using Cirq.
'''
import cirq


def swap(qubit1, qubit2):
    '''Construct a ciruit that swaps the values of two qubits.

    Parameters:
    qubit1 (cirq.Qubit): The first qubit to swap.
    qubit2 (cirq.Qubit): The second qubit to swap.

    Returns:
    cirq.Circuit: The circuit that swaps the two qubits.
    '''
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubit1, qubit2))
    circuit.append(cirq.CNOT(qubit2, qubit1))
    circuit.append(cirq.CNOT(qubit1, qubit2))
    return circuit
