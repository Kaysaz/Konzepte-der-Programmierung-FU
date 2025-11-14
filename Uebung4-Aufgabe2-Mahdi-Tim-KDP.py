# Konzepte der Programmierung - Aufgabe 2, Woche 4
# Tim Schenk 5611815, Mahdi Bayanloo 5598602
# 14.11.2025
# Spezifikation nextEven(n):
# Eingabe:  n - eine ganze Zahl
# Ausgabe:  die kleinste gerade Zahl, die strikt größer ist als n
# Falls n gerade ist:   nextEven(n) = n + 2
# Falls n ungerade ist: nextEven(n) = n + 1


# Gegeben:

def nextEven(n:int) -> int:
    if n%2 == 0:
        return (n+2)
    else:
        return (n+1)


# Auszuwerten ist:

nextEven(3+4)



# a) Call-by-Value
# Argument wird zuerst ausgewertet, bevor die Funktion beginnt.

# 1. Ausdruck auswerten:

3 + 4 ⇒ 7

# 2. Funktionsaufruf:

nextEven(7)

# 3. Funktionskörper:
# Prüfe 7 % 2 == 0 -> false

return 7 + 1

# 4. Ergebnis

8


# b) Call-by-Name
# Der Ausdruck 3+4 wird nicht vorher ausgewertet, sondern als unevaluierter Ausdruck in die Funktion eingesetzt.

# 1. Argument wird substituiert (unbewertet):

nextEven(3+4)

# -> im Funktionskörper wird überall n durch (3+4) ersetzt:

if (3+4)%2 == 0:
    return (3+4)+2
else:
    return (3+4)+1

# 2. Bedingung auswerten

# (3+4) % 2
# -> zuerst 3+4 = 7
# -> 7 % 2 = 1

# Also Bedingung ist false.

# 3. else-Zweig

return (3+4) + 1

# Jetzt wird (3+4) erneut ausgewertet (call-by-name führt keine gemeinsame Auswertung durch):

(3+4) = 7
7 + 1 = 8

# Ergebnis:

8



