"""Calculs dans F_8 = F_2[X]/(X^3 + X + 1).

Un élément est un entier de 0 à 7 dont les bits sont les coefficients
(a2 a1 a0) du polynôme a2*α^2 + a1*α + a0.
"""

MODULUS = 0b1011  # X^3 + X + 1


def add(a, b):
    """Addition = XOR des bits (coefficients modulo 2)."""
    return a ^ b


def mul(a, b):
    """Produit de polynômes sur F_2, puis réduction modulo X^3 + X + 1."""
    result = 0
    for i in range(3):
        if (b >> i) & 1:
            result ^= a << i
    # réduction : on enlève X^4 puis X^3
    for deg in (4, 3):
        if (result >> deg) & 1:
            result ^= MODULUS << (deg - 3)
    return result


def power(a, n):
    result = 1
    for _ in range(n):
        result = mul(result, a)
    return result


def inverse(a):
    """Inverse : a^7 = 1, donc a^(-1) = a^6."""
    if a == 0:
        raise ZeroDivisionError("0 n'a pas d'inverse")
    return power(a, 6)


def to_poly(a):
    terms = []
    if a & 4:
        terms.append("α²")
    if a & 2:
        terms.append("α")
    if a & 1:
        terms.append("1")
    return " + ".join(terms) if terms else "0"


def print_table(op, symbol):
    print(f"Table de {symbol}")
    print("      " + " ".join(f"{b:>3}" for b in range(8)))
    for a in range(8):
        print(f"{a:>3} | " + " ".join(f"{op(a, b):>3}" for b in range(8)))
    print()


if __name__ == "__main__":
    alpha = 0b010
    print("Puissances de α :")
    for k in range(8):
        v = power(alpha, k)
        print(f"  α^{k} = {to_poly(v)}  (bits {v:03b})")
    print()
    print("Inverses :")
    for a in range(1, 8):
        print(f"  ({to_poly(a)})^-1 = {to_poly(inverse(a))}")
    print()
    print_table(add, "l'addition")
    print_table(mul, "la multiplication")

    # vérifications
    assert power(alpha, 3) == 0b011       # α^3 = α + 1
    assert power(alpha, 7) == 1           # α^7 = 1
    assert all(mul(a, inverse(a)) == 1 for a in range(1, 8))
    print("Toutes les vérifications sont correctes.")
