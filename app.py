# Code for X and O game

# Play location/postion
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# -----Global variables-----

# Is game is going?
game_still_going = True

# Who won? or tie?
winner = None

# Whose turn is it? Starting with X
current_player = "x"


# Function to display board (opt 1)
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# function to play game
def play_game():
    # call function to display board
    display_board()
    # while game is still running, run this loop
    while game_still_going:
        # manage player's turn
        handle_turn(current_player)
        # Check wins
        check_if_game_over()
        # Next player
        flip_player()
    # game isn't running, i.e: game_still_going = False
    if winner == "x" or winner == "o":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# def function to handle player's turn
# "player" is what ever parameter you put when calling the function
# In this case, "player" will be the current player, which was defined in the beginining as a global variable

def handle_turn(player):
    print(player + "'s turn.")
    position = input("choose a position on the board from 1 - 9: ")

    '''
    "valid" is a boolean variable introduced for purpose of a loop.
    To check for invalid position from the input.
    To trigger this, I then tell "for loop to assume that the variable in incorrect
    '''
    valid = False
    # Run loop (read previous comment)
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose a position on the board from 1 - 9: ")
        '''
        Convert input string to int, and then to index for computer to correctly place it,
        where 1 - 9 in 0 - 8 in index (number of digits remain the same,
        but count start it 1 less at the beging and end
        '''
        position = int(position) - 1

        # Now that We have converted to index, let's check is the postion is avaliable

        if board[position] == "_":
            # If the above state meant is true, all conditions tiers has been fulfilled.
            # In other words, the condition to run this parent loop no longer exist
            # we'll then change the intial set variable to True
            valid = True
        else:
            print("You can't go there. Play again")
    board[position] = player
    # display board
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


# define check for win
def check_for_winner():
    # call global variable
    global winner

    # these variables pick-up the winner from rows, columns, and diagonals is any

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonals()

    # Here we check which win it is row, winner, or diagonal. We then turn the winner in that as the winner
    # else we return non
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = column_winner
    else:
        winner = None
    return


# Function to row for win
def check_row():
    # Call global variable
    global game_still_going
    # check if 1 of 3 rows match in entries
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# Function to columns for win
def check_column():
    # Call global variable
    global game_still_going
    # check if 1 of 3 columns match in entries
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# Function to check diagonals for wins
def check_diagonals():
    # Call global variable
    global game_still_going
    # Check if 1 of the 2 diagonals match in entries, result is a boolean value
    diagonals_1 = board[0] == board[4] == board[8] != "_"
    diagonals_2 = board[2] == board[4] == board[6] != "_"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


# Checking for tie
def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return


# define function to change player's turn
def flip_player():
    # We need the global variable that tells us the current player
    global current_player
    # If player is x change to o
    if current_player == "x":
        current_player = "o"
    # If player is o change to x
    elif current_player == "o":
        current_player = "x"
    return


# Run function to play game
play_game()
