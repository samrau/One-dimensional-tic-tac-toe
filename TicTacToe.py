import random
#Step 1: Write a function evaluate that accepts the string with the board of 1D tic-tac-toe as argument and returns one character based on the state of the game:

def evaluate(board):
    # if there is a win
    if "xxx" in board:
        return "x wins!"
    elif "ooo" in board:
        return "o wins!"
    #if there is a draw
    if "-" not in board:
        return "! draw"
    #In case there is no win or no draw, the game is not finished
    return "-"

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    if position < 0 or position >= len(board):
        print("Invalid Position")
        return board
    if board[position] != "-":
        print("Invalid move. The position is taken")
        return board
    
    new_board = list(board)
    new_board[position] = mark

    return ''.join(new_board)

# Write a player_move function that accepts a string with the game board, asks the player which position he wants to play and returns 
#the updated game board with the player's move. The function should reject negative or too large numbers or moves to an occupied position. 
#If the user has entered a wrong argument, the function should ask again (to get correct answer).

def player_move(board):
    valid_move = False
    while not valid_move:
        try:
            position = int(input("Enter the position (0-{}): ".format(len(board) - 1)))
            if 0 <= position < len(board) and board[position] == '-':
                valid_move = True
            else:
                print("Invalid move. Please choose a valid number or unoccupied position.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    mark = input("Enter x or o: ")
    while mark not in ['x', 'o']:
        print("Invalid input. Please enter x or o: ")
        mark = input("Enter x or o: ")
    return move(board, mark, position)
#Step 4: Write a pc_move function that accepts the string with the game board. It will select a position to play, and returns the game board with the computer's move.

def pc_move(board):
    empty_positions = [i for i in range(len(board)) if board[i] == '-']

    while empty_positions:
        position = random.choice(empty_positions)

        if board[position] == '-':
            return move(board, 'o', position)
    print("No empty positions available.")
    return board

#Write a 1D_tictactoe function that creates a string with a game board and alternately calls the player_move and pc_move functions until someone wins or draws. 
#Do not forget to check the status of the game after every turn.
def play_1D_tictactoe():
# Initialize an empty board with 20 dashes
    current_board = "--------------------"

    # Play the game until there's a winner or a draw
    while True:
        # Player's move
        print("Player's Move:")
        current_board = player_move(current_board)
        print(current_board)
        result = evaluate(current_board)
        if result != "-":
            print("Game Over! Result:", result)
            break

        # Computer's move
        print("Computer's Move:")
        current_board = pc_move(current_board)
        print(current_board)
        result = evaluate(current_board)
        if result != "-":
            print("Game Over! Result:", result)
            break
# Run the game
play_1D_tictactoe()