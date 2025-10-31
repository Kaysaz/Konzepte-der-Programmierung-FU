# Galgenmännchen (Hangman) für zwei Spieler:innen
# Anforderungen:
# 1) Namen per input()
# 2) Spieler:in 1 gibt ein Wort ein (nur Buchstaben erlaubt, überprüft mit isalpha())
# 3) Spieler:in 2 rät Buchstaben (Info zur Länge des Wortes)
# 4) Hinweise: Positionen / optische Ausgabe; Behandlung bei Nicht-Vorkommen
# 5) Maximal 10 falsche Buchstaben -> Verlust
#
# Hinweis: Das Geheimwort wird via getpass versteckt (falls verfügbar).
# Falls getpass nicht verfügbar (z. B. manche IDEs), wird die Eingabe normal angezeigt.

import getpass

GALGEN = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
r"""
  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========""",
r"""
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========""",
r"""
  +---+
  |   |
_[O]_ |
 /|\  |
 / \  |
      |
=========""",
r"""
  +---+
  |   |
_[X]_ |
 /|\  |
 / \  |
      |
========="""
]

MAX_WRONG = 10

def eingabe_geheimwort(prompt="Spieler:in 1, gib das Geheimwort ein (nur Buchstaben): "):
    while True:
        try:
            word = getpass.getpass(prompt)
        except Exception:
            # Fallback, falls getpass nicht funktioniert (z. B. manche Online-IDE)
            word = input(prompt)
        word = word.strip()
        if len(word) == 0:
            print("Das Wort darf nicht leer sein. Bitte erneut eingeben.")
            continue
        if not word.isalpha():
            print("Nur Buchstaben sind erlaubt. Keine Leerzeichen, Zahlen oder Sonderzeichen.")
            continue
        return word.lower()

def zeige_maskiertes(wort, geratene_buchstaben):
    # zeigt das Wort mit Unterstrichen für nicht-geratene Buchstaben
    return " ".join([ch if ch in geratene_buchstaben else "_" for ch in wort])

def positionen_anzeigen(wort, buchst):
    # gibt 1-basierte Positionen des Buchstabens im Wort zurück
    pos = [i+1 for i, ch in enumerate(wort) if ch == buchst]
    return pos

def spiel_starten():
    print("Willkommen zum Galgenmännchen — zwei Spieler:innen")
    p1 = input("Name Spieler:in 1 (der das Wort wählt): ").strip() or "Spieler1"
    p2 = input("Name Spieler:in 2 (der rät): ").strip() or "Spieler2"
    print(f"\nHallo {p1} und {p2}!\n")
    geheimwort = eingabe_geheimwort(f"{p1}, gib bitte das Geheimwort ein (wird versteckt): ")
    wort_laenge = len(geheimwort)
    print("\n" * 40)  # Bildschirm etwas "reinigen", damit das Wort nicht sichtbar bleibt
    
    print(f"{p2}, das Geheimwort hat {wort_laenge} Buchstaben.")
    geratene_buchstaben = set()
    falsche_buchstaben = []
    runde = 0
    
    while True:
        print("\n" + "="*40)
        # Zeichne Galgen entsprechend der Anzahl falscher Versuche
        falsch = len(falsche_buchstaben)
        index = min(falsch, MAX_WRONG)
        print(GALGEN[index])
        print(f"Falsche Versuche: {falsch}/{MAX_WRONG}  ->  {', '.join(falsche_buchstaben) if falsche_buchstaben else '(keine)'}")
        print("Wort: ", zeige_maskiertes(geheimwort, geratene_buchstaben))
        print("="*40)
        
        if "_" not in zeige_maskiertes(geheimwort, geratene_buchstaben):
            print(f"\nHerzlichen Glückwunsch {p2}! Du hast das Wort '{geheimwort}' erraten!")
            break
        if len(falsche_buchstaben) >= MAX_WRONG:
            print(f"\n{p2} hat verloren. Das Wort war: '{geheimwort}'")
            break
        
        # Eingabe von Spieler:in 2
        guess = input(f"{p2}, gib einen Buchstaben oder den ganzen Versuch ein: ").strip().lower()
        if not guess:
            print("Leere Eingabe — bitte Buchstaben oder Wort eingeben.")
            continue
        if guess.isalpha():
            if len(guess) == 1:
                buch = guess
                if buch in geratene_buchstaben or buch in falsche_buchstaben:
                    print(f"'{buch}' wurde bereits geraten.")
                    continue
                if buch in geheimwort:
                    geratene_buchstaben.add(buch)
                    pos = positionen_anzeigen(geheimwort, buch)
                    pos_text = ", ".join(str(p) for p in pos)
                    print(f"Gut! Der Buchstabe '{buch}' kommt im Wort vor an Position(en): {pos_text}.")
                    print("Aktueller Stand:", zeige_maskiertes(geheimwort, geratene_buchstaben))
                else:
                    falsche_buchstaben.append(buch)
                    print(f"Der Buchstabe '{buch}' kommt nicht im Wort vor.")
                    # Optional: zusätzliche kreative Nachricht je nach Anzahl falscher Versuche
                    verbleibend = MAX_WRONG - len(falsche_buchstaben)
                    if verbleibend > 0:
                        print(f"Noch {verbleibend} Fehlversuche möglich.")
            else:
                # Spieler:in 2 versucht das ganze Wort
                if guess == geheimwort:
                    print(f"\nFantastisch {p2}! Du hast das Wort korrekt erraten: '{geheimwort}'")
                    break
                else:
                    # ganzer Wort-Versuch falsch -> zählt als 2 Fehlversuche (optional)
                    # Hier zählen wir ihn als 1 Fehlversuch:
                    falsche_buchstaben.append(f"[Wort:{guess}]")
                    print(f"Das war nicht korrekt.")
                    verbleibend = MAX_WRONG - len(falsche_buchstaben)
                    if verbleibend > 0:
                        print(f"Noch {verbleibend} Fehlversuche möglich.")
        else:
            print("Ungültige Eingabe. Bitte nur Buchstaben (a-z).")
            continue

if __name__ == "__main__":
    spiel_starten()
