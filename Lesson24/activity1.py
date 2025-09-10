def print_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]} \n -+-+-+-+-+-")
    print(f"{board[4]} | {board[5]} | {board[6]} \n -+-+-+-+-+-")
    print(f"{board[1]} | {board[2]} | {board[3]} \n -+-+-+-+-+-")

def check_winner(board, player):
    if (board[7] == board[8] == board[9] == player or
        board[4] == board[5] == board[6] == player or
        board[1] == board[2] == board[3] == player or
        board[7] == board[4] == board[1] == player or
        board[8] == board[5] == board[2] == player or
        board[9] == board[6] == board[3] == player or
        board[7] == board[5] == board[3] == player or
        board[9] == board[5] == board[1] == player):
        return True
    return False
def game():
    board = {i: " " for i in range(1, 10)}
    turn = "x"
    count = 0

    while count < 9:
        print_board(board)
        move = int(input(f'player {turn}, enter your move(1-9): '))

        if board.get(move) == " ":
            board[move] = turn
            count += 1
            if count >= 5 and check_winner(board, turn):
                print_board(board)
                print(f'Game Over!!! player {turn} wins.....')
                break
            if turn == "x":
                turn = "o"
            else:
                turn = "x"
        else:
            print("Invalid move. Try again.")
    else:
        print("it is a tie")
    
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        game()
game()
        