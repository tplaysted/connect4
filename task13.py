import random
import copy


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
def create_board(rows, cols):
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below

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

    num_cols = len(board[0])

    print('========== ConnectK =========')  # print header

    col_list = '  '

    for i in range(0, num_cols):  # i takes the values 0 up to but not including num_cols
        col_list += (str((i + 1) % 10) + '   ')

    print()  # extra line
    print(col_list.rstrip())  # numbering the columns, not including spaces at end

    line_sep = ''

    for i in range(0, num_cols):
        line_sep += ' ---'

    print(line_sep)  # separate rows

    for row in board:
        row_str = '|'
        for cell in row:  # | O |   | X |
            if cell != 0:
                row_str += ' ' + str(cell) + ' |'
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

    num_rows = len(board)

    for row in range(num_rows - 1, -1, -1):  # start by inspecting bottom row, and work up
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
    num_cols = len(board[0])

    valid_inputs = []

    for i in range(0, num_cols):
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
def end_of_game(board, num_win):  # Question 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param num_win: number in a row to win
    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, -1 if draw.
    """
    # Implement your solution below

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
        return -1
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


def local_2_player_game(rows, cols, players, num_win):
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below

    player = 1

    board = create_board(rows, cols)

    last_move = 0
    last_player = 0

    while True:
        clear_screen()
        print_board(board)

        if last_move != 0:
            print('Player', last_player, 'dropped a piece into column', last_move)

        last_move = execute_player_turn(player, board)

        result = end_of_game(board, num_win)

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


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    moves = list(range(1, len(board[0]) + 1))
    random.shuffle(moves)

    for move in moves:
        if drop_piece(board, player, move):
            return move

    return 0


def cpu_player_medium(board, player, players, num_win):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param num_win: number to connect to win
    :param players: player list
    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below

    # ==== Checking for immediate wins ==== #

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, player, col):
            if end_of_game(test_board, num_win) == player:
                drop_piece(board, player, col)
                return col

    # ==== Checking for opponent immediate wins ==== #

    opponent = get_next_player(player, players)

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, opponent, col):
            if end_of_game(test_board, num_win) == opponent:
                drop_piece(board, player, col)
                return col

    # ==== Play a random move ==== #

    return cpu_player_easy(board, player)


def game_against_cpu(rows, cols, players, cpu_players, num_win):
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Implement your solution below

    # ==== Get game mode from player ==== #
    print('==== 1 (Easy) ====')
    print('==== 2 (Medium) ====')
    print('==== 3 (Hard) ====')
    mode = int(validate_input('Please select a cpu difficulty: ', ['1', '2', '3']))

    # ==== Game setup ==== #

    player = 1

    board = create_board(rows, cols)

    last_move = 0
    last_player = 0

    # ==== Begin game loop ==== #

    while True:
        clear_screen()
        print_board(board)

        if last_move != 0:
            print('Player', last_player, 'dropped a piece into column', last_move)

        if player not in cpu_players:
            last_move = execute_player_turn(player, board)
        else:
            if mode == 1:
                last_move = cpu_player_easy(board, player)
            elif mode == 2:
                last_move = cpu_player_medium(board, player, players, num_win)
            else:
                last_move = cpu_player_hard(board, player, players, num_win)

        result = end_of_game(board, num_win)

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


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def is_trap_for_player(board, player, move, num_win):
    """
    Checks whether the given move, if played by "player", lays an effective trap for them.

    :param num_win:
    :param board: Current game board
    :param player: Player who is next to play
    :param move: The move to check
    :return: True (is trap) False (not a trap or invalid)
    """

    test_board_1 = copy.deepcopy(board)

    if not drop_piece(test_board_1, player, move):
        return False

    for row in range(0, len(test_board_1) - 1):  # since we consider two-stacks
        for col in range(0, len(test_board_1[0])):
            test_board_2 = copy.deepcopy(test_board_1)
            test_board_3 = copy.deepcopy(test_board_1)

            if test_board_2[row][col] == 0:
                test_board_2[row][col] = player

            if test_board_3[row + 1][col] == 0:
                test_board_3[row + 1][col] = player

            result_1 = end_of_game(test_board_2, num_win)
            result_2 = end_of_game(test_board_3, num_win)

            if result_1 == player and result_2 == player:
                return True

    return False


def is_losing(board, player, move, players, num_win):
    """
    Returns true if the proposed move loses immediately for the current player, false otherwise

    :param num_win:
    :param players: player list
    :param board: Current board
    :param player: The player to play next
    :param move: Proposed move
    :return: boolean
    """

    test_board_1 = copy.deepcopy(board)
    next_player = get_next_player(player, players)

    if not drop_piece(test_board_1, player, move):
        return False

    for next_move in range(1, len(board[0]) + 1):
        test_board_2 = copy.deepcopy(test_board_1)

        if drop_piece(test_board_2, next_player, next_move):
            if end_of_game(test_board_2, num_win) == next_player:
                return True

    return False


def cpu_player_hard(board, player, players, num_win):
    """

    First, check to see if there are immediate threats and play accordingly if there are
    i.e. the medium strategy.

    Second, see if there are moves available to play which lay a trap, that is, two winning squares on top of one
    another. If it is not losing, play it.

    Third, see if the opponent has any traps which he can lay. If it is not losing, block them.

    Last, play the easy strategy

    :param num_win:
    :param players:
    :param board: the current game board
    :param player: the player who is next to play
    :return: the chosen move (int)
    """

    # ==== Starting with the medium strategy ==== #

    # ==== Checking for immediate wins ==== #

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, player, col):
            if end_of_game(test_board, num_win) == player:
                drop_piece(board, player, col)
                return col

    # ==== Checking for opponent immediate wins ==== #

    opponent = get_next_player(player, players)

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, opponent, col):
            if end_of_game(test_board, num_win) == opponent:
                drop_piece(board, player, col)
                return col

    # ==== Now check if we have any traps ==== #

    for col in range(1, len(board[0]) + 1):

        if is_trap_for_player(board, player, col, num_win):
            if not is_losing(board, player, col, players, num_win):
                if drop_piece(board, player, col):
                    return col

    # ==== Now check if opponent any traps ==== #

    for col in range(1, len(board[0]) + 1):

        if is_trap_for_player(board, opponent, col, num_win):
            if not is_losing(board, player, col, player, num_win):
                if drop_piece(board, player, col):
                    return col

    # ==== deploy random strategy (trying to avoid losing moves) ==== #

    moves = list(range(1, len(board[0]) + 1))
    random.shuffle(moves)

    for move in moves:
        if not is_losing(board, player, move, players, num_win):
            if drop_piece(board, player, move):
                return move

    # ==== give up hope ==== #

    return cpu_player_easy(board, player)


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below

    player_list = [1, 2, 3]
    cpu_player_list = [2]
    row_num = 10
    col_num = 13
    conn_num = 5

    valid_inputs = ['1', '2', '3', '4']
    prompt = 'Please choose an item: '

    while True:

        print('=============== Main Menu ===============')
        print('Welcome to Connect 4!')
        print('1. View Rules')
        print('2. Play a local 2 player game')
        print('3. Play a game against the computer')
        print('4. Exit')
        print('=========================================')

        choice = int(validate_input(prompt, valid_inputs))

        if choice == 1:
            clear_screen()
            print_rules()
        elif choice == 2:
            clear_screen()
            local_2_player_game(row_num, col_num, player_list, conn_num)
        elif choice == 3:
            clear_screen()
            game_against_cpu(row_num, col_num, player_list, cpu_player_list, conn_num)
        else:
            print('Bye bye!')
            break


def cpu_simulation(number_runs):
    """
    Pits hard cpu against medium cpu to compute efficiency


    :param number_runs: number of games to play
    :return: the percentage of games own by cpu_hard
    """

    player_list = [1, 2, 3, 4, 5]
    cpu_player_list = [3, 5]
    row_num = 10
    col_num = 13
    conn_num = 6

    wins = 0
    losses = 0
    draws = 0
    players = [1, 2]

    for i in range(0, number_runs):
        clear_screen()
        print('Running game number:', i)

        board = create_board(row_num, col_num)
        player = 1
        result = 0

        while result == 0:
            if player == 1:
                cpu_player_medium(board, player, player_list, conn_num)
            else:
                cpu_player_hard(board, player, player_list, conn_num)

            player = get_next_player(player, players)

            result = end_of_game(board, conn_num)

        if result == 2:
            wins += 1
        elif result == 3:
            draws += 1
        else:
            losses += 1

    wins = 100 * wins / number_runs
    draws = 100 * draws / number_runs
    losses = 100 * losses / number_runs

    print('Wins:', wins, ' Losses:', losses, ' Draws:', draws)


if __name__ == "__main__":
    # Enter test code below
    trap_board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 2, 2, 2, 0, 0],
                  [0, 0, 1, 1, 2, 0, 0], [2, 1, 1, 1, 2, 0, 1]]
    main()
