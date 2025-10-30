# Notions essentielles de mécanique quantique appliquées à l'informatique:

## Vecteurs, matrices, produit matriciel et notation "braket":

#### Vecteurs:

Un vecteur est (en gros) une rangée de nombres à qui on impose des propriétés particulières. En général, un vecteur représente les coordonnées d'un point dans un repère par rapport à l'origine.

<img src="file:///home/maxime/snap/marktext/9/.config/marktext/images/2025-09-13-19-14-47-image.png" title="" alt="" width="217">

*i)* **Addition de vecteurs**:

$\begin{pmatrix} a \\ b \end{pmatrix} + \begin{pmatrix} c \\ d \end{pmatrix} = \begin{pmatrix} a+c \\ b+d \end{pmatrix}$

<img src="file:///home/maxime/snap/marktext/9/.config/marktext/images/2025-09-13-19-15-08-image.png" title="" alt="" width="431">

*ii)* **Multiplication par un nombre**:

$\lambda \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} \lambda a \\ \lambda b \end{pmatrix}$

<img src="file:///home/maxime/snap/marktext/9/.config/marktext/images/2025-09-13-19-15-26-image.png" title="" alt="" width="433">

*iii)* **Produit scalaire**:

$\begin{pmatrix} a \\ b \end{pmatrix} \cdot \begin{pmatrix} c \\ d \end{pmatrix} = \begin{pmatrix} a & b \end{pmatrix} \begin{pmatrix} c \\ d \end{pmatrix} = ac+bd$

#### Matrices:

Une matrice est (en gros) un tableau de nombres à qui on impose des propriétés particulières:

*i)* **Addition de matrices**:

$\begin{pmatrix} a & b\\ c & d \end{pmatrix} + \begin{pmatrix} e & f\\ g & h \end{pmatrix} = \begin{pmatrix} a+e & b+f\\ c+g & d+h \end{pmatrix}$

*ii)* **Multiplication par un nombre**:

$\lambda \begin{pmatrix} a & b\\ c & d \end{pmatrix} = \begin{pmatrix} \lambda a & \lambda b\\\ \lambda c & \lambda d \end{pmatrix}$

*iii)* **Multiplication d'une matrice et d'un vecteur** ("plusieurs produits scalaires, ligne par ligne"):

$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} au+bv \\ cu+dv \end{pmatrix}$

**IMPORTANT:** Effets d'une multiplication d'un vecteur par une matrice = rotation et/ou changement de longueur du vecteur.

<img src="file:///home/maxime/snap/marktext/9/.config/marktext/images/2025-09-13-19-16-09-image.png" title="" alt="" width="406">

## Bits et portes logiques classiques:

Les ordinateurs classiques (ceux que l'on utilise tous les jours) traitent de l'information écrite sous forme de **bits**, c'est-à-dire des 0 et des 1. L'association de ces bits permet de former des nombres, mots, des symboles,... La façon de traiter ces informations se fait au travers d'opérations ou transformations que l'on peut effectuer sur ces bits grâce des **portes logiques**. Voici quelques exemples de portes logiques les plus utilisées dans circuits électronique:

- **AND** (ET):

- **OR** (ou):

- **XOR** (ou exclusif):

- **NAND**:
  
  <mark>Montrer l'addition de deux nombres?</mark>

Il est possible d'appliquer ces portes logiques à la chaîne et de former ainsi des **circuits logiques**. 

## Etats superposés et qubits:

Il a été démontré que la matière se comporte comme une onde et cela s'observe notamment dans les atomes (mais aussi à l'oeil nus -> BEC) et des températures basses (autour du zéro absolu mais pas que -> trous noirs). Par exemple, on a observé que les électrons d'un atome ne sont pas des petites billes qui tournent autour du noyau, mais en fait des des particules délocalisées, distribuées dans l'espace et la mesure de leur position est probabiliste. Un électron peut être vu comme un nuage, symbolisant qu'il est partout en même temps autour du noyau.

Ainsi, la mesure de sa position peut prendre un grand nombre de valeur (infinité). Il existe des systèmes (voir plus tard) qui peuvent occuper seulement deux états (ou "positions") et peuvent servir d'équivalents quantiques des bits classiques, que l'on nomme des **qubits**. 

<mark>Différence entre qubit et pièce de monnaie (pile ou face)?</mark>

Ces états qu'un système peut occuper (même pour les bits classiques, on n'a pas encore précisé ce que ce 0 et 1 veulent dire), appelons-les $\ket 0$ et $\ket 1$. Classiquement, un système peut être soit dans l'état $\ket 0$ soit dans l'état $\ket 1$. En mécanique quantique, le qubit peut occuper un de ces deux états ou une combinaison des deux, appelée **superposition d'états**. Par contre, lorsque l'on veut connaître dans quel état il se trouve, la mesure nous indiquera parfois 0 et parfois 1, avec une certraine probabilitié (comme pour la position de l'électron). La façon de noter cette superposition est en fait comme suit:

$ \qquad \alpha \ket 0 + \beta \ket 1 $ 

et les coefficients $\alpha$ et $\beta$ renferment la probabilité de mesurer $\ket 0$ ou $\ket 1$, respectivement: $P(0) = |\alpha|^2$ et $P(1) = |\beta|^2$ (à noter que ce sont en fait des nombres complexes, mais on verra sûrement ça plus tard), où $|\alpha|^2 + |\beta|^2 =1$.

On représentera l'état de notre système $\alpha \ket 0 + \beta \ket 1$ par

$ \qquad \begin{pmatrix} \alpha ,\ \beta \end{pmatrix} \begin{pmatrix} \ket{0} \\ \ket{1} \end{pmatrix},$

ou en version raccourcie, en un vecteur $\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$.

## Portes logiques quantiques:

Tout comme pour les bits classiques, on veut pouvoir manipuler les qubits et effectuer des opérations. Pour cela, on applique les équivalents quantiques des portes logiques. Concrètement, appliquer ces portes quantiques s'écrit comme des mutliplications consécutives de matrices sur un (ou plusieurs) qubit(s). Cette écriture est donc très pratique pour comprendre l'évolution des qubits dans un circuit.

## 
