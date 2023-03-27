import random


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


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    moves = list(range(1, len(board[0])))
    random.shuffle(moves)

    for move in moves:
        if drop_piece(board, player, move):
            return move

    return 0


if __name__ == "__main__":
    # Enter test code below
    board = create_board()

    cpu_player_easy(board, 1)
