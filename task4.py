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


# say for example row = 2, column = 4

# then board[row] = [0, 0, 0, 1, 0, 0, 0]

# then board[row][column - 1] = 1


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
    drop_piece(board, 1, 3)
    drop_piece(board, 2, 3)
    drop_piece(board, 1, 3)
    drop_piece(board, 2, 3)
    drop_piece(board, 1, 3)
    drop_piece(board, 2, 3)

    array = [[0, 1], [1, 2], [2, 3], [3, 4]]

    # array[2] = [2,3]

    # array[2][0] = 2

    for row in board:
        print(row)
