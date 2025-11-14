# Konzepte der Programmierung - Aufgabe 1, Woche 4
# Tim Schenk 5611815, Mahdi Bayanloo 5598602
# 14.11.2025


# Definition 1 a)
def askFor(a:str) -> str:
    global z
    global y
    if a == "Passierschein A39":
        z = "Passierschein A38"
        y = "Präfekt"
    elif a == "Rundschreiben B56":
        x = "Niemand"
        z = "alles"
    else:
        z = "dem hellbraunen Formular"
    print("Sie gehen zu Schalter 56.")

# Definition 2 b)
def askFor(a:str) -> str:
    global x
    global y
    if a == "Passierschein A39":
        z = "Passierschein A38"
        y = "Präfekt"
    elif a == "Rundschreiben B56":
        x = "Niemand"
        z = "alles"
    else:
        z = "dem hellbraunen Formular"
        print("Sie gehen zu Schalter 56.")

# Des Weiteren ist die Funktion getWhatVarWants(<string>) gegeben:
def getWhatVarWants(x:str) -> str:
    z = "Rundschreiben B56"
    if x == "dem hellbraunen Formular":
        z = "Passierschein A39"
        print("Sie suchen ",z)
    askFor(z)

# Nun soll der folgende Code mit den zuvor gegebenen Funktionen ausgeführt werden:
x = "Asterix"
y = "Obelix"
z = "Formular A38"
print(x," & ",y,"suchen ",z,".")
askFor(z)
print("Sie fragen nach ",z,".")
getWhatVarWants(z)
print(x," erhält ",z,".")
print(y," verliert und wird verrückt.")



# a) Definition #1:

# Ergebnis - Ausgabe:

# Asterix  &  Obelix suchen  Formular A38 .
# Sie gehen zu Schalter 56.
# Sie fragen nach  dem hellbraunen Formular .
# Sie suchen  Passierschein A39
# Sie gehen zu Schalter 56.
# Asterix  erhält  Passierschein A38 .
# Präfekt  verliert und wird verrückt.


# Begründung (Gültigkeitsbereiche / Zuweisungen):

# Weil askFor in Definition 1 z und y als global deklariert, verändern Zuweisungen an z bzw. y in askFor die globalen Variablen. Deshalb wird z zuerst auf "dem hellbraunen Formular" gesetzt (beim ersten askFor), später auf "Passierschein A38" (durch den zweiten askFor), und y wird bei letzterem Aufruf auf "Präfekt" geändert. Lokale Zuweisungen (z. B. innerhalb von getWhatVarWants oder nicht-global deklarierten Variablen) beeinflussen die globalen Variablen nicht.



# b) Definition #2:

# Ausgabe für b):

# Asterix  &  Obelix suchen  Formular A38 .
# Sie gehen zu Schalter 56.
# Sie fragen nach  Formular A38 .
# Sie suchen  Rundschreiben B56
# Niemand  erhält  Formular A38 .
# Obelix  verliert und wird verrückt.
# Asterix  &  Obelix suchen  Formular A38 .
# Sie gehen zu Schalter 56.
# Sie fragen nach  Formular A38 .
# Sie suchen  Rundschreiben B56
# Niemand  erhält  Formular A38 .
# Obelix  verliert und wird verrückt.


# Begründung (Gültigkeitsbereiche / Zuweisungen):

# Durch die global x-Deklaration in Definition 2 wird x beim zweiten askFor global auf "Niemand" gesetzt. Weil z in askFor nicht global ist, führen alle Zuweisungen an z in askFor nur zu lokalen Änderungen — die globale z bleibt therefore "Formular A38". Der print in deiner Version steht nur im else, deshalb wird beim zweiten askFor (elif-Zweig) nichts gedruckt.