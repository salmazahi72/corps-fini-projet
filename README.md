# Construction, Représentation et Calculs dans les Corps Finis

**Master :** Cryptologie et Sécurité de l'Information  
**Module :** Anneaux et Corps Finis  
**Auteurs :** Salma Zahi & Hiba Boulaachour  

---

## Description du Projet
Ce projet étudie la construction théorique des corps finis ($\mathbb{F}_q$), leurs différentes représentations informatiques (Polynomiale, Normale, Zech, Matricielle) ainsi que l'efficacité des algorithmes d'opérations arithmétiques associées. Une étude comparative et une application concrète sur le corps $\mathrm{GF}(2^8)$ (AES) sont également présentées.

##  Structure du Dépôt
- `rapport/` : Documentation et notes théoriques.
  - `01-construction.md` : Fondements algébriques et construction par quotientation.
- `code/` : Implémentation des opérations dans les corps finis.
  - `gf8.py` : Script Python illustrant l'arithmétique dans $\mathrm{GF}(2^8)$.
- `README.md` : Présentation générale du projet.

## 🚀 Utilisation du Code
```bash
python code/gf8.py
