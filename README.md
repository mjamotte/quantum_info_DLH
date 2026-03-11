# Introduction à l'informatique quantique

Cours introductif sur l'informatique quantique — Digital Learning Hub.

## Structure du cours

Le cours est divisé en modules, rassemblés dans quatre catégories:

- **Catégorie A** — Tronc commun (cours magistraux, à suivre de manière linéaire)
- **Catégorie B** — Démonstrations avec Qiskit (notebooks interactifs)
- **Catégorie C** — Sujets nécessitant les nombres complexes (optionnels)
- **Catégorie D** — Approfondissements (optionnels)

### A — Tronc commun

| Module | Titre | Fichier |
|--------|-------|---------|
| A1 | Introduction | `modules/A_tronc_commun/A1_introduction.tex` |
| A2 | Le qubit (vecteurs, matrices, portes) | `modules/A_tronc_commun/A2_qubit.tex` |
| A3 | La mesure | `modules/A_tronc_commun/A3_mesure.tex` |
| A4 | Systèmes à deux qubits | `modules/A_tronc_commun/A4_deux_qubits.tex` |
| A5 | Circuits et portes logiques | `modules/A_tronc_commun/A5_circuits_portes.tex` |

### B — Démonstrations Qiskit

| Module | Titre | Slides | Notebook(s) |
|--------|-------|--------|-------------|
| B0 | Installation Qiskit | — | `B0_qiskit_installation.ipynb` |
| B1 | quantum_info (1, 2 & 3) | `B1_qiskit_quantum_info.tex` | `B1_qiskit_quantum_info.ipynb`, `B1_qiskit_deux_qubits.ipynb` |
| B2 | Module circuit | `B2_qiskit_circuits.tex` | — |
| B3 | Exécution sur QPU | `B3_qiskit_qpu.tex` | — |
| B4 | Distribution quantique de clés | `B4_distribution_clefs.tex` | `B4_distribution_clefs.ipynb` |
| B5 | Téléportation | `B5_teleportation.tex` | `B5_teleportation_exercice.ipynb` |
| B6 | Grover | `B6_grover.tex` | `B6_grover.ipynb` |

### C — Nombres complexes

| Module | Titre | Fichier |
|--------|-------|---------|
| C1 | Introduction aux nombres complexes | `modules/C_nombres_complexes/C1_nombres_complexes.tex` |
| C2 | Le qubit avec nombres complexes | `modules/C_nombres_complexes/C2_qubit_complexe.tex` |

### D — Approfondissements

| Module | Titre | Fichier |
|--------|-------|---------|
| D1 | Plateformes quantiques | `modules/D_approfondissements/D1_plateformes.tex` |
| D2 | Inégalités de Bell (CHSH) | `modules/D_approfondissements/D2_chsh.tex` + `D2_chsh.ipynb` |

## Organisation des dossiers

```
modules/
  A_tronc_commun/       # Slides LaTeX du tronc commun (A1–A5)
  B_demos_qiskit/       # Slides + notebooks des démos Qiskit (B0–B6)
  C_nombres_complexes/  # Slides sur les nombres complexes (C1–C2)
  D_approfondissements/ # Slides d'approfondissement (D1–D2)
figures/                # Toutes les figures (chemin commun)
notebooks/              # Notebooks originaux (archive)
plan/                   # Plan du cours et bibliographie
slides/                 # Slides originaux (archive)
```

## Compilation

Chaque fichier `.tex` dans `modules/` est autonome et peut être compilé avec `pdflatex`. Les figures sont référencées via `\graphicspath{{../../figures/}}`.

## Auteurs

JAMOTTE Maxime, SCHOONEN Cédric — Digital Learning Hub
