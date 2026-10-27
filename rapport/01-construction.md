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

## 3. Le corps F_8

### Le polynôme irréductible
On prend P = X^3 + X + 1 sur F_2. Il est de degré 3 et n'a pas de racine dans F_2
(P(0) = 1 et P(1) = 1 + 1 + 1 = 1), donc il est irréductible.

On note α la classe de X. Comme P(α) = 0, on a α^3 + α + 1 = 0, donc (modulo 2) :

**α^3 = α + 1**

### Les 8 éléments
Tous les polynômes de degré ≤ 2 à coefficients dans F_2 :

0, 1, α, α+1, α^2, α^2+1, α^2+α, α^2+α+1

Donc |F_8| = 2^3 = 8.

### Les puissances de α

| Puissance | Calcul | Résultat |
|---|---|---|
| α^0 | | 1 |
| α^1 | | α |
| α^2 | | α^2 |
| α^3 | règle | α + 1 |
| α^4 | α(α+1) = α^2 + α | α^2 + α |
| α^5 | α(α^2+α) = α^3 + α^2 = (α+1) + α^2 | α^2 + α + 1 |
| α^6 | α(α^2+α+1) = α^3 + α^2 + α = (α+1) + α^2 + α | α^2 + 1 |
| α^7 | α(α^2+1) = α^3 + α = (α+1) + α | 1 |

Comme α^7 = 1, les 7 éléments non nuls sont α^0, ..., α^6 : α est un générateur
du groupe multiplicatif F_8^*, qui est cyclique d'ordre 7.

### Inverse
Comme α^7 = 1, l'inverse de α^k est α^(7-k). Exemple : l'inverse de α est α^6 = α^2 + 1.
Vérification : α(α^2 + 1) = α^3 + α = (α+1) + α = 1.
