def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below

    while True:
        value = input(prompt)

        if value not in valid_inputs:
            print('Invalid input, please try again.')
        else:
            return value


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below

    rows = 6
    cols = 7

    # Initialise board using list comprehension
    board = [[0 for i in range(cols)] for j in range(rows)]

    return board


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Implement your solution below

    numrows = len(board)
    numcols = len(board[0])

    for row in range(numrows - 1, -1, -1):
        if board[row][column - 1] == 0:
            board[row][column - 1] = player
            return True

    return False


def execute_player_turn(player, board):  # Task 5
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    numrows = len(board)
    numcols = len(board[0])

    valid_inputs = []

    for i in range(0, numcols):
        valid_inputs.append(str(i + 1))  # construct list of valid inputs

    # create a prompt depending on the player
    prompt = 'Player ' + str(player) + ', please enter the column you would like to drop your piece into: '

    while True:
        move = int(validate_input(prompt, valid_inputs))

        if drop_piece(board, player, move):
            return move
        else:
            print('That column is full, please try again.')


if __name__ == "__main__":
    # Enter test code below
    board = create_board()
    move = execute_player_turn(1, board)
    print(board)
