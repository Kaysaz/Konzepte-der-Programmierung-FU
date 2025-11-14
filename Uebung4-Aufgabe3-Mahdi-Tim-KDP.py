# Konzepte der Programmierung - Aufgabe 3, Woche 4
# Tim Schenk 5611815, Mahdi Bayanloo 5598602
# 14.11.2025


# a) multiplyAllBy(xs, n)

# def multiplyAllBy(xs: list[int], n: int) -> list[int]:

# Eingabe: xs - Liste ganzer Zahlen, n - ganze Zahl
# Ausgabe: Liste der gleichen Länge wie xs, wobei jedes Element xi durch xi * n ersetzt ist.
# Beispiel: multiplyAllBy([1,4,3], 4) -> [4,16,12]
# Vorbedingung: xs ist eine Python-Liste (kann leer sein).
# Nachbedingung: Rückgabe[i] == xs[i] * n für alle gültigen Indices i.

# Implementierungen:

from typing import List

# 1) while-Schleife
def multiplyAllBy_while(xs: List[int], n: int) -> List[int]:
    res: List[int] = []
    i = 0
    while i < len(xs):
        res.append(xs[i] * n)
        i += 1
    return res

# 2) for-Schleife
def multiplyAllBy_for(xs: List[int], n: int) -> List[int]:
    res: List[int] = []
    for x in xs:
        res.append(x * n)
    return res

# 3) Rekursion
def multiplyAllBy_rec(xs: List[int], n: int) -> List[int]:
    # Basisfall: leere Liste
    if not xs:
        return []
    # rekursiver Fall: erstes Element verarbeiten + Rest rekursiv
    first = xs[0] * n
    return [first] + multiplyAllBy_rec(xs[1:], n)


# b) lovedDigits(n)

# def lovedDigits(n: int) -> int:

# Eingabe: n - nicht-negative ganze Dezimalzahl (n >= 0)
# Ausgabe: eine ganze Dezimalzahl, die entsteht, wenn jede Ziffer d von n durch love(d) ersetzt wird, mit love(0)=0 und love(d)=10-d für d>0.
# Beispiel: lovedDigits(165702) -> 945308
# Vorbedingung: n ist eine nicht-negative ganze Zahl.
# Nachbedingung: Die Rückgabe hat die gleiche Anzahl an Dezimalstellen wie n (außer spezielles Verhalten bei führenden Nullen; n hat keine führenden Nullen).

# Verwendet wird de arithmetische Definition:

# def love_digit(d: int) -> int:
#    """Verliebte Ziffer: love(0)=0, sonst 10-d. Vorbedingung: 0 <= d <= 9"""
#    return 0 if d == 0 else 10 - d

# Implementierung:

# 1) while-Schleife
def lovedDigits_while(n: int) -> int:
    if n == 0:
        return 0
    # bestimme die größte Zehnerpotenz p mit p <= n (z.B. n=165 -> p=100)
    p = 1
    temp = n
    while temp >= 10:
        temp //= 10
        p *= 10
    result = 0
    remaining = n
    while p > 0:
        digit = remaining // p            # aktuelle führende Ziffer
        mapped = 0 if digit == 0 else 10 - digit
        result = result * 10 + mapped
        remaining = remaining % p
        p //= 10
    return result


# 2) for-Schleife
def lovedDigits_for(n: int) -> int:
    if n == 0:
        return 0
    # Anzahl der Ziffern bestimmen (k)
    temp = n
    k = 0
    while temp > 0:
        temp //= 10
        k += 1
    # Startzehnerpotenz
    p = 10 ** (k - 1)
    result = 0
    remaining = n
    # for i in range(k): bearbeite von höchster zur niedrigsten Stelle
    for _ in range(k):
        digit = remaining // p
        mapped = 0 if digit == 0 else 10 - digit
        result = result * 10 + mapped
        remaining %= p
        p //= 10
    return result


# 3) Rekursion
def lovedDigits_rec(n: int) -> int:
    if n == 0:
        return 0
    # Hilfsfunktion: berechne größte Zehnerpotenz p <= n
    def highest_pow10(x: int) -> int:
        p = 1
        while x >= 10:
            x //= 10
            p *= 10
        return p

    def helper(remaining: int, p: int) -> int:
        # p ist die aktuelle Zehnerpotenz (z.B. 100 für die Hunderterstelle)
        if p == 0:
            return 0  # sollte nicht normalerweise auftreten, Schutz
        digit = remaining // p
        mapped = 0 if digit == 0 else 10 - digit
        rest = remaining % p
        if p == 1:
            return mapped
        # restliche Stellen rekursiv bearbeiten
        return mapped * (10 ** (len_digits(p) - 1)) + helper(rest, p // 10)

    # Hilfsfunktion um zu ermitteln wie viele Stellen eine Potenz p hat (p ist 10^m)
    def len_digits(p: int) -> int:
        # p = 10^m -> len = m+1
        cnt = 0
        while p > 0:
            p //= 10
            cnt += 1
        return cnt

    p0 = highest_pow10(n)
    return helper(n, p0)


# Tests (Nachweise):

# multiplyAllBy
assert multiplyAllBy_while([1,4,3], 4) == [4,16,12]   # -> True
assert multiplyAllBy_for([1,4,3], 4) == [4,16,12]     # -> True
assert multiplyAllBy_rec([1,4,3], 4) == [4,16,12]     # -> True

# lovedDigits (Beispiel aus Aufgabenstellung)
n = 165702
assert lovedDigits_while(n) == 945308   # -> True
assert lovedDigits_for(n) == 945308     # -> True
assert lovedDigits_rec(n) == 945308     # -> True

# Randfälle
assert lovedDigits_while(0) == 0        # -> True
assert lovedDigits_for(0) == 0          # -> True
assert lovedDigits_rec(0) == 0          # -> True

# Wenn alle Assertions True sind, gibt es KEINE Ausgabe. 
# Das bedeutet: alle Tests wurden erfolgreich bestanden.



