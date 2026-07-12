import math

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]             
]

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def evaluate(board):
    x_lines = sum(1 for line in WIN_LINES if 'O' not in [board[i] for i in line])
    o_lines = sum(1 for line in WIN_LINES if 'X' not in [board[i] for i in line])
    return x_lines - o_lines

def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return 'Draw' if ' ' not in board else None

def is_terminal(board):
    return check_winner(board) is not None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1 
    if winner == 'O': return -1 
    if winner == 'Draw': return 0
    
    if depth == 0:
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                max_eval = max(max_eval, minimax(board, depth - 1, False))
                board[i] = ' '
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                min_eval = min(min_eval, minimax(board, depth - 1, True))
                board[i] = ' '
        return min_eval

def get_ai_move(board, depth_limit=4):
    best_score = math.inf
    best_move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_score = minimax(board, depth_limit - 1, True)
            board[i] = ' '
            
            if move_score < best_score:
                best_score = move_score
                best_move = i
                
    return best_move

def play_game():
    board = [' '] * 9
    
    print("Welcome to Tic-Tac-Toe!\nYou are 'X' and the AI is 'O'.\nPositions are numbered 1-9, mapping left-to-right, top-to-bottom.")
    
    demo_board = [str(i) for i in range(1, 10)]
    print_board(demo_board)
    print("Let's begin!")
    
    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = 'X'
                    break
                print("Invalid move! Spot is taken or out of bounds. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                
        print_board(board)
        
        if is_terminal(board):
            break

        print("AI is thinking...")
        ai_idx = get_ai_move(board, depth_limit=4)
        board[ai_idx] = 'O'
        print(f"AI plays at position {ai_idx + 1}:")
        print_board(board)
        
        if is_terminal(board):
            break

    result = check_winner(board)
    if result == 'X':
        print("Congratulations! You won!")
    elif result == 'O':
        print("The AI wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()