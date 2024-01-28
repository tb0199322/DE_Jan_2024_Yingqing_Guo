import random
from game_2048_function
import initialize_game, print_board, move, is_game_over, is_game_won

def main():
    # Initialize the game
    board = initialize_game()

    while True:
        # Print the current state of the board
        print_board(board)

        # Get user input for movement (w, s, a, d)
        try:
            direction = input("Enter direction (w/a/s/d): ")
            move(board, direction)
        except ValueError as e:
            print(f"Invalid input. {e}")

        # Check if the game is won or over
        if is_game_won(board):
            print("Congratulations! You won the game. Do you want to restart the game?")
            break
        elif is_game_over(board):
            print("Game over. You can restart or end.")
            break

if __name__ == "__main__":
    main()