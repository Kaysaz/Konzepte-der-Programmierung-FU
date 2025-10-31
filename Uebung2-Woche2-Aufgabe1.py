# Tim Schenk 
# Vorlesung: Konzepte der Programmierung
# 2. Übungsblatt Aufgabe 1
# 30.10.2025

import os


def clear_screen():
    """Clear the console screen in a cross-platform way."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        # Fallback: print several newlines if clearing fails
        print("\n" * 100)


def read_player_name(prompt_text):
    """Read a non-empty player name."""
    while True:
        name = input(prompt_text).strip()
        if name:
            return name
        print("Bitte gib einen gültigen Namen ein.")


def read_secret_word(player_one_name):
    """Read and validate the secret word (letters only)."""
    while True:
        secret_raw = input(f"{player_one_name}, gib ein geheimes Wort ein (nur Buchstaben): ").strip()
        if secret_raw and secret_raw.isalpha():
            return secret_raw
        print("Ungültige Eingabe. Erlaubt sind nur Buchstaben (keine Leerzeichen/Ziffern/Sonderzeichen).")


def show_progress(current_progress, guessed_letters, wrong_guesses, max_wrong):
    print()
    print("Aktueller Stand:")
    print(" ".join(current_progress))
    print(f"Geratene Buchstaben: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print(f"Fehlversuche: {wrong_guesses}/{max_wrong}")
    print()


def main():
    print("Willkommen zum Galgenmännchen (2-Spieler-Version)!\n")

    # (1) Namen der Spieler:innen
    player_one_name = read_player_name("Name von Spieler:in 1 (legt das Wort fest): ")
    player_two_name = read_player_name("Name von Spieler:in 2 (rät das Wort): ")

    # (2) Spieler:in 1 gibt ein Wort ein, nur Buchstaben erlaubt
    secret_word_original = read_secret_word(player_one_name)
    secret_word = secret_word_original.lower()

    # Privatsphäre: Bildschirm leeren, damit Spieler:in 2 das Wort nicht sieht
    clear_screen()

    # (3) Spieler:in 2 bekommt die Information, wie lang das Wort ist
    print(f"{player_two_name}, das geheime Wort hat {len(secret_word)} Buchstaben.")

    # Spielzustand
    current_progress = ["_" for _ in secret_word]
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 10

    # (3) und (4) Raten-Schleife mit Hinweisen
    while wrong_guesses < max_wrong and "_" in current_progress:
        show_progress(current_progress, guessed_letters, wrong_guesses, max_wrong)

        guess_raw = input(f"{player_two_name}, gib einen Buchstaben ein: ").strip()
        if not guess_raw:
            print("Bitte gib etwas ein.")
            continue

        guess = guess_raw.lower()

        # Erlaube genau einen Buchstaben (keine Ziffern/Zeichen)
        if len(guess) != 1 or not guess.isalpha():
            print("Ungültige Eingabe. Bitte genau einen Buchstaben eingeben.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' wurde bereits geraten.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            # (4a) Treffer: Positionen aufdecken
            for index, ch in enumerate(secret_word):
                if ch == guess:
                    current_progress[index] = secret_word_original[index]  # erhalte Original-Groß/Kleinschreibung

            print(f"Treffer! Der Buchstabe '{guess}' kommt im Wort vor.")

            if "_" not in current_progress:
                # Wort vollständig gelöst
                break
        else:
            # (4b) Kein Treffer
            wrong_guesses += 1
            print(f"Leider falsch. Der Buchstabe '{guess}' kommt nicht vor.")

    # (5) Auswertung: gewonnen oder verloren
    print()
    if "_" not in current_progress:
        print("Glückwunsch! Du hast das Wort gelöst!")
        print("Wort:", "".join(current_progress))
    else:
        print("Schade, du hast verloren.")
        print(f"Das gesuchte Wort war: {secret_word_original}")
        print(f"Fehlversuche insgesamt: {wrong_guesses}/{max_wrong}")


if __name__ == "__main__":
    main()

    # alle print args neu schreiben


