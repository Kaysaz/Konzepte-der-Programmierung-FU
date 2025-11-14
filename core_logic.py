#code-logic
#we used AI to help about the GUIbut the code itself is is working even without gui

# Mahdi Bayanloo 5598602
# Tim Schenk, 5611815


from typing import List, Optional, Tuple

Board = List[List[Optional[str]]]

def buildLine(reihe: List[Optional[str]]) -> str:
    """Returns a string like 'x| |o' from a row list such as ['x', None, 'o']."""
    def show(x): return "" if x is None else x
    return " | ".join(show(x) for x in reihe)

def printBoard(spielfeld: Board) -> None:
    """Prints the whole board using buildLine for each row."""
    for row in spielfeld:
        print(buildLine(row))

def checkWin(spielfeld: Board) -> Tuple[bool, Optional[str]]:
    """Checks if someone has won. Returns (True, 'x' or 'o') if there is a winner, otherwise (False, None)."""
    lines = []

    # Rows and columns
    for i in range(3):
        lines.append(spielfeld[i])  # row i
        lines.append([spielfeld[0][i], spielfeld[1][i], spielfeld[2][i]])  # column i

    # Diagonals
    lines.append([spielfeld[0][0], spielfeld[1][1], spielfeld[2][2]])
    lines.append([spielfeld[0][2], spielfeld[1][1], spielfeld[2][0]])

    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return True, line[0]
    return False, None

def placeSign(spieler: int, spielfeld: Board) -> Board:

    sign = 'x' if spieler == 1 else 'o'

    valid = False  # variable used instead of while True
    while not valid:
        try:
            raw = input(f"Player {spieler} ({sign}) – enter position as row,col (0-2): ").strip()
            parts = raw.split(",")
            if len(parts) != 2:
                raise ValueError("Please enter two numbers separated by a comma, e.g., 1,2.")
            r = int(parts[0].strip())
            c = int(parts[1].strip())

            # Bounds check
            if not (0 <= r <= 2 and 0 <= c <= 2):
                raise IndexError("Position outside the board. Use values 0, 1, or 2.")

            # Occupied check
            if spielfeld[r][c] is not None:
                raise ValueError("That cell is already taken. Choose another one.")

            # Apply move
            spielfeld[r][c] = sign
            valid = True  # condition now met, loop will stop

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except IndexError as ie:
            print(f"Invalid input: {ie}")
        except Exception:
            print("Invalid input. Please try again (example: 1,2).")

    return spielfeld

def ticTacToe() -> None:
    
    spielfeld: Board = [[None for _ in range(3)] for _ in range(3)]
    current_player = 1
    moves_played = 0

    print("Welcome to Tic Tac Toe!")
    print("Board positions are (row,col) with values 0, 1, 2.\n")
    printBoard(spielfeld)
    print("-" * 12)

    game_active = True  # temporary variable controlling the game loop
    while game_active:
        spielfeld = placeSign(current_player, spielfeld)
        moves_played += 1

        printBoard(spielfeld)
        print("-" * 12)

        # Check for winner
        won, who = checkWin(spielfeld)
        if won:
            print(f"Game over – Winner is '{who}'! 🎉")
            game_active = False
            continue  # end game loop

        # Check for draw
        if moves_played == 9:
            print("Game over – It's a draw.")
            game_active = False
            continue

        # Switch player
        current_player = 2 if current_player == 1 else 1

# Optional helpers for GUI (not required for assignment)
def _new_board_for_gui() -> Board:
    return [[None for _ in range(3)] for _ in range(3)]

def _apply_move_for_gui(board: Board, r: int, c: int, player_sign: str) -> None:
    if not (0 <= r <= 2 and 0 <= c <= 2):
        raise ValueError("Position outside the board.")
    if board[r][c] is not None:
        raise ValueError("Cell already taken.")
    if player_sign not in ('x', 'o'):
        raise ValueError("Sign must be 'x' or 'o'.")
    board[r][c] = player_sign

def _game_state_for_gui(board: Board) -> Tuple[str, Optional[str]]:
    won, who = checkWin(board)
    if won:
        return 'win', who
    if all(cell is not None for row in board for cell in row):
        return 'draw', None
    x_count = sum(cell == 'x' for row in board for cell in row)
    o_count = sum(cell == 'o' for row in board for cell in row)
    next_sign = 'x' if x_count == o_count else 'o'
    return 'playing', next_sign

if __name__ == "__main__":
    ticTacToe()
