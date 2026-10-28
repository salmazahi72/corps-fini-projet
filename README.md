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

##  Utilisation du Code
```bash
python code/gf8.py                                                 
---

### 2. Compléter le fichier `code/gf8.py`
Assure-toi que ton fichier `gf8.py` contient une implémentation claire de l'arithmétique dans $\mathrm{GF}(2^8)$ pour l'AES.

```python
# GF(2^8) avec le polynôme irréductible de Rijndael : X^8 + X^4 + X^3 + X + 1 (0x11B)

P_RIJNDAEL = 0x11B

def add_gf28(a, b):
    """Addition dans GF(2^8) (XOR bit à bit)."""
    return a ^ b

def xtime(a):
    """Multiplication par X (0x02) avec réduction modulo P(X)."""
    if a & 0x80:
        return ((a << 1) ^ P_RIJNDAEL) & 0xFF
    else:
        return (a << 1) & 0xFF

def multiply_gf28(a, b):
    """Multiplication polynomiale dans GF(2^8)."""
    result = 0
    for i in range(8):
        if (b >> i) & 1:
            temp = a
            for _ in range(i):
                temp = xtime(temp)
            result ^= temp
    return result

if __name__ == "__main__":
    a = 0x57  # Exemple AES
    b = 0x83
    print(f"Addition : {hex(a)} + {hex(b)} = {hex(add_gf28(a, b))}")
    print(f"Multiplication : {hex(a)} * {hex(b)} = {hex(multiply_gf28(a, b))}")
