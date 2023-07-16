import sys
import utilities
import staticEstimations

def miniMax(board, depth, final_position, isMax, alpha, beta):
    """
    Perform the MiniMax algorithm to determine the best move and its evaluation during the opening phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]
    @param depth: The current depth level of the search.
    @type depth: int
    @param final_position: The final best move determined by the algorithm.
    @type final_position: list[str]
    @param isMax: A flag indicating whether it is a maximizing player's turn.
    @type isMax: bool
    @param alpha: The current alpha value for pruning.
    @type alpha: int
    @param beta: The current beta value for pruning.
    @type beta: int

    @return: The evaluation value and the final best move.
    @rtype: tuple[int, list[str]]
    """
    # Base case: reached maximum depth, evaluate and return current board position
    if depth == 0:
        utilities.positions_evaluated += 1
        return staticEstimations.static_estimation_opening(board), board

    if isMax:
        max_eval = alpha
        # Iterate over possible board positions resulting from opening moves
        for board_position in utilities.generateMovesOpening(board):
            # Recursively call miniMax on each position with decreased depth
            val = miniMax(board_position, depth - 1, final_position, False, alpha, beta)
            
            # Pruning: if alpha >= beta, stop evaluating further moves
            if alpha >= beta:
                break
            else:
                # Update alpha value if a higher value is found
                alpha = max(max_eval, alpha)
            
            # Update max_eval and final_position if a better evaluation is found
            if val[0] > max_eval:
                max_eval = val[0]
                final_position = board_position

        return max_eval, final_position

    else:
        min_eval = beta
        # Iterate over possible board positions resulting from black moves during the opening phase
        for position in utilities.generateMovesBlackOpening(board):
            # Recursively call miniMax on each position with decreased depth
            val = miniMax(position, depth - 1, final_position, True, alpha, beta)
            
            # Pruning: if alpha >= beta, stop evaluating further moves
            if alpha >= beta:
                break
            else:
                # Update beta value if a lower value is found
                beta = min(min_eval, beta)
            
            # Update min_eval and final_position if a better evaluation is found
            if val[0] < min_eval:
                min_eval = val[0]
                final_position = val[1]
        
        return min_eval, final_position

    
if __name__ == '__main__':

    board, output_file, depth = utilities.fetch_input(sys.argv)

    final_position = []
    final_position = miniMax(board, depth, final_position, True, -sys.maxsize - 1, sys.maxsize)

    utilities.get_result(final_position, output_file, utilities.positions_evaluated)
