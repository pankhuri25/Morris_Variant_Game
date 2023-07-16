import sys
import utilities
import improved


def MiniMax(board, depth, final_position, is_max_level):
    """
    Perform the MiniMax algorithm to determine the best move and its evaluation.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]
    @param depth: The current depth level of the search.
    @type depth: int
    @param final_position: The final best move determined by the algorithm.
    @type final_position: list[str]
    @param is_max_level: A flag indicating whether it is a maximizing player's turn.
    @type is_max_level: bool

    @return: The evaluation value and the final best move.
    @rtype: tuple[int, list[str]]
    """
    # Base case: reached maximum depth, evaluate and return current board position
    if depth == 0:
        utilities.positions_evaluated += 1
        return improved.static_estimation_opening_improved(board), board
    
    if is_max_level:
        max_eval = float('-inf')
        # Iterate over possible board positions resulting from opening moves
        for board_position in utilities.generateMovesOpening(board):
            # Recursively call MiniMax on each position with decreased depth and is_max_level set to False
            val = MiniMax(board_position, depth - 1, final_position, False)
            if val[0] > max_eval:
                max_eval = val[0]
                final_position = board_position

        return max_eval, final_position    
    
    else:
        min_eval = float('inf')
        # Iterate over possible board positions resulting from black moves during the opening phase
        for position in utilities.generateMovesBlackOpening(board):
            # Recursively call MiniMax on each position with decreased depth and is_max_level set to True
            val = MiniMax(position, depth - 1, final_position, True)
            if val[0] < min_eval:
                min_eval = val[0]
                final_position = val[1]

        return min_eval, final_position


if __name__ == '__main__':

    input_board, output_file, depth = utilities.fetch_input(sys.argv)

    positions = []
    positions = MiniMax(input_board, depth, positions, True)

    utilities.get_result(positions, output_file, utilities.positions_evaluated)
