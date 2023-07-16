import utilities

def static_estimation_opening(board):
    """
    Perform static estimation of the game state during the opening phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: The static estimation value representing the difference between the number of 'W' and 'B' pieces.
    @rtype: int
    """
    num_white = 0
    num_black = 0

    # Count the number of 'W' and 'B' pieces on the board
    for i in board:
        if i == 'W':
            num_white += 1
        elif i == 'B':
            num_black += 1

    # Calculate and return the static estimation value
    return num_white - num_black


def static_estimation_game(board):
    """
    Perform static estimation of the game state during the game phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: The static estimation value representing the game state.
    @rtype: int
    """
    num_white = 0
    num_black = 0

    # Generate a list of possible game board positions resulting from black moves during midgame or endgame
    black_moves_list = utilities.generateMovesBlackMidgameEndgame(board)
    num_black_moves = len(black_moves_list)

    # Count the number of 'W' and 'B' pieces on the board
    for i in board:
        if i == 'W':
            num_white += 1
        elif i == 'B':
            num_black += 1

    # Check for winning or losing conditions and return a corresponding static estimation value
    if num_black <= 2:
        return 10000
    elif num_white <= 2:
        return -10000
    elif num_black_moves == 0:
        return 10000
    else:
        return 1000 * (num_white - num_black) - num_black_moves
