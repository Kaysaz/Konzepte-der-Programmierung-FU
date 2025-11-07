# Konzepte der Programmierung - Aufgabe 2 Woche 3
# Tim Schenk, Mahdi Bayahloo
# 3.11.2025



# (a) Funktion qSumme(<zahl>)
#    Berechnet die Quersumme einer eingegebenen Zahl
#    ohne sie in String oder Liste zu konvertieren.

def qSumme(zahl: int) -> int:
    """Berechnet die Quersumme einer (positiven oder negativen) Zahl."""
    zahl = abs(zahl)
    s = 0
    while zahl:
        s += zahl % 10     # letzter Ziffer hinzufügen
        zahl //= 10        # letzte Ziffer entfernen
    return s



# (b) Caesar-Verschlüsselung
#     (i) encrypt(n, <text>)  → verschlüsselt Text mit Schlüssel n
#     (ii) decrypt(n, <text>) → entschlüsselt Text mit Schlüssel n

def encrypt(n: int, text: str) -> str:
    """
    (b)(i) Verschlüsselt den gegebenen Text mit einer Caesar-Verschiebung.
    - Nur Buchstaben (A–Z, a–z) werden verschoben.
    - Andere Zeichen (Zahlen, Sonderzeichen, Leerzeichen) bleiben gleich.
    """
    n = n % 26  # Schlüssel auf 0–25 begrenzen
    out = []
    for ch in text:
        o = ord(ch)
        if ord('A') <= o <= ord('Z'):              # Großbuchstaben
            base = ord('A')
            out.append(chr((o - base + n) % 26 + base))
        elif ord('a') <= o <= ord('z'):            # Kleinbuchstaben
            base = ord('a')
            out.append(chr((o - base + n) % 26 + base))
        else:                                      # Sonderzeichen, Zahlen, etc.
            out.append(ch)
    return ''.join(out)


def decrypt(n: int, text: str) -> str:
    """
    (b)(ii) Entschlüsselt den mit Caesar verschlüsselten Text.
    - Entschlüsselung = Verschiebung um -n.
    """
    return encrypt(-n, text)



# (c) dictEncrypt(<wörterbuch>, <text>)
#     Verschlüsselt Text anhand eines gegebenen Wörterbuchs.

def dictEncrypt(wb: dict, text: str) -> str:
    """
    (c) Ersetzt Zeichen im Text gemäß Wörterbuch wb.
    Falls ein Zeichen nicht im Wörterbuch enthalten ist,
    bleibt es unverändert.
    """
    out = []
    for ch in text:
        out.append(wb.get(ch, ch))  # get() gibt ch zurück, falls Key fehlt
    return ''.join(out)



# (d) decryptDict(<wörterbuch>)
#     Erstellt das inverse Wörterbuch zur Entschlüsselung.

def decryptDict(wb: dict) -> dict:
    """
    (d) Gibt ein Wörterbuch zurück, das die Verschlüsselung umkehrt.
    Überprüft, ob das Wörterbuch injektiv ist (eindeutige Zuordnung).
    """
    values = list(wb.values())
    if len(set(values)) != len(values):
        raise ValueError("Das Wörterbuch ist nicht injektiv; Entschlüsselung nicht eindeutig möglich.")
    return {v: k for k, v in wb.items()}



# (e) Eindeutigkeits-Kriterium

# (e) Eine Verschlüsselung ist eindeutig, wenn die Abbildung eine Bijektion ist:
#     Jedes Klarzeichen wird genau einem Geheimzeichen zugeordnet – und umgekehrt.



# Tests zu allen Teilaufgaben

print("=== (a) qSumme ===")
print("qSumme(0) =", qSumme(0))
print("qSumme(12345) =", qSumme(12345))
print("qSumme(-709) =", qSumme(-709))

print("\n=== (b) Caesar-Verschlüsselung ===")
example = "Alea iacta est."
enc = encrypt(8, example)
dec = decrypt(8, enc)
print("encrypt(8, 'Alea iacta est.') ->", enc)
print("decrypt(8, enc) ->", dec)
print("encrypt(3, 'XYZ xyz 123!') ->", encrypt(3, "XYZ xyz 123!"))
print("decrypt(3, encrypt(3, 'Hello, World!')) ->", decrypt(3, encrypt(3, "Hello, World!")))

print("\n=== (c) dictEncrypt & (d) decryptDict ===")
sample_wb = {'A':'m', 'B':'N', 'a':'x', '1':'9', ' ':'_'}
text = "A B a1 !"
enc_text = dictEncrypt(sample_wb, text)
print("Wörterbuch:", sample_wb)
print("Originaltext:", text)
print("dictEncrypt ->", enc_text)
inv = decryptDict(sample_wb)
print("decryptDict ->", inv)
print("Rückentschlüsselung ->", dictEncrypt(inv, enc_text))

print("\n=== Fehlerfall für (d) ===")
bad_wb = {'A':'x', 'B':'x'}
try:
    decryptDict(bad_wb)
except ValueError as e:
    print("Fehler erkannt:", e)

print("\n=== (e) Kriterium ===")
print("Eine Verschlüsselung ist eindeutig, wenn die Abbildung eine Bijektion ist –",
      "jedes Klarzeichen wird genau einem Geheimzeichen zugeordnet und umgekehrt.")
