from tkinter import Button, Frame, Menu, Tk, messagebox
import random


class Xo:
    # All possible winning lines (indices in the flat button list)
    WINNING_COMBINATIONS = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    def __init__(self):
        self.window = Tk()
        self.window.title("xo")

        self.buttons = []
        self.all_buttons = []

        self.ai_turn = False
        self.game_over = False

        self.create_menu()
        self.create_buttons()
        self.start_game()

    def create_menu(self):
        menu_bar = Menu(master=self.window)
        self.window.config(menu=menu_bar)

        menu_bar.add_command(label="Reset Game", command=self.reset_board)
        menu_bar.add_command(label="Exit", command=self.exit_game)
        menu_bar.add_command(label="Info", command=self.info)

    def reset_board(self):
        """Clear the board and reset all game state."""
        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal")

        self.ai_turn = False
        self.game_over = False

    def exit_game(self):
        ask = messagebox.askquestion(
            title="xo",
            message="Are you sure you want to exit?"
        )
        if ask == "yes":
            self.window.destroy()

    @staticmethod
    def info():
        messagebox.showinfo(
            title="info",
            message=(
                "Hello!\n\n"
                "My name is Mohammad,\n\n"
                "I love Python programming.\n"
                "And I just started!\n\n"
                "Built with Python in September 2023\n\n"
            )
        )

    def create_buttons(self):
        self.frame = Frame(self.window)
        self.frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                button = Button(
                    self.frame,
                    text="",
                    width=8,
                    height=4,
                    font=("Tahoma", 20, "bold"),
                    command=lambda i=i, j=j: self.make_move(i, j)
                )
                button.grid(row=i, column=j)
                row.append(button)
                self.all_buttons.append(button)
            self.buttons.append(row)

    @staticmethod
    def start_game():
        messagebox.showinfo(
            "Instructions",
            "Welcome to Tic Tac Toe!\n\n"
            "You are the 'X' player. Click on any empty cell to make your move."
        )

    def make_move(self, row: int, col: int):
        # Ignore clicks after game over, during AI turn, or on used cells
        if self.game_over or self.ai_turn:
            return

        button = self.buttons[row][col]
        if button["text"] != "":
            return

        # Player's move
        button.config(text="X", fg="red", font=("Tahoma", 20, "bold"))

        # Check player win
        if self.check_win("X"):
            self.end_game("You win!")
            return

        # Check tie
        if self.check_tie():
            self.end_game("It's a tie!")
            return

        # AI's turn
        self.ai_turn = True
        self.ai_move()

    def ai_move(self):
        if self.game_over:
            return

        available = [b for b in self.all_buttons if b["text"] == ""]

        if not available:
            return

        # First try to win, then block the player, otherwise choose randomly
        move = self.find_winning_move("O") or self.find_winning_move("X")

        if move is None:
            move = random.choice(available)

        move.config(text="O", fg="blue", font=("Tahoma", 20, "bold"))

        # Check AI win
        if self.check_win("O"):
            self.end_game("AI wins!")
            return

        # Check tie
        if self.check_tie():
            self.end_game("It's a tie!")
            return

        self.ai_turn = False

    def find_winning_move(self, player: str):
        """
        Return an empty button that completes a line for the given player.
        Returns None if no such move exists.
        """
        for a, b, c in self.WINNING_COMBINATIONS:
            cells = (
                self.all_buttons[a],
                self.all_buttons[b],
                self.all_buttons[c],
            )
            texts = [cell["text"] for cell in cells]

            if texts.count(player) == 2 and texts.count("") == 1:
                for cell, text in zip(cells, texts):
                    if text == "":
                        return cell

        return None

    def check_win(self, player: str) -> bool:
        for a, b, c in self.WINNING_COMBINATIONS:
            if (
                self.all_buttons[a]["text"]
                == self.all_buttons[b]["text"]
                == self.all_buttons[c]["text"]
                == player
            ):
                return True

        return False

    def check_tie(self) -> bool:
        return all(button["text"] != "" for button in self.all_buttons)

    def end_game(self, message: str):
        """Finish the game, disable the board, and show the result."""
        self.game_over = True
        self.ai_turn = False

        for button in self.all_buttons:
            button.config(state="disabled")

        messagebox.showinfo("xo", message)


def main():
    xo = Xo()
    xo.window.mainloop()


if __name__ == "__main__":
    main()