# Tic Tac Toe game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if there's a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(spot != " " for spot in board)

# Main function to play the game
def play_tic_tac_toe():
    board = [" "] * 9  # Empty board
    current_player = "X"  # X starts the game

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("That spot is already taken! Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_tic_tac_toe()
