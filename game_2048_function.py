def initialize_game():
    # Initialize a 4x4 grid with two random 2s
    # Represent empty cells with 0
    board = [[0] * 4 for _ in range(4)]
    for _ in range(2):
        place_random_2(board)
    return board

def place_random_2(board):
    # Place a random 2 in an empty cell
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" ".join(map(str, row)))
    print()

def move(board, direction):
    # Implement the movement logic
    # This function should handle invalid inputs using exception handling
    # Update the board accordingly

def is_game_won(board):
    # Check if 2048 is present on the board

def is_game_over(board):
    # Check if no more moves are possible