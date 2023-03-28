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
def end_of_game(board, num_win=4):  # Question 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param num_win: number to connect to win
    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
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


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below

    players = [1, 2]

    # ==== Checking for immediate wins ==== #

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, player, col):
            if end_of_game(test_board) == player:
                drop_piece(board, player, col)
                return col

    # ==== Checking for opponent immediate wins ==== #

    opponent = get_next_player(player, players)

    for col in range(1, len(board[0]) + 1):
        test_board = copy.deepcopy(board)

        if drop_piece(test_board, opponent, col):
            if end_of_game(test_board) == opponent:
                drop_piece(board, player, col)
                return col

    # ==== Play a random move ==== #

    return cpu_player_easy(board, player)


def game_against_cpu():
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

    players = [1, 2]
    player = 1

    board = create_board()

    last_move = 0
    last_player = 0

    # ==== Begin game loop ==== #

    while True:
        clear_screen()
        print_board(board)

        if last_move != 0:
            print('Player', last_player, 'dropped a piece into column', last_move)

        if player == 1:
            last_move = execute_player_turn(player, board)
        else:
            if mode == 1:
                last_move = cpu_player_easy(board, player)
            elif mode == 2:
                last_move = cpu_player_medium(board, player)
            else:
                last_move = cpu_player_hard(board, player)

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


def is_trap_for_player(board, player):
    """
    Checks whether there exists a two-stack trap in the position for a given player

    :param board: Current game board
    :param player: Player who is next to play
    :return: True (is trap) False (not a trap or invalid)
    """

    for row in range(0, len(board) - 1):  # since we consider two-stacks
        for col in range(0, len(board[0])):
            test_board_1 = copy.deepcopy(board)
            test_board_2 = copy.deepcopy(board)

            if test_board_1[row][col] == 0:
                test_board_1[row][col] = player

            if test_board_2[row + 1][col] == 0:
                test_board_2[row + 1][col] = player

            result_1 = end_of_game(test_board_1)
            result_2 = end_of_game(test_board_2)

            if result_1 == player and result_2 == player:
                return True

    return False


def is_losing(board, player, move):
    """
    Returns true if the proposed move loses immediately for the current player, false otherwise

    :param board: Current board
    :param player: The player to play next
    :param move: Proposed move
    :return: boolean
    """

    test_board_1 = copy.deepcopy(board)
    players = [1, 2]
    next_player = get_next_player(player, players)

    if not drop_piece(test_board_1, player, move):
        return False

    for next_move in range(1, len(board[0]) + 1):
        test_board_2 = copy.deepcopy(test_board_1)

        if drop_piece(test_board_2, next_player, next_move):
            if end_of_game(test_board_2) == next_player:
                return True

    return False


def static_eval(board, player):
    """
    Return an int which gauges the degree to which the position favours the given player

    +100 if player has connected 4, -100 if opponent has connected 4

    +1 if player has formed at least one trap (and opponent has not), -1 if opponent has formed at least one trap

    0 otherwise

    :param board:
    :param player:
    :return: evaluation
    """

    players = [1, 2]

    if end_of_game(board) == player:
        return 1000

    if end_of_game(board) in players:  # for many-player scenario
        return -1000

    if end_of_game(board, 3) in players:  # for many-player scenario
        return -1

    if end_of_game(board, 3) == player:
        return 1

    return 0


def minimax(board, depth, alpha, beta, max_player, player):
    """

    Recursive function to explore game tree

    :param board:
    :param depth:
    :param alpha:
    :param beta:
    :param max_player: the maximising player (remains constant from initial call)
    :param player: the player to play next
    :return: evaluation of the position tree explored to the given depth

    """

    players = [1, 2]

    if depth == 0 or end_of_game(board) != 0:
        return static_eval(board, max_player)

    children = []

    for move in range(1, len(board[0]) + 1):  # create a list of valid child positions
        child = copy.deepcopy(board)

        if drop_piece(child, player, move):
            children.append(child)

    random.shuffle(children)

    if player == max_player:
        max_eval = -1000
        for child in children:
            new_eval = minimax(child, depth - 1, alpha, beta, max_player, get_next_player(player, players))
            max_eval = max(max_eval, new_eval)

            alpha = max(alpha, new_eval)
            if beta <= alpha:
                break

        return max_eval
    else:
        min_eval = 1000
        for child in children:
            new_eval = minimax(child, depth - 1, alpha, beta, max_player, get_next_player(player, players))
            min_eval = min(min_eval, new_eval)

            beta = min(beta, new_eval)
            if beta <= alpha:
                break

        return min_eval


def centreness(col):
    middle = 4
    return middle - abs(middle - col[0])


def cpu_player_hard(board, player):
    """

    Implement the minimax algorithm with alpha-beta pruning

    :param board: the current game board
    :param player: the player who is next to play
    :return: the chosen move (int)
    """

    players = [1, 2]

    move_evals = []  # move evaluations according to minimax

    for move in range(1, len(board[0]) + 1):  # get move evaluations
        test_board = copy.deepcopy(board)
        if drop_piece(test_board, player, move):
            move_evals.append([move, minimax(test_board, 7, -1000, 1000, player, get_next_player(player, players))])

    min_eval = -100
    best_move = 1

    move_evals.sort(key=centreness)  # favour central moves

    for move in move_evals:
        if move[1] >= min_eval:
            min_eval = move[1]
            best_move = move[0]

    drop_piece(board, player, best_move)
    return best_move


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below

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
            local_2_player_game()
        elif choice == 3:
            clear_screen()
            game_against_cpu()
        else:
            print('Bye bye!')
            break


def cpu_simulation(number_runs):
    """
    Pits hard cpu against medium cpu to compute efficiency


    :param number_runs: number of games to play
    :return: the percentage of games own by cpu_hard
    """

    wins = 0
    losses = 0
    draws = 0
    players = [1, 2]
    result = -1

    for i in range(0, number_runs):
        clear_screen()
        print('Last result: ', result)
        print('Running game number:', i)

        board = create_board()
        player = 1
        result = 0

        while result == 0:
            if player == 1:
                cpu_player_medium(board, player)
            else:
                cpu_player_hard(board, player)

            player = get_next_player(player, players)

            result = end_of_game(board)

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
