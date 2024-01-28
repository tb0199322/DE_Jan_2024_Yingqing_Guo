from game_logic import initialize_board, display_board, move_up, move_left, move_down, move_right, add_random_tile, is_game_over

def main():
    board = initialize_board()
    while True:
        display_board(board)
        if is_game_over(board):
            print("Game Over")
            break
        move_input = input("Enter move (W/A/S/D): ").upper()
        if move_input == 'W':
            board = move_up(board)
        elif move_input == 'A':
            board = move_left(board)
        elif move_input == 'S':
            board = move_down(board)
        elif move_input == 'D':
            board = move_right(board)
        else:
            print("Invalid move. Use W/A/S/D.")

        add_random_tile(board)

if __name__ == "__main__":
    main()