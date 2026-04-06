# TODO

## Qubit

## Single-qubit operations

## Circuits

- Teleportation exercise here? (circuit construction, QPU execution later)

## Measurement

- General concepts in "advanced" chapter (projections onto arbitrary states, other bases, idempotence, eigenvectors)
- Graph to illustrate that $\ket{\psi}\bra{\psi}$ performs a projection (bra extracts coefficient and ket is the new direction)
- Measurement in arbitrary bases, vector basis concept, link with X,Z operators

## Key distribution

Slides first:

- Explain with Hadamard application ($H^2=I$) instead of $X,Z$ bases
- Table to summarize the steps
- Write $H$ and $I$ instead of random bits: keep bits only for data

Notebook:

- Map random bits to 'H' and 'I' labels for clarity

## Grover

Slides first:

- Motivate with concrete applications
- General idea: evaluate all candidates simultaneously
- Do not discuss oracle construction: only say that the oracle gate marks the solution by sign
- Directly explain geometric procedure to amplify the solution coefficient
- Graph to illustrate that $2 \ket{+}\bra{+} - I$ performs a geometric reflection around $\ket{+}$

Notebook:

- Detail why mcx is used to implement the geometric reflection
- Exercise with qiskit quantum_info: visualize the statevector evolution

