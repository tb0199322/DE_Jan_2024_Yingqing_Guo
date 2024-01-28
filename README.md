This code provides the basic game mechanics for a simplified version of 2048. The game involves merging tiles by moving them in different directions (up, down, left, right) and aims to reach the tile with a value of 2048 to win.
1.	initialize_board():
•	Initializes a 4x4 game board with all cells set to 0.
•	Calls the add_random_tile() function to place a random tile (either 2 or 4) on an empty cell.
2.	add_random_tile(board):
•	Finds all empty cells on the board.
•	If there are empty cells, randomly selects one and places a tile with a value of 2 or 4 based on a probability (90% chance for 2, 10% chance for 4).
3.	display_board(board):
•	Prints the current state of the board to the console.
•	Uses "." to represent empty cells.
4.	merge_tiles(row):
•	Takes a row as input and merges adjacent tiles according to the game rules:
•	If two adjacent tiles have the same value, they merge into one tile with a value equal to their sum.
•	If there is an empty space between tiles, the tiles move towards the empty space.
5.	transpose_board(board):
•	Transposes the given board (rows become columns and vice versa).
6.	move_left(board):
•	Merges tiles in each row to the left.
•	Calls merge_tiles() for each row.
7.	move_right(board):
•	Merges tiles in each row to the right.
•	Calls merge_tiles() for each row, reverses the row, and then reverses it back.
8.	move_up(board):
•	Transposes the board, moves tiles left using move_left(), and then transposes it back.
9.	move_down(board):
•	Transposes the board, moves tiles right using move_right(), and then transposes it back.
10.	is_game_over(board):
•	Checks if the game is over:
•	If any cell is empty, the game is not over.
•	If two adjacent tiles in any row have the same value, the game is not over.
•	Returns True if the game is over; otherwise, returns False.

