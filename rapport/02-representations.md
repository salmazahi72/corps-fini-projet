# Représentations des Éléments d'un Corps Fini

Pour implémenter les corps finis sur un ordinateur ou un circuit électronique, plusieurs représentations des éléments sont possibles. Le choix de la représentation impacte directement l'efficacité des calculs.

---

## 1. Représentation en Base Polynomiale (Standard)

- **Définition :** Soit $\alpha$ une racine du polynôme irréductible $P(X) \in \mathbb{F}_p[X]$ de degré $n$. Tout élément $A \in \mathbb{F}_{p^n}$ s'exprime dans la base $\mathcal{B}_P = \{1, \alpha, \alpha^2, \dots, \alpha^{n-1}\}$.
- **Expression :** $A(\alpha) = \sum_{i=0}^{n-1} a_i \alpha^i$ avec $a_i \in \mathbb{F}_p$.
- **Stockage :** Un vecteur de coefficients $(a_0, a_1, \dots, a_{n-1}) \in \mathbb{F}_p^n$.
- **Avantage :** Très intuitive, idéale pour l'implémentation logicielle (sur CPU généraliste).
- **Inconvénient :** La multiplication nécessite une étape de réduction polynomiale modulo $P(X)$.

---

## 2. Représentation en Base Normale

- **Définition :** Il existe un élément $\beta \in \mathbb{F}_{p^n}$ tel que $\mathcal{B}_N = \{\beta, \beta^p, \beta^{p^2}, \dots, \beta^{p^{n-1}}\}$ forme une base de $\mathbb{F}_{p^n}$ sur $\mathbb{F}_p$.
- **Expression :** $A = \sum_{i=0}^{n-1} b_i \beta^{p^i}$ avec $b_i \in \mathbb{F}_p$.
- **Propriété clé (Caractéristique 2) :** L'élévation au carré $A^2$ dans $\mathbb{F}_{2^n}$ correspond à un simple **décalage circulaire des bits** (*cyclic shift*).
- **Avantage :** Calcul des carrés et élévation à la puissance extrêmement rapides.
- **Domaine d'élection :** Circuits matériels dédiés (FPGA / ASIC).

---

## 3. Représentation Logarithmique (Logarithmes de Zech)

- **Définition :** Soit $g$ un générateur du groupe cyclique $\mathbb{F}_q^*$. Tout élément non nul s'écrit sous la forme $g^k$ avec $k \in \{0, 1, \dots, q-2\}$.
- **Arithmétique :**
  - **Multiplication :** $g^a \cdot g^b = g^{(a+b) \pmod{q-1}}$ (simple addition des exposants).
  - **Division :** $g^a / g^b = g^{(a-b) \pmod{q-1}}$.
  - **Addition :** $g^a + g^b = g^a (1 + g^{b-a}) = g^{a + Z(b-a)}$ via une table de correspondance $Z(k) = \log_g(1 + g^k)$.
- **Avantage :** Multiplication et division immédiates.
- **Inconvénient :** Inexploitable pour les grands corps cryptographiques en raison de la taille de la table $Z(k)$.
