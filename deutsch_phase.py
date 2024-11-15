'''
Cirq: Exercise 4 - Implementing SWAP
Name: Nico Nap
UvAnetID: 14259338

This file contains an implementation of Deutsch's algorithm in the form of a
circuit using Cirq.
'''
import cirq


def deutsch(oracle):
    '''Construct a ciruit that returns f(0) XOR f(1) while calling the oracle
    only once.

    Parameters:
    oracle (cirq.Gate): The oracle to use in the circuit.

    Returns:
    cirq.Circuit: The circuit that gives f(0) XOR f(1) with probability 1.
    '''
    circuit = cirq.Circuit()
    # LineQubit(0) is a qubit in the |+> state.
    qubit = cirq.LineQubit(0)
    circuit.append(oracle(qubit))
    circuit.append(cirq.H(qubit))
    circuit.append(cirq.measure(qubit, key='result'))
    return circuit
