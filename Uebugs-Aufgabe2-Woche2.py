# Importiere die Rezeptliste
from rezeptListe import rezepte

# a) Alle Rezepte mit Stichwort "fingerfood" herausfiltern
print("Teil (a): Rezepte mit 'fingerfood' filtern")
fingerfood_rezepte = []
i = 0
while i < len(rezepte):
    if rezepte[i][0] == "fingerfood":
        fingerfood_rezepte.append(rezepte[i])
    i += 1

print(f"Gefundene fingerfood-Rezepte: {len(fingerfood_rezepte)}")
print()

# b) Liste aller benötigten Zutaten erstellen (ohne Mengen)
print("Teil (b): Liste aller benötigten Zutaten erstellen")
alle_zutaten = []

# Durch alle fingerfood-Rezepte iterieren
i = 0
while i < len(fingerfood_rezepte):
    zutaten_liste = fingerfood_rezepte[i][1]
    j = 0
    while j < len(zutaten_liste):
        zutat = zutaten_liste[j][1]
        # Prüfen, ob Zutat bereits in der Liste ist
        if zutat not in alle_zutaten:
            alle_zutaten.append(zutat)
        j += 1
    i += 1

print(f"Alle benötigten Zutaten: {alle_zutaten}")
print()

# c) Einkaufsliste mit aufsummierten Mengen erstellen
print("Teil (c): Einkaufsliste mit aufsummierten Mengen erstellen")

# Zuerst eine Einkaufsliste mit Menge 0 für jede Zutat initialisieren
einkaufsliste_roh = []
i = 0
while i < len(alle_zutaten):
    einkaufsliste_roh.append([alle_zutaten[i], 0])
    i += 1

# Durch alle fingerfood-Rezepte iterieren und Mengen addieren
i = 0
while i < len(fingerfood_rezepte):
    zutaten_liste = fingerfood_rezepte[i][1]
    j = 0
    while j < len(zutaten_liste):
        menge = zutaten_liste[j][0]
        zutat = zutaten_liste[j][1]
        # Finde den Index der Zutat in der Einkaufsliste
        k = 0
        while k < len(einkaufsliste_roh):
            if einkaufsliste_roh[k][0] == zutat:
                einkaufsliste_roh[k][1] += menge
                break
            k += 1
        j += 1
    i += 1

# Liste von Listen in Liste von Tupeln konvertieren
einkaufsliste = []
i = 0
while i < len(einkaufsliste_roh):
    einkaufsliste.append((einkaufsliste_roh[i][1], einkaufsliste_roh[i][0]))
    i += 1

print("Einkaufsliste:")
for eintrag in einkaufsliste:
    print(f"  {eintrag[0]}: {eintrag[1]}")

