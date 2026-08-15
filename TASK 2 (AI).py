import math

board = [" "] * 9

def show():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")


def winner():
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def minimax(ai):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if " " not in board:
        return 0

    scores = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if ai else "X"
            scores.append(minimax(not ai))
            board[i] = " "

    return max(scores) if ai else min(scores)


def ai_move():
    best = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"


print("TIC-TAC-TOE")
print("You = X | AI = O")
print("Choose positions 1 to 9")

while True:

    show()

    position = int(input("Enter position: ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move!")
        continue

    board[position] = "X"

    if winner() == "X":
        show()
        print("You Win!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break

    print("AI is thinking...")
    ai_move()

    if winner() == "O":
        show()
        print("AI Wins!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break
