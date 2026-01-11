
## Modules essentiels du tronc commun:

1. Introduction
   - expériences montrant que le monde est quantique
   - ordis quant vs class
   - principaux algorithmes: que peux-t-on faire avec les ordis quantiques?
   - plan des sujets(modules) que l'on propose dans ce cours
   - expliquer que le sujet nécessite 3 notions clés de math (algèbre lin, complexes, probas),
     mais que notre cours évitera le plus possible les complexes afin de simplifier le sujet:
     l'offre est donc divisée en modules "de base" (sans complexes) et modules qui nécessitent
     une introduction sur les nombres complexes en pré-requis.

2. Le qubit (sans nombres complexes)
   - représentation vectorielle
   - représentation bra-ket
   - superposition et lien entre probabilité et coefficients
   - opérations sur 1 qubit et leur description en matrices

3. Qiskit: module `quantum information` (partie 1)
  - introduction du module
  - opérations sur un qubit

4. La mesure
  - la mesure comme projection (dans la base computationelle pour le moment)
  - visualisation géométrique
  - notation algébrique: produit scalaire, bra, et projecteurs (notations |0><0| et matrices)
  - reproductibilité de la mesure: P^2=P (c'est pourquoi la mesure est une projection)
  - reproductibilité de la mesure: les états sont des vecteurs propres d'une observable (Z pour la base computationnelle)
  - projection sur des vecteurs arbitraires: autres bases et observables associées (e.g. X)

3. Qiskit: module `quantum information` (partie 2)
  - mesures sur un qubit

(Insérer ici la démo sur la distribution de clés)

5. Systèmes à deux qubits
  - notations tensorielle en représentation bra-ket
  - règles d'associativité et distributivité
  - base computationnelle et label avec la numérotation binaire
  - superdense coding: 2^n états encodable dans n qubits
  - notations en représentation vectorielle
  - action des opérateurs à un qubit et produits tensoriels de matrices 
  - opérateurs à deux qubit non-décomposables en produit tensorielle (swap, cx, cz)
  - intrication: illustrer avec paire de Bell
  - décomposition de Schmidt et conséquence de l'intrication sur les mesures partielles

3. Qiskit: module `quantum information` (partie 3)
  - opérations sur deux qubits

6. Circuits et portes logiques
  - représentation symbolique d'un calcul sur QPU
  - le circuit décrit la construction d'un état quantique depuis |00...0>
  - modèle de calcul: circuit -> exécution sur QPU -> résultats de mesures
  - faire le parallèle avec les portes logiques classiques dans les circuits électroniques

7. Qiskit : module `circuit`
  - construction de circuits
  - matrices derrières les portes logiques
  - construction d'une paire de Bell

8. Qiskit: exécution sur QPU
 - différentes backends (vrai QPUs et simulateurs)
 - transpilation
 - primitives
 - démo avec une paire de Bell



## Modules de démo optionnels du tronc commun (recommandés):

9. Distribution quantique de clés

10. Téléportation (et superdense coding?)

11. Grover



## Modules pour approfondir:

12. Platformes physiques pour construire des QPUs 

13. CHSH

14. [non-préparé] Bruit et correction d'erreur (bases)

15. [non-préparé] Algorithmes variationels (survol)

16. [non-préparé] Matrices densités et états mixtes (bases)



## Modules incluant des nombres complexes:

17. Introduction des nombres complexes

18. Le qubit (avec nombres complexes)
  - état général d'un qubit
  - conjugaison et vecteurs 'bra'
  - unitarité des matrices
  - no-cloning
  - portes logiques complexes
  - sphère de Bloch et lien avec les rotations
  - application: vérifier les circuits transpilés

19. [non-préparé] Mécanique des systèmes physiques
  - Hamiltonien, évolution temporelle et équation de Schrödinger

20. [non-préparé] Shor
  - factorisation: utilisation pour le chiffrement [sans complexes]
  - factorisation: algorithme de Shor [sans complexes]
  - estimation de phase [avec complexes]
  - transformée de Fourier quantique [avec complexes]



