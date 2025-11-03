# Tic Tac Toe Spiel
# Aufgabe 1 Woche 3
# Tim Schenk
# 3.11.2025

def placeSign(spieler, spielfeld):
    """
    Platziert ein Zeichen des Spielers auf dem Spielfeld.
    Liest die Position vom Benutzer ein und behandelt Fehler.
    
    Args:
        spieler: Integer (1 oder 2) - Spieler 1 = 'x', Spieler 2 = 'o'
        spielfeld: 3x3 Liste - Das aktuelle Spielfeld
    
    Returns:
        spielfeld: Das aktualisierte Spielfeld
    """
    zeichen = 'x' if spieler == 1 else 'o'
    
    while True:
        try:
            position_input = input(f"Spieler {spieler} ({zeichen}): Geben Sie die Position ein (Zeile,Spalte): ")
            
            # Split the input and convert to integers
            position = tuple(map(int, position_input.split(',')))
            
            # Check if position is within bounds
            if len(position) != 2:
                print("Bitte geben Sie genau 2 Koordinaten ein!")
                continue
            
            zeile, spalte = position
            
            if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
                print("Position außerhalb des Spielfelds! Bitte Werte zwischen 0 und 2 eingeben.")
                continue
            
            # Check if position is already occupied
            if spielfeld[zeile][spalte] is not None:
                print("Diese Position ist bereits besetzt! Bitte wählen Sie eine andere.")
                continue
            
            # Place the sign
            spielfeld[zeile][spalte] = zeichen
            break
            
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie zwei Zahlen getrennt durch Komma ein (z.B. 1,2)")
        except KeyboardInterrupt:
            print("\nSpiel abgebrochen.")
            exit()
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            continue
    
    return spielfeld


def buildLine(reihe):
    """
    Erstellt einen String aus einer Zeile des Spielfelds.
    Zeichen werden durch | getrennt, None wird als Leerzeichen dargestellt.
    
    Args:
        reihe: Liste mit 3 Elementen (None, 'x' oder 'o')
    
    Returns:
        String: Die formatierte Zeile
    """
    result = ""
    for i, element in enumerate(reihe):
        if element is None:
            result += " "
        else:
            result += str(element)
        if i < len(reihe) - 1:
            result += "|"
    return result


def printBoard(spielfeld):
    """
    Gibt das Spielfeld auf der Konsole aus.
    
    Args:
        spielfeld: 3x3 Liste - Das Spielfeld
    """
    for i, reihe in enumerate(spielfeld):
        print(buildLine(reihe))
    print()  # Leerzeile nach dem Spielfeld


def checkWin(spielfeld):
    """
    Prüft, ob ein Spieler gewonnen hat.
    
    Args:
        spielfeld: 3x3 Liste - Das Spielfeld
    
    Returns:
        Tupel: (True, 'x'/'o') wenn gewonnen, sonst (False, None)
    """
    # Prüfe Reihen
    for reihe in spielfeld:
        if reihe[0] is not None and reihe[0] == reihe[1] == reihe[2]:
            return (True, reihe[0])
    
    # Prüfe Spalten
    for spalte in range(3):
        if spielfeld[0][spalte] is not None and \
           spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte]:
            return (True, spielfeld[0][spalte])
    
    # Prüfe Diagonale von links oben nach rechts unten
    if spielfeld[0][0] is not None and \
       spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2]:
        return (True, spielfeld[0][0])
    
    # Prüfe Diagonale von rechts oben nach links unten
    if spielfeld[0][2] is not None and \
       spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0]:
        return (True, spielfeld[0][2])
    
    return (False, None)


def ticTacToe():
    """
    Hauptfunktion für das Tic Tac Toe Spiel.
    Lässt zwei Spieler abwechselnd spielen bis jemand gewinnt oder Unentschieden.
    """
    # Initialisiere Spielfeld
    spielfeld = [3 * [None] for i in range(3)]
    
    # Spieler 1 beginnt
    aktueller_spieler = 1
    zuege = 0
    
    print("=== Tic Tac Toe ===\n")
    print("Geben Sie die Position als Zeile,Spalte ein (z.B. 1,2)")
    print("Koordinaten von 0 bis 2\n")
    
    # Spiele bis jemand gewinnt oder Unentschieden
    while True:
        # Zeige aktuelles Spielfeld
        printBoard(spielfeld)
        
        # Spieler macht Zug
        spielfeld = placeSign(aktueller_spieler, spielfeld)
        zuege += 1
        
        # Prüfe auf Gewinn
        gewonnen, gewinner = checkWin(spielfeld)
        
        if gewonnen:
            printBoard(spielfeld)
            spieler_nummer = 1 if gewinner == 'x' else 2
            print(f"Spieler {spieler_nummer} ({gewinner}) hat gewonnen! 🎉")
            break
        
        # Prüfe auf Unentschieden (alle 9 Felder belegt)
        if zuege >= 9:
            printBoard(spielfeld)
            print("Unentschieden! Das Spielfeld ist voll.")
            break
        
        # Wechsle Spieler
        aktueller_spieler = 1 if aktueller_spieler == 2 else 2


if __name__ == "__main__":
    ticTacToe()
