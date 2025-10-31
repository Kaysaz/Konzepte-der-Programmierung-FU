# Einfaches Drachenhöhlen-Textadventure

# System falls ein falscher Anwort gegeben wurde
def get_choice(prompt, valid):
    """Fragt so lange, bis eine gültige Zahl eingegeben wurde."""
    while True:
        try:
            w = int(input(prompt))
            if w in valid:
                return w
            print(f"Gültige Optionen: 1,2,3,4")
        except ValueError:
            print("Bitte eine Zahl eingeben.")

# Willkommenstext
print("Willkommen im Spiel 'Drachenhöhle'!")
print("Treffe kluge Entscheidungen. Vier richtige hintereinander führen zum Happy End.")
print("Andere Entscheidungen können das Spiel früh beenden.\n")

# Name abfragen
name = input("Wie heißt du, Abenteurer/in? ")

# Erste Entscheidung
print(f"\n{name}, du stehst vor der Höhle. Was tust du?")
print("1 - Laut reinrennen")
print("2 - Leise schleichen")
print("3 - Picknick aufbauen")
print("4 - Umkehren")
w1 = get_choice("Deine Wahl (1-4): ", {1,2,3,4})

if w1 == 1:
    print("\nDu rennst hinein und weckst den Drachen. Du wirst verbrannt. Ende.")
    exit()
if w1 == 3:
    print("\nDas Picknick lockt wilde Tiere an — und den Drachen. Du wirst gefressen. Ende.")
    exit()
if w1 == 4:
    print("\nDu gehst nach Hause. Das Dorf wird später angegriffen. Du warst nicht bereit. Ende.")
    exit()

# Nur weiter, wenn w1 == 2 (leise schleichen)
print("\nGut gemacht. Du schleichst hinein und findest zwei Gänge.")
print("1 - Rechter, breiter Gang (man hört Ketten)")
print("2 - Linker, enger Gang (ruhig, riecht nach alten Kammern)")
print("3 - Laut rufen")
w2 = get_choice("Deine Wahl (1-3): ", {1,2,3})

if w2 == 1:
    print("\nEine Falle löst sich im breiten Gang. Du wirst verschüttet. Ende.")
    exit()
if w2 == 3:
    print("\nDu rufst laut. Der Drache erwacht wütend. Ende.")
    exit()

# Nur weiter, wenn w2 == 2 (linker, enger Gang)
print("\nDer linke Gang führt dich zur Schatzkammer: der Drache schläft.")
print("1 - Den Schatz stehlen")
print("2 - Ein altes Schwert als Geschenk legen (Respekt zeigen)")
print("3 - Den Drachen wecken und herausfordern")
w3 = get_choice("Deine Wahl (1-3): ", {1,2,3})

if w3 == 1:
    print("\nBeim Stehlen machst du Lärm. Der Drache erwacht und jagt dich. Ende.")
    exit()
if w3 == 3:
    print("\nDer Drache erwacht und akzeptiert den Kampf. Du verlierst. Ende.")
    exit()

# Nur weiter, wenn w3 == 2 (Respekt zeigen) -> das ist die dritte korrekte Entscheidung
print(f"\nDer Drache öffnet ein Auge, {name}. Er sieht dein Geschenk.")
print("1 - Verbeugen und Bündnis anbieten")
print("2 - Das Schwert packen und wegrennen")
w4 = get_choice("Deine Wahl (1-2): ", {1,2})

if w4 == 2:
    print("\nDu versuchst zu stehlen. Der Drache ist beleidigt und greift an. Ende.")
    exit()

# w4 == 1 -> Happy End
print(f"""
{name}, du überzeugst den Drachen.
Anstatt dich zu fressen, bietet er dir Frieden an: ein Bündnis, Schutz fürs Dorf
und einen kleinen Anteil am Schatz.
Herzlichen Glückwunsch. Happy End!
""")
