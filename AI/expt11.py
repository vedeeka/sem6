import math

# Initialize empty Tic-Tac-Toe board
board = [' '] * 9

# Winning combinations
wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


# Function to display board
def print_board():

    print()

    for i in range(0, 9, 3):
        print(
            f" {board[i]} | {board[i+1]} | {board[i+2]} "
        )

        if i < 6:
            print("---|---|---")

    print()


# Function to check winner
def check_winner(player):

    return any(
        all(board[i] == player for i in pos)
        for pos in wins
    )


# Function to check draw
def is_draw():

    return ' ' not in board


# Minimax Algorithm
def minimax(is_max):

    # Base conditions
    if check_winner('X'):
        return 1

    if check_winner('O'):
        return -1

    if is_draw():
        return 0

    # Maximizing player (X)
    if is_max:

        best = -math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                value = minimax(False)

                board[i] = ' '

                best = max(best, value)

        return best

    # Minimizing player (O)
    else:

        best = math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                value = minimax(True)

                board[i] = ' '

                best = min(best, value)

        return best


# Find best move for AI
def find_best_move():

    best_value = -math.inf
    best_move = -1

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'X'

            value = minimax(False)

            board[i] = ' '

            if value > best_value:

                best_value = value
                best_move = i

    return best_move


# ---------------- MAIN PROGRAM ---------------- #

print("TIC-TAC-TOE USING MINIMAX")
print("\nPositions are numbered from 1 to 9 as:")

print("""
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
""")


# Optional initial board state
choice = input("Enter initial board state? (y/n): ").lower()

if choice == 'y':

    print("\nUse X, O or leave blank")

    for i in range(9):

        value = input(f"Position {i+1}: ").upper()

        if value in ['X', 'O']:
            board[i] = value
        else:
            board[i] = ' '


# Game loop
while True:

    print_board()

    # Check if AI already won
    if check_winner('X'):
        print("X wins!")
        break

    # Check if player won
    if check_winner('O'):
        print("O wins!")
        break

    # Check draw
    if is_draw():
        print("Draw!")
        break

    # Player move
    try:

        move = int(input("Enter position (1-9): ")) - 1

        if move not in range(9):
            print("Invalid position!")
            continue

        if board[move] != ' ':
            print("Cell already occupied!")
            continue

        board[move] = 'O'

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Check after player move
    if check_winner('O'):
        print_board()
        print("O wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    # AI move
    x_move = find_best_move()

    board[x_move] = 'X'

    print(f"\nX chooses position {x_move + 1}")

    # Check after AI move
    if check_winner('X'):
        print_board()
        print("X wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break