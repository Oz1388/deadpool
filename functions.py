# functions.py

def print_board(board):
    """Display the current Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there’s a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def make_move(board, player, row, col):
    """Place the player's mark on the board if valid."""
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("That spot is already taken!")
        return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)
