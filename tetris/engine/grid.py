from collections import defaultdict
from tetris.components.structures import Grid, Piece

def generate_grid():
    # Create placeholders
    tetrominoes = dict()
    penalty_pieces = defaultdict(list)

    # Read input file
    with open('Problems/Problem5.txt','r') as f:
        input_params = f.read().split('\n')
        M,N = [int(i) for i in input_params[1].split(' ')]
        pieces = input_params[input_params.index('PIECES') + 1 : input_params.index('FORBIDDEN')]
        forbidden = input_params[input_params.index('FORBIDDEN') + 1 : input_params.index('PENALTY')]
        penalty = input_params[input_params.index('PENALTY') + 1 : -1]
        # print(M,N)
        # print(pieces)
        # print(forbidden)
        # print(penalty)

        # Generate Grid object
        g = Grid(M=M, N=N)

        # Set forbidden cells
        for cell in forbidden:
            g.set_forbidden_cells(cell.split(','))

        # Generate pieces
        for t_piece in pieces:
            label, shape = t_piece.split(' ')
            tetrominoes[label] = Piece(label=label, shape=shape)

        # Generate penalty pairs
        for pairs in penalty:
            s,d = pairs.split(' ')
            penalty_pieces[s].append(d)
            penalty_pieces[d].append(s)

    # print(penalty_pieces)
    return g, tetrominoes, penalty_pieces


if __name__ == '__main__':
    generate_grid()