import sys
import utilities
import MiniMaxGame as MMG

if __name__ == '__main__':

    input_board, output_file, depth = utilities.fetch_input(sys.argv)

    positions = []
    positions = MMG.MiniMax(utilities.swap(input_board), depth, positions, True)

    utilities.get_result(positions, output_file, utilities.positions_evaluated)
