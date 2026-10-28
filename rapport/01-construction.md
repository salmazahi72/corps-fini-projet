### Table de multiplication de $\mathbb{F}_4$

Rappel : $\alpha^2 = \alpha + 1$ et $\alpha \cdot (\alpha + 1) = \alpha^2 + \alpha = (\alpha + 1) + \alpha = 1$.

| $\times$ | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0$** | $0$ | $0$ | $0$ | $0$ |
| **$1$** | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| **$\alpha$** | $0$ | $\alpha$ | $\alpha+1$ | $1$ |
| **$\alpha+1$** | $0$ | $\alpha+1$ | $1$ | $\alpha$ |

---

## 3. Généralisation aux extensions $\mathbb{F}_{p^n}$

Soit $p$ un nombre premier et $n \ge 1$ un entier. Pour construire le corps fini $\mathbb{F}_{p^n}$, on choisit un polynôme irréductible $P(X) \in \mathbb{F}_p[X]$ de degré $n$.

### Propriétés et Structure :
1. **Quotientation :** Le corps fini est obtenu par le quotient de l'anneau des polynômes par l'idéal maximal généré par $P(X)$ :
   $$\mathbb{F}_{p^n} \cong \mathbb{F}_p[X] / (P(X))$$

2. **Représentation des éléments :** Soit $\alpha$ une racine de $P(X)$ dans $\mathbb{F}_{p^n}$ (c'est-à-dire $P(\alpha) = 0$). Tout élément $A \in \mathbb{F}_{p^n}$ s'exprime de manière unique sous la forme :
   $$A(\alpha) = \sum_{i=0}^{n-1} a_i \alpha^i = a_{n-1}\alpha^{n-1} + \dots + a_1\alpha + a_0 \quad \text{avec } a_i \in \mathbb{F}_p$$

3. **Arithmétique :**
   - **Addition :** Somme terme à terme des coefficients modulo $p$.
   - **Multiplication :** Multiplication polynomiale classique suivie d'une réduction par le reste de la division euclidienne par $P(X)$.
