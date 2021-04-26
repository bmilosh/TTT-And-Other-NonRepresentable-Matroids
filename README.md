# TTT-And-Other-NonRepresentable-Matroids

The files here correspond to some results of my thesis that are not included in https://github.com/bmilosh/Common-Information-and-Matroid-Ports .
Specifically, they relate to the recursive implementations of the Euclidean intersection (EP) and the generalized Euclidean intersection properties (GP), and visualizations of the TTT matroids.
The EP and GP implementations can be used to find matroids that are not linearly representable.

allnonGPMats.py contains the 288 Ingleton-compliant (5,9) matroids that do not satisfy GP at depth 1.

chcekEP.ipynb is a Jupyter notebook that contains tools needed to check if a matroid is k-EP for some positive integer k.
chcekGP.ipynb is a Jupyter notebook that contains tools needed to check if a matroid is k-GP for some positive integer k.
Both these notebooks were created using SageMath version 9.1 .

mat94unk_alg.py contains all 9,572 (4,9) matroids that Bollen was unable to determine their 2-algebraic status.
mat95unk_alg.py contains all 12,129 (5,9) matroids that Bollen was unable to determine their 2-algebraic status.

vam.py contains some special matroids: the 5 Ingleton-compliant non-linear (4,8) matroids and the 39 non-Ingleton-compliant (4,8) matroids.

plot_TTT_matroids.ipynb is a Jupyter notebook that shows how the TTT matroids are related to one another by circuit-hyperplane relaxations.

Each file contains more information as deemed necessary.

Links to other resources used here:
Bollen database: https://github.com/gpbollen/Algebraicity-of-Matroids-and-Frobenius-Flocks . 
Royle and Mayhew database: http://doi.org/10.26182/5e3378f0ca2cd .
