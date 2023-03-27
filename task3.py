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


if __name__ == "__main__":
    # Enter test code below
    board = create_board()
    print_board(board)