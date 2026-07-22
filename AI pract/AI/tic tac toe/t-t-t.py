import math

wins = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def print_board(b):
    print()
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()

def winner(b):
    for x, y, z in wins:
        if b[x] == b[y] == b[z] != " ":
            return b[x]
    if " " not in b:
        return "Draw"
    return None

def minimax(board, is_max):
    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, True))
                board[i] = " "
        return best

def ai_move(board):
    best = math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True)
            board[i] = " "
            if score < best:
                best = score
                move = i

    return move

board = [" "] * 9

print("Positions:")
print_board(["1","2","3","4","5","6","7","8","9"])

while True:
    move = int(input("Enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"
    print_board(board)

    if winner(board):
        break

    m = ai_move(board)
    board[m] = "O"

    print("AI Move:")
    print_board(board)

    if winner(board):
        break

result = winner(board)

if result == "X":
    print("You Win!")
elif result == "O":
    print("AI Wins!")
else:
    print("Draw!")













# import math
# wins = [
#     [0,1,2],[3,4,5],[6,7,8],
#     [0,3,6],[1,4,7],[2,5,8],
#     [0,4,8],[2,4,6]
# ]


# def printb(b):
#     print()
#     for i in range(0,9,3):
#         print(b[i] + "|" + b[i+1]+ "|"+ b[i+2])
#     print()



# def winner(b):
#     for x,y,z in wins:
#         if b[x]==b[y]==b[z]!=" ":
#             if b[x]=="X":
#                 return 1
#             else :
#                 return -1
#     return 0


# def minimax(board,is_max):
#     d= winner(board)
#     if d != 0:
#         return d
#     if " " not in board:
#         return 0

#     if is_max:
#         best = -math.inf
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "X"
#                 best = max(best, minimax(board, False))
#                 board[i] = " "
#         return best
#     else:
#         best = math.inf
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "O"
#                 best = min(best, minimax(board, True))
#                 board[i] = " "
#         return best

# def ai_play(b):
#     best=9999
#     move=-1
#     for i in range(9):
#         if b[i]==" ":
#             b[i]="O"
#             score = minimax(b, True)
#             b[i] = " "
#             if score < best:
#                 best = score
#                 move = i

#     return move           





# board=[" "]*9
# print("Positions:")
# printb(["1","2","3","4","5","6","7","8","9"])

# while True:
#     move = int(input("Enter your move (1-9): ")) - 1
#     board[move]='X'
#     print(board)

#     if winner(board)==1:
#         print("yes")
#         break

#     ai_move=ai_play(board)
#     board[ai_move]="O"
#     if winner(board)==-1:
#         print("no")
#         break


