# Problem Set 1, Week 3 of Konzepte der Programmierung
# ui_tk.py
# We used AI to help about the GUI, however the code itself is is working even without gui (e.g. corelogic.py)

# Mahdi Bayanloo, 5598602
# Tim Schenk, 5611815

# ui_tk.py
import tkinter as tk
from tkinter import messagebox, ttk
from core_logic import (
    _new_board_for_gui,
    _apply_move_for_gui,
    _game_state_for_gui,
)

# ---- Visual constants ----
BG_APP = "#f7f7fb"
BG_CARD = "#ffffff"
BG_CARD_ACCENT = "#eef2ff"
FG_PRIMARY = "#0f172a"
FG_MUTED = "#475569"
FG_ACCENT = "#4f46e5"

CELL_FONT = ("Segoe UI", 24, "bold")   # Nice on Windows; fallback is automatic
STATUS_FONT = ("Segoe UI", 12)
TITLE_FONT = ("Segoe UI", 16, "bold")
BTN_FONT = ("Segoe UI", 12, "bold")


class TicTacToeApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Tic Tac Toe")
        root.configure(bg=BG_APP)

        try:
            ttk.Style().theme_use("clam")
        except Exception:
            pass

        # Shell
        self.container = tk.Frame(root, bg=BG_APP)
        self.container.pack(padx=16, pady=16, fill="both", expand=True)

        self.card = tk.Frame(self.container, bg=BG_CARD, bd=0, highlightthickness=0)
        self.card.pack(fill="both", expand=True)
        self.card.grid_columnconfigure(0, weight=1)

        # Header
        header = tk.Frame(self.card, bg=BG_CARD)
        header.grid(row=0, column=0, sticky="ew", padx=14, pady=(14, 6))

        self.title = tk.Label(header, text="Tic Tac Toe", bg=BG_CARD, fg=FG_PRIMARY, font=TITLE_FONT)
        self.title.pack(anchor="w")

        self.subtitle = tk.Label(
            header, text="Click a square to place your mark.",
            bg=BG_CARD, fg=FG_MUTED, font=STATUS_FONT
        )
        self.subtitle.pack(anchor="w", pady=(4, 0))

        # Status
        self.status = tk.Label(self.card, text="Turn: x", bg=BG_CARD, fg=FG_PRIMARY, font=STATUS_FONT)
        self.status.grid(row=1, column=0, sticky="w", padx=14, pady=(0, 8))

        # Board wrap
        self.board_wrap = tk.Frame(self.card, bg=BG_CARD, padx=6, pady=6)
        self.board_wrap.grid(row=2, column=0, padx=14, pady=8, sticky="nsew")
        self.card.grid_rowconfigure(2, weight=1)
        self.card.grid_columnconfigure(0, weight=1)

        self.board_frame = tk.Frame(self.board_wrap, bg=BG_CARD_ACCENT, padx=8, pady=8)
        self.board_frame.pack(fill="both", expand=True)

        # Init state
        self.board = _new_board_for_gui()
        self.buttons = []
        for r in range(3):
            row_btns = []
            for c in range(3):
                btn = tk.Button(
                    self.board_frame, text="", font= CELL_FONT,
                    width=3, height=1, relief="flat", bd=0,
                    bg=BG_CARD, fg=FG_PRIMARY,
                    activebackground="#f4f4ff", activeforeground=FG_PRIMARY,
                    cursor="hand2",
                    command=lambda rr=r, cc=c: self.on_click(rr, cc)
                )
                btn.grid(row=r, column=c, padx=8, pady=8, ipadx=6, ipady=6, sticky="nsew")
                btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#fafafa"))
                btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=BG_CARD))
                row_btns.append(btn)
            self.buttons.append(row_btns)

        for i in range(3):
            self.board_frame.grid_columnconfigure(i, weight=1)
            self.board_frame.grid_rowconfigure(i, weight=1)

        # Footer
        footer = tk.Frame(self.card, bg=BG_CARD)
        footer.grid(row=3, column=0, sticky="ew", padx=14, pady=(8, 14))

        self.reset_btn = tk.Button(
            footer, text="Restart", font=BTN_FONT, fg="white", bg=FG_ACCENT,
            activebackground="#4338ca", activeforeground="white",
            bd=0, relief="flat", padx=14, pady=8, cursor="hand2",
            command=self.reset
        )
        self.reset_btn.pack(anchor="e")

        self.update_status()
        self._center_window(370, 460)

    def on_click(self, r: int, c: int):
        # Get game state BEFORE the move to know who should play
        state, who = _game_state_for_gui(self.board)

        if state == "win":
            messagebox.showinfo("Game Over", f"🎉 {who} already won!")
            return
        if state == "draw":
            messagebox.showinfo("Game Over", "It's a draw.")
            return
        if state != "playing":
            return

        next_sign = who  # who = 'x' or 'o' when playing

        try:
            _apply_move_for_gui(self.board, r, c, next_sign)
        except ValueError as e:
            messagebox.showwarning("Invalid Move", str(e))
            return

        self.buttons[r][c].configure(text=next_sign)

        # Re-check game state AFTER the move
        state, who = _game_state_for_gui(self.board)
        if state == "win":
            self.status.configure(text=f"Winner: {who}")
            self._highlight_win()
            self._disable_board()
            messagebox.showinfo("Game Over", f"🎉 {who} wins!")
        elif state == "draw":
            self.status.configure(text="Draw")
            self._disable_board()
            messagebox.showinfo("Game Over", "It's a draw.")
        else:
            self.status.configure(text=f"Turn: {who}")

    def reset(self):
        self.board = _new_board_for_gui()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(text="", state="normal", bg=BG_CARD)
        self.update_status()

    def update_status(self):
        state, who = _game_state_for_gui(self.board)
        if state == "playing":
            self.status.configure(text=f"Turn: {who}")
        elif state == "win":
            self.status.configure(text=f"Winner: {who}")
        else:
            self.status.configure(text="Draw")

    def _disable_board(self):
        for row in self.buttons:
            for b in row:
                b.configure(state="disabled")

    def _center_window(self, w: int, h: int):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 3
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _highlight_win(self):
        # Local UI-only check to highlight the winning line
        b = self.board
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for line in lines:
            vals = [b[r][c] for r, c in line]
            if vals[0] is not None and vals.count(vals[0]) == 3:
                for r, c in line:
                    self.buttons[r][c].configure(bg="#dbeafe")  # soft blue
                return


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
