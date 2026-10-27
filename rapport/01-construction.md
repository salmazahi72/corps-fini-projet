# Construction des corps finis

## 1. Le corps F_p = Z/pZ
Quand p est premier, Z/pZ est un corps : tout élément non nul a un inverse.

Exemple F_2 : éléments 0 et 1, avec 1 + 1 = 0.

## 2. Le corps F_4
On prend P = X^2 + X + 1 (irréductible sur F_2).
On note α la classe de X, avec la règle α^2 = α + 1.
Éléments : 0, 1, α, α + 1.

### Table d'addition de F_4

| + | 0 | 1 | α | α+1 |
|---|---|---|---|---|
| **0** | 0 | 1 | α | α+1 |
| **1** | 1 | 0 | α+1 | α |
| **α** | α | α+1 | 0 | 1 |
| **α+1** | α+1 | α | 1 | 0 |

### Table de multiplication de F_4

| × | 0 | 1 | α | α+1 |
|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | α | α+1 |
| **α** | 0 | α | α+1 | 1 |
| **α+1** | 0 | α+1 | 1 | α |

Chaque élément non nul a un inverse (α et α+1 sont inverses l'un de l'autre), donc F_4 est un corps.
