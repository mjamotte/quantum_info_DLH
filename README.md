# Course plan

The course is divided into modules, grouped in the following categories:

- Category A: Lectures to be followed linearly
- Category B: Demonstrations with Qiskit
- Category C: (Optional) topics requiring an introduction to complex numbers
- Category D: (Optional) topics to go further

## Essential core modules:

A1. Introduction

- experiments showing that the world is quantum
- quantum vs classical computers
- main algorithms: what can we do with quantum computers?
- outline of the topics (modules) offered in this course
- explain that the subject requires 3 key math concepts (linear algebra, complex numbers, probabilities),
  but that our course will avoid complex numbers as much as possible to simplify the subject:
  the offering is therefore divided into "basic" modules (without complex numbers) and modules that require
  an introduction to complex numbers as a prerequisite.

A2. The qubit (without complex numbers)

- vector representation
- bra-ket representation
- superposition and the link between probability and coefficients
- single-qubit operations and their matrix description

B1. Qiskit: `quantum information` module (part 1)

- module introduction
- single-qubit operations

A3. Measurement [SKIP]

- measurement as projection (in the computational basis for now)
- geometric visualization
- algebraic notation: dot product, bra, and projectors (|0><0| notation and matrices)
- measurement reproducibility: P^2=P (this is why measurement is a projection)
- measurement reproducibility: states are eigenvectors of an observable (Z for the computational basis)
- projection onto arbitrary vectors: other bases and associated observables (e.g. X)

B1. Qiskit: `quantum information` module (part 2)

- single-qubit measurements

(Optional: insert here the "B2" demo on key distribution)

A4. Two-qubit systems

- tensor notation in bra-ket representation
- associativity and distributivity rules
- computational basis and labeling with binary numbering
- 2^n states encodable in n qubits
- vector representation notation
- action of single-qubit operators and tensor products of matrices
- two-qubit operators not decomposable into tensor products (swap, cx, cz)
- entanglement: illustrate with Bell pair
- Schmidt decomposition and consequence of entanglement on partial measurements

B1. Qiskit: `quantum information` module (part 3)

- two-qubit operations

A5. Circuits and logic gates

- draw the parallel with classical logic gates in electronic circuits
- symbolic representation of a computation on QPU
- the circuit describes the construction of a quantum state from |00...0>
- computing model: circuit -> execution on QPU -> measurement results

B3. Qiskit: `circuit` module

- circuit construction
- matrices behind the logic gates
- constructing a Bell pair

B4. Qiskit: execution on QPU

- different backends (real QPUs and simulators)
- transpilation
- primitives
- demo with a Bell pair

## Optional demo modules from the core curriculum (recommended):

B2. Quantum key distribution

B5. Teleportation (and superdense coding?)

B6. Grover

## Modules including complex numbers:

C1. Introduction to complex numbers

C2. The qubit (with complex numbers)

- general state of a qubit
- conjugation and 'bra' vectors
- unitarity of matrices
- no-cloning
- complex logic gates
- Bloch sphere and link with rotations
- application: verifying transpiled circuits

C3. [not prepared] Mechanics of physical systems

- Hamiltonian, time evolution and Schrödinger equation

C4. [not prepared] Shor

- factorization: use for encryption [without complex numbers]
- factorization: Shor's algorithm [without complex numbers]
- phase estimation [with complex numbers]
- quantum Fourier transform [with complex numbers]

## Modules for further study:

D1. Measurements

D2. CHSH: interpretations of superpositions in quantum mechanics

D3. Physical platforms for building QPUs 

D4. [non-préparé] Matrices densités et états mixtes (bases)

D5. [non-préparé] Bruit et correction d'erreur (bases)

D6. [non-préparé] Algorithmes variationels (survol)
