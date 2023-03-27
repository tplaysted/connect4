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
        line_sep += (' ---')

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


if __name__ == "__main__":
    # Enter test code below
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 1, 2, 2], [0, 0, 0, 1, 2, 2, 2]]
    print_board(board)
    print(end_of_game(board))
