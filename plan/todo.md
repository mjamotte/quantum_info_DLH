# TODO

## Mesure

- Déplacer explication des mesures dans la base computationnelle dans le chapitre présentant le qubit
- Concepts généraux dans chapitre "avancé" (projections sur états quelconques, autres bases, idempotence, vecteurs propres)
- Passer ce chapitre et le proposer comme module d'approfondissement
- Graphe pour illustrer que $\ket{\psi}\bra{\psi}$ fait une projection (bra extrait coef et ket est nouvelle direction)

## Distribution de clés

Slides d'abord:

- Expliquer avec application de Hadamard ($H^2=I$) au lieu des bases $X,Z$
- Tableau pour résumer les étapes
- Noter $H$ et $I$ au lieu des bits aléatoires: garder bits uniquement pour données

Notebook:

- Map bits aléatoires sur labels 'H' et 'I' pour plus de clarté

## Grover

Slides d'abord:

- Motiver avec applications concrètes
- Idée générale: évaluer tous les candidats en même temps
- Pas parler de la construction de l'oracle: seulement dire que la porte oracle marque la solution par signe
- Directement expliquer procédure géométrique pour amplifier le coefficient de la solution
- Graphe pour illustrer que $2 \ket{+}\bra{+}$ - I$ fait une réflection géométrique autour de $\ket{+}$

Notebook:

- Détailler pourquoi mcx est utilisé pour implémenter la réflexion géométrique
