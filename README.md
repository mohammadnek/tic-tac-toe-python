# Tic Tac Toe (Python + Tkinter)

A simple Tic Tac Toe game built with Python and Tkinter.
You play as **X** against a basic AI that plays as **O**.

This is a learning project to practice Python, Tkinter, and Git.

## Features

- 3x3 Tic Tac Toe board with a graphical interface
- Play against a simple AI opponent
- AI tries to win, then blocks the player, otherwise plays randomly
- Menu with Reset Game, Info, and Exit
- Win / lose / tie detection
- Board is locked after the game ends

## Requirements

- Python 3.8 or newer
- Tkinter (usually included with Python)

On Linux you may need to install Tkinter separately:

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

No third-party Python packages are required.

## How to Run

### 1. Check that Python is installed

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

### 2. Download or clone the project

Clone with Git:

```bash
git clone https://github.com/mohammadnek/tic-tac-toe-python.git
cd tic-tac-toe-python
```

Or simply download the files and open a terminal in the project folder.

### 3. Run the game

```bash
python tic_tac_toe.py
```

If `python` is not recognized, use:

```bash
python3 tic_tac_toe.py
```

On Windows you can also double-click `tic_tac_toe.py`, but running it from the terminal is recommended so you can see any error messages.

### 4. A window should open

If the game window does not open:

- Make sure Tkinter is installed (see the Requirements section).
- Make sure you are running the command from the folder that contains `tic_tac_toe.py`.

## How to Play

1. Run the program.
2. You are **X**. Click on any empty cell to make your move.
3. The AI responds with **O**.
4. The game ends when someone wins or the board is full.
5. Use **Reset Game** from the menu to play again.

## Project Structure

```
.
├── tic_tac_toe.py   # Main game file
├── README.md        # Project documentation
└── .gitignore       # Ignored files for Git
```

## Possible Future Improvements

- Smarter AI (Minimax algorithm)
- Two-player mode on the same device
- Score tracking
- Better UI and theme

## Author

**Mohammad**

Built with Python and Tkinter.

## License

This project is open source and available under the MIT License.
