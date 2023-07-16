# global variable set so that every time the utilities file is called, the count increments.
positions_evaluated = 0 

def is_close_mill():
    """
    Get a dictionary of possible mill configurations.

    @return: A dictionary containing possible mill configurations.
    @rtype: dict
    """
    possible_mill_dict = {
        0: [(6,18)], 
        1: [(11,20)], 
        2: [(7,15)], 
        3: [(10,17)],
        4: [(8,12)], 
        5: [(9,14)], 
        6: [(7,8), (0,18)], 
        7: [(6,8), (2,15)], 
        8: [(6,7),(4,12)],
        9: [(5,14),(10,11)], 
        10: [(3,17), (9,11)], 
        11: [(1,20), (9,10)], 
        12: [(4,8), (13,14)],
        13: [(12,14), (16,19)], 
        14: [(5,9), (12,13)], 
        15: [(16,17),(2,7)],
        16: [(13,19), (15,17)], 
        17: [(3,10), (15,16)], 
        18: [(0,6), (19,20)],
        19: [(13,16), (18,20)], 
        20: [(18,19), (1,11)]
    }
    return possible_mill_dict


def closeMill(location, board):

    """
    Check if a given location on the board forms a mill.

    @param location: The position on the board to check for a mill.
    @type location: int
    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: True if a mill is formed at the given location, False otherwise.
    @rtype: bool
    """
    
    # Retrieve the piece at the given location on the board
    piece = board[location]

    # If the piece is 'x', no mill can be formed at that location
    if piece == 'x':
        return False

    # Obtain the mill_locations using the is_close_mill() function
    mill_locations = is_close_mill()

    # Iterate over each position in mill_locations corresponding to the given location
    for pos in mill_locations[location]:
        # Assign x1 and x2 the values from pos
        x1, x2 = pos

        # Check if board[x1] and board[x2] are equal to the piece
        if (board[x1] == piece and board[x2] == piece):
            # Return True indicating a mill is formed
            return True

    # If no mill is found, return False
    return False



def neighbours(j):
    """
    Get a list of neighboring locations for a given location on the game board.

    @param j: The location on the game board.
    @type j: int

    @return: A list of neighboring locations for the given position.
    @rtype: list[int]
    """
    if j == 0:
        return [1, 6]
    elif j == 1:
        return [0, 11]
    elif j == 2:
        return [3, 7]
    elif j == 3:
        return [2, 10]
    elif j == 4:
        return [5, 8]
    elif j == 5:
        return [4, 9]
    elif j == 6:
        return [0, 7, 18]
    elif j == 7:
        return [2, 6, 8, 15]
    elif j == 8:
        return [4, 7, 12]
    elif j == 9:
        return [5, 10, 14]
    elif j == 10:
        return [3, 9, 11, 17]
    elif j == 11:
        return [1, 10, 20]
    elif j == 12:
        return [8, 13]
    elif j == 13:
        return [12, 14, 16]
    elif j == 14:
        return [9, 13]
    elif j == 15:
        return [7, 16]
    elif j == 16:
        return [13, 15, 17, 19]
    elif j == 17:
        return [10, 16]
    elif j == 18:
        return [6, 19]
    elif j == 19:
        return [16, 18, 20]
    elif j == 20:
        return [11, 19]



def generateRemove(b, position_list):
    """
    Generate a list of possible game board positions resulting from removing a black ('B') piece.

    @param b: The current state of the game board represented as a list of pieces.
    @type b: list[str]
    @param position_list: The list to which the modified board positions will be appended.
    @type position_list: list[list[str]]

    @return: None
    """
    # Flag to track if any position for removal is found
    position_found = False

    # Iterate over each location on the board
    for location in range(len(b)):
        if b[location] == 'B':
            # Check if the black piece forms a mill at the current location
            if not closeMill(location, b):
                position_found = True

                # Create a copy of the board and modify it by removing the black piece
                b_copy = b.copy()
                b_copy[location] = 'x'

                # Append the modified board to the position list
                position_list.append(b_copy)

    # If no position for removal is found, append the original board state to the position list
    if not position_found:
        position_list.append(b)


