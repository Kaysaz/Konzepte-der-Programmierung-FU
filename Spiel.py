# Integers

def get_choice(prompt, valid):
    """Fragt so lange, bis eine gültige Zahl eingegeben wurde."""
    while True:
        try:
            e = int(input(prompt))
            if e in valid:
                return e
            print(f"Gültige Optionen: 1,2,3,4")
        except ValueError:
            print("Bitte eine Zahl eingeben:")

text_option1 = """Sie kommen erstmal an die Hölle der Drache. Was wollen sie tun?
1. Nach Hause gehen.
2. Bewusst die Hölle betreten.
3. Die Drache mit der Geruch von Fleisch auslocken.
4. Hinterfragst dein Gedankengang weshalb du überhaupt ein Drache kämpfen möchte.
"""

# Spiel Programm

print("Willkommen zur Fantasy Spiel 'Dragon Slayer'")
      
name = input("Verrate mir dein Namen.\n")


print(f"\n{name},")
print(text_option1)
e1 = get_choice("Wähle. 1-4 ", {1,2,3,4}) 

if input == 1: 
    print("Du bist nach Hause gegangen. Der Drache har dann dein Dorf vernichtet. End.")
    exit()

