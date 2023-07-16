import utilities

def improve_close_mill(location, board, given_piece):
    """
    Check if moving a given piece to a specific location can improve the formation of a close mill.

    @param location: The target location to check for close mill improvement.
    @type location: int
    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]
    @param given_piece: The piece to be moved to the target location.
    @type given_piece: str

    @return: True if moving the given piece to the location improves a close mill, False otherwise.
    @rtype: bool
    """
    if board[location] == 'x' or board[location] != given_piece:
        return False

    # Check if moving the given piece to the location improves a close mill
    for pos in utilities.is_close_mill()[location]:
        if board[pos[0]] == board[location] or board[pos[1]] == board[location]:
            return True

    return False


def static_estimation_game_improved(board):
    """
    Perform an improved static estimation of the game state during the game phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: The improved static estimation value representing the game state.
    @rtype: int
    """
    # Generate lists of possible moves for black and white pieces
    black_moves_list = utilities.generateMovesBlackMidgameEndgame(board)
    white_moves_list = utilities.generateMovesMidgameEndgame(board)
    num_black_moves = len(black_moves_list)
    num_white_moves = len(white_moves_list)
    num_white = 0
    num_black = 0
    num_white_mills = 0
    num_black_mills = 0

    # Count the number of white mills, black mills, white pieces, and black pieces on the board
    for location in range(len(board)):
        if improve_close_mill(location, board, 'W'):
            num_white_mills += 1

        if improve_close_mill(location, board, 'B'):
            num_black_mills += 1

        if board[location] == 'W':
            num_white += 1
       
        elif board[location] == 'B':
            num_black += 1

    # Check for winning or losing conditions and return a corresponding improved static estimation value
    if num_black <= 2:
        return 10000
    elif num_white <= 2:
        return -10000
    elif num_black_moves == 0:
        return 10000
    else:
        return 1000 * ((num_white + num_white_mills + num_white_moves) - (num_black + num_black_mills)) - num_black_moves



def static_estimation_opening_improved(board):
    """
    Perform an improved static estimation of the game state during the opening phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: The improved static estimation value representing the game state.
    @rtype: int
    """
    num_white = 0
    num_black = 0
    num_white_mills = 0
    num_black_mills = 0

    # Generate lists of possible moves for white and black pieces during the opening phase
    white_moves_list = utilities.generateMovesOpening(board)
    num_white_moves = len(white_moves_list)
    black_moves_list = utilities.generateMovesBlackOpening(board)
    num_black_moves = len(black_moves_list)

    # Count the number of white mills, black mills, white pieces, and black pieces on the board
    for location in range(len(board)):
        if improve_close_mill(location, board, 'W'):
            num_white_mills += 1

        if improve_close_mill(location, board, 'B'):
            num_black_mills += 1

        if board[location] == 'W':
            num_white += 1
       
        elif board[location] == 'B':
            num_black += 1

    # Calculate the improved static estimation value for the opening phase based on piece counts and moves
    return (num_white + num_white_mills + num_white_moves) - (num_black + num_black_mills + num_black_moves)