def generateAdd(board) -> list[list[str]]:
    """
    Generate a list of possible game board positions resulting from adding a 'W' piece to an unoccupied position.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from adding a 'W' piece.
    @rtype: list[list[str]]
    """
    position_list = []

    # Iterate over each location on the board
    for location in range(len(board)):
        # Check if the position is unoccupied ('x')
        if board[location] == 'x':
            # Create a copy of the board and modify it by adding 'W' to the unoccupied position
            b = board.copy()
            b[location] = 'W'

            # Check if a mill is formed at the new position
            if closeMill(location, b):
                # Call the generateRemove() method to generate positions resulting from removing opponent's pieces
                generateRemove(b, position_list)
            else:
                # Add the modified board state to the position list
                position_list.append(b)

    # Return the list of possible positions resulting from adding a 'W' piece
    return position_list




def generateMove(board) -> list[list[str]]:
    """
    Generate a list of possible game board positions resulting from a move made by the 'W' player.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from the 'W' player's move.
    @rtype: list[list[str]]
    """
    position_list = []

    # Iterate over each location on the board
    for location in range(len(board)):
        # Check if the piece at the current location is 'W'
        if board[location] == 'W':
            # Obtain the neighboring positions using the neighbours() function
            n = neighbours(location)

            # Iterate over each neighboring position
            for i in n:
                # Check if the position is unoccupied ('x')
                if board[i] == 'x':
                    # Create a copy of the board and modify it by moving 'W' to the unoccupied position
                    b = board.copy()
                    b[location] = 'x'
                    b[i] = 'W'

                    # Check if a mill is formed at the new position
                    if closeMill(i, b):
                        # Call the generateRemove() method to generate positions resulting from removing opponent's pieces
                        generateRemove(b, position_list)
                    else:
                        # Add the modified board state to the position list
                        position_list.append(b)

    # Return the list of possible positions resulting from the 'W' player's move
    return position_list



def generateHopping(board) -> list[list[str]]:
    """
    Generate a list of possible game board positions resulting from a 'W' piece hopping to an unoccupied position.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from 'W' piece hopping.
    @rtype: list[list[str]]
    """
    position_list = []

    # Iterate over each position on the board
    for i in range(len(board)):
        # Check if the current position contains a 'W' piece
        if board[i] == 'W':
            # Iterate over each position on the board again
            for j in range(len(board)):
                # Check if the current position is different from the original position and unoccupied ('x')
                if i != j and board[j] == 'x':
                    # Create a copy of the board and modify it by hopping 'W' from the original position to the unoccupied position
                    b = board.copy()
                    b[i] = 'x'
                    b[j] = 'W'

                    # Check if a mill is formed at the new position
                    if closeMill(j, b):
                        # Call the generateRemove() method to generate positions resulting from removing opponent's pieces
                        generateRemove(b, position_list)
                    else:
                        # Add the modified board state to the position list
                        position_list.append(b)

    # Return the list of possible positions resulting from 'W' piece hopping
    return position_list



def generateMovesOpening(board) -> list[list[str]]:
    """
    Generate a list of possible game board positions resulting from opening moves.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from opening moves.
    @rtype: list[list[str]]
    """
    # Call the generateAdd() method to generate possible positions resulting from adding a 'W' piece
    return generateAdd(board)


def generateMovesMidgameEndgame(board) -> list[list[str]]:
    """
    Generate a list of possible game board positions resulting from midgame or endgame moves.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from midgame or endgame moves.
    @rtype: list[list[str]]
    """
    num_white = 0

    # Count the number of 'W' pieces on the board
    for i in range(len(board)):
        if board[i] == 'W':
            num_white += 1

    # Check the number of 'W' pieces
    if num_white == 3:
        # If there are exactly 3 'W' pieces, call generateHopping() to generate possible positions from hopping
        return generateHopping(board)
    else:
        # Otherwise, call generateMove() to generate possible positions from regular moves
        return generateMove(board)

    

