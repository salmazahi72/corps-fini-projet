# Étude Comparative des Représentations et Applications

## 1. Tableau Comparatif des Complexités

| Opération | Base Polynomiale | Base Normale | Logarithmes de Zech |
| :--- | :--- | :--- | :--- |
| **Addition** | Facile ($\mathcal{O}(n)$) | Facile ($\mathcal{O}(n)$) | Difficile (Table de Zech) |
| **Multiplication** | Moyenne ($\mathcal{O}(n^{1.58})$ avec Karatsuba) | Complexe (sauf avec ONB) | **Très Facile** ($\mathcal{O}(1)$ - addition) |
| **Élévation au carré** | Réduction polynomiale requise | **Quasi-Instantanée** (Décalage de bits) | Facile (Multiplication par 2) |
| **Inversion** | Algorithme d'Euclide Étendu ($\mathcal{O}(n^2)$) | Algorithme d'Itoh-Tsujii | **Instantanée** (Négation) |
| **Domaine d'élection** | Logiciel / CPU généraliste | Matériel / FPGA / ASIC | Corps de très petite taille ($q < 2^{16}$) |

---

## 2. Cas d'Étude : Le Corps $\mathrm{GF}(2^8)$ dans l'AES

Dans le standard de chiffrement symétrique **AES** (Advanced Encryption Standard), les opérations s'effectuent dans le corps fini $\mathrm{GF}(2^8)$ :
- **Polynôme irréductible de Rijndael :** $P(X) = X^8 + X^4 + X^3 + X + 1$ (représenté par `0x11B`).
- **Représentation choisie :** Base Polynomiale.
- **Opération clé `xtime()` :** La multiplication par $X$ (`0x02`) s'effectue via un décalage d'un bit vers la gauche, suivi d'un XOR avec `0x1B` en cas de dépassement (si le bit de poids fort vaut 1).
