# Copy and paste validate_input here
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


# Copy and paste create_board here
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


# Copy and paste print_board here
def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    # Implement your solution below

    numrows = len(board)
    numcols = len(board[0])

    print('========== Connect4 =========')  # print header
    print('Player 1: X       Player 2: O')

    col_list = '  '

    for i in range(0, numcols):  # i takes the values 0 up to but not including numcols
        col_list += (str(i + 1) + '   ')

    print()  # extra line
    print(col_list.rstrip())  # numbering the columns, not including spaces at end

    line_sep = ''

    for i in range(0, numcols):
        line_sep += ' ---'

    print(line_sep)  # separate rows

    for row in board:
        row_str = '|'
        for cell in row:  # | O |   | X |
            if cell == 1:
                row_str += ' X |'
            elif cell == 2:
                row_str += ' O |'
            else:
                row_str += '   |'
        print(row_str)
        print(line_sep)

    print('=============================')


# Copy and paste drop_piece here
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

    for row in range(numrows - 1, -1, -1):  # start by inspecting bottom row, and work up
        if board[row][column - 1] == 0:
            board[row][column - 1] = player
            return True

    return False


# Copy and paste execute_player_turn here
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


# Copy and paste end_of_game here
def end_of_game(board):  # Question 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below
    numrows = len(board)
    numcols = len(board[0])

    num_win = 4

    game_over = True

    # ==== Checking for horizontal wins ==== #

    for i, row in enumerate(board):
        for j, val in enumerate(row[0:len(row) - num_win + 1]):
            is_win = True

            if val == 0:
                game_over = False
                continue

            for k in range(1, num_win):
                if board[i][j + k] != val:
                    is_win = False
                    break

            if is_win:
                return val

    # ==== Checking for vertical wins ==== #

    for i, row in enumerate(board[0:len(board) - num_win + 1]):
        for j, val in enumerate(row):
            is_win = True

            if val == 0:
                game_over = False
                continue

            for k in range(1, num_win):
                if board[i + k][j] != val:
                    is_win = False
                    break

            if is_win:
                return val

    # ==== Checking for diagonal (sloping down) wins ==== #

    for i, row in enumerate(board[0:len(board) - num_win + 1]):
        for j, val in enumerate(row[0:len(row) - num_win + 1]):
            is_win = True

            if val == 0:
                game_over = False
                continue

            for k in range(1, num_win):
                if board[i + k][j + k] != val:
                    is_win = False
                    break

            if is_win:
                return val

    # ==== Checking for diagonal (sloping up) wins ==== #

    for i, row in enumerate(board[0:len(board) - num_win + 1]):
        for j, val in enumerate(row[num_win - 1:len(row)]):
            is_win = True

            if val == 0:
                game_over = False
                continue

            for k in range(1, num_win):
                if board[i + k][j - k + num_win - 1] != val:
                    is_win = False
                    break

            if is_win:
                return val

    # ==== No-win scenario ==== #

    if game_over:
        return 3
    else:
        return 0


# Don't forget to include any helper functions you may have created
def get_next_player(player, players):
    """
    Returns the number of the player whose turn it is next
    Order goes according to the players array

    :param player: int
    :param players: array[int]
    :return: int
    """

    if player not in players:
        raise ValueError('Player passed does not belong to player list')

    index = players.index(player) + 1

    if index == len(players):
        return players[0]
    else:
        return players[index]


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below
    players = [1, 2]
    player = 1

    board = create_board()

    last_move = 0
    last_player = 0

    while True:
        clear_screen()
        print_board(board)

        if last_move != 0:
            print('Player', last_player, 'dropped a piece into column', last_move)

        last_move = execute_player_turn(player, board)

        result = end_of_game(board)

        if result > 0:
            clear_screen()
            print_board(board)
            break
        else:
            last_player = player
            player = get_next_player(player, players)

    if result == 3:
        print('Game over! It was a draw')
    else:
        print('Game over! Player', result, 'was the winner.')


if __name__ == "__main__":
    # Enter test code below
    local_2_player_game()