def swap(board):
    """
    Swap the 'W' pieces with 'B' pieces and unoccupied positions ('x') in the game board.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: The board with 'W' pieces swapped with 'B' pieces and 'x' positions preserved.
    @rtype: list[str]
    """
    swapped_board = []

    # Iterate over each element in the board
    for element in board:
        if element == 'W':
            # Swap 'W' piece with 'B'
            swapped_board.append('B')
        elif element == 'B':
            # Swap 'B' piece with 'W'
            swapped_board.append('W')
        else:
            # Preserve unoccupied position ('x')
            swapped_board.append('x')

    # Return the swapped board
    return swapped_board


    
def blackMoveList(black_position_list):
    """
    Generate a list of game board positions resulting from black moves, with 'W' and 'B' pieces swapped.

    @param black_position_list: The list of game board positions for black moves.
    @type black_position_list: list[list[str]]

    @return: A list of game board positions resulting from black moves, with 'W' and 'B' pieces swapped.
    @rtype: list[list[str]]
    """
    black_moves_list = []

    # Iterate over each board position in the black position list
    for board_pos in black_position_list:
        # Swap 'W' and 'B' pieces in the board position
        black_moves_list.append(swap(board_pos))

    # Return the list of game board positions resulting from black moves with swapped 'W' and 'B' pieces
    return black_moves_list



def generateMovesBlackOpening(board):
    """
    Generate a list of possible game board positions resulting from black moves during the opening phase.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from black moves.
    @rtype: list[list[str]]
    """
    # Swap 'W' and 'B' pieces in the board
    swapped_board = swap(board)

    # Generate a list of possible game board positions resulting from opening moves
    black_position_list = generateMovesOpening(swapped_board)

    # Generate a list of game board positions resulting from black moves with 'W' and 'B' pieces swapped
    return blackMoveList(black_position_list)



def generateMovesBlackMidgameEndgame(board):
    """
    Generate a list of possible game board positions resulting from black moves during midgame or endgame.

    @param board: The current state of the game board represented as a list of pieces.
    @type board: list[str]

    @return: A list of possible game board positions resulting from black moves.
    @rtype: list[list[str]]
    """
    # Swap 'W' and 'B' pieces in the board
    swapped_board = swap(board)

    # Generate a list of possible game board positions resulting from midgame or endgame moves
    black_position_list = generateMovesMidgameEndgame(swapped_board)

    # Generate a list of game board positions resulting from black moves with 'W' and 'B' pieces swapped
    return blackMoveList(black_position_list)



def fetch_input(args):
    """
    Fetch the input file name, output file name, and depth from the command-line arguments.

    @param args: The command-line arguments passed to the script.
    @type args: list[str]

    @return: A tuple containing the board positions, output file name, and depth.
    @rtype: tuple
    """
    # Check if the number of arguments is valid
    if len(args) == 1:
        exit("Error :: Please enter both input and output file names")

    # Extract the input and output file names from the arguments
    input_file = args[1]
    output_file = args[2]

    # Check if the depth is mentioned
    if len(args) != 4:
        exit("Error :: Depth not mentioned!")
    else:
        # Convert the depth argument to an integer
        depth = int(args[3])

    # Read the board positions from the input file
    with open(input_file, 'r') as file:
        board_pos = file.read()

    # Return the board positions as a list, output file name, and depth as a tuple
    return list(board_pos), output_file, depth



def get_result(final_output, output_file, positions_evaluated):
    """
    Display and store the final result, positions evaluated, and board position.

    @param final_output: The final output of the algorithm containing the MINIMAX estimate and board position.
    @type final_output: tuple[int, list[str]]
    @param output_file: The name of the output file where the board position will be stored.
    @type output_file: str
    @param positions_evaluated: The number of positions evaluated by the static estimation.
    @type positions_evaluated: int

    @return: None
    """
    # Extract the board position from the final output
    final_result_string = ''.join(final_output[1])

    # Print the board position, positions evaluated, and MINIMAX estimate
    print()
    print('Board Position:', final_result_string)
    print('Positions evaluated by Static Estimation:', positions_evaluated)
    print('MINIMAX estimate:', final_output[0])

    # Write the board position to the output file
    with open(output_file, 'w') as f:
        f.write(final_result_string)


