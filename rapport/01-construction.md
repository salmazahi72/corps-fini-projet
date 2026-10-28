## 2. Le corps $\mathbb{F}_4$

On prend $P(X) = X^2 + X + 1$ (irréductible sur $\mathbb{F}_2$). On note $\alpha$ la classe de $X$, avec la règle $\alpha^2 = \alpha + 1$. 

Les 4 éléments de $\mathbb{F}_4$ sont : $\{0, 1, \alpha, \alpha + 1\}$.

### Table d'addition de $\mathbb{F}_4$
En caractéristique 2, l'addition correspond à un XOR bit à bit ($1 + 1 = 0$, $\alpha + \alpha = 0$).

| $+$ | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0$** | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| **$1$** | $1$ | $0$ | $\alpha+1$ | $\alpha$ |
| **$\alpha$** | $\alpha$ | $\alpha+1$ | $0$ | $1$ |
| **$\alpha+1$** | $\alpha+1$ | $\alpha$ | $1$ | $0$ |

### Table de multiplication de $\mathbb{F}_4$
Rappel : $\alpha^2 = \alpha + 1$ et $\alpha \cdot (\alpha + 1) = \alpha^2 + \alpha = (\alpha + 1) + \alpha = 1$.

| $\times$ | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0$** | $0$ | $0$ | $0$ | $0$ |
| **$1$** | $0$ | $1$ | $\alpha$ | $\alpha+1$ |
| **$\alpha$** | $0$ | $\alpha$ | $\alpha+1$ | $1$ |
| **$\alpha+1$** | $0$ | $\alpha+1$ | $1$ | $\alpha$ |
