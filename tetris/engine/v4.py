from tqdm import tqdm
import pandas as pd
from tetris.engine.grid import generate_grid

"""
Add pieces which result in minimum height and combine incoming pieces based on size
{"1": , "2": , "3": , "4": , "5":  }
"""


def search_location(g, label, current_piece, penalty_pieces):
    height_increase = float("inf")
    cells_occupied = None
    print('Label:', label)
    print('Shape', current_piece.shape)
    placed = False
    health = False
    no_cell_found = False
    cells_checked = 0
    ## Set a limit to the number of row to be evaluated
    max_rows = min(g.N, g.grid_height+5)
    # print('Max_rows to be evaluated:', max_rows)
    # Try to place the piece in the grid
    for row in range(g.N):
        for col in range(g.M):
            # Check if the cell is empty
            if g.grid[row][col] == '0':
                current_piece.start_point = [row, col]
                current_piece.set_cells()
                for orientation in current_piece.cells_occupied.keys():
                    # print('Pre check orientation:',orientation)
                    if healthcheck(current_piece, orientation, g, penalty_pieces):
                        cells_checked += 1
                        piece_height = max([cell[0] for cell in current_piece.cells_occupied[orientation]])
                        if piece_height < height_increase:
                            height_increase = piece_height
                            cells_occupied = current_piece.cells_occupied[orientation]
                            # print('Item placed')
                            placed = True
                            # print("Orientation", orientation)
                            # print("Height increase", height_increase)
                        else:
                            pass
                            # print('Height is more')
                            # print('Piece height:',piece_height)
                            # print('Current height:', height_increase)
                    else:
                        if not placed:
                            health = True
                            #print('Healthcheck failed')
                if cells_checked >= g.M:
                    break
                # if cells_occupied:
                #     g.place_the_piece(label, cells_occupied, height_increase)
                #     print("Item placed")
                #     return 1
            else:
                if not placed:
                    no_cell_found = True
                    #print('Cell is not empty')


    if cells_occupied:
        g.place_the_piece(label, cells_occupied, height_increase)
        print("Item placed")
        return 1
    else:
        if health:
            print('Health check voliation')
        if no_cell_found:
            print('No cell found')

    return 0


def healthcheck(current_piece, orientation, g, penalty_pieces):
    """"
    Validate the current piece orientation with the constraints
    """
    # Check if the piece is within the grid boundaries
    min_x, min_y, max_x, max_y = 0, 0, g.N - 1, g.M - 1
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        if current_x < min_x or current_x > max_x or current_y < min_y or current_y > max_y:
            # print("The piece is placed outside the grid")
            return False

    # Check if the piece is not placed on a forbidden cell or overlapping on an already placed piece
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        if g.grid[current_x][current_y] != '0':
            # print("The piece is placed either on a forbidden area or overlapping with another piece")
            return False

    # Check if the piece to not adjacent to a penalty piece
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        # Check cells on all sides - Lazy solution
        try:
            if g.grid[current_x][current_y - 1] in penalty_pieces[current_piece.label]:
                # print('Penalty')
                return False
        except:
            pass

        try:
            if g.grid[current_x - 1][current_y] in penalty_pieces[current_piece.label]:
                # print('Penalty')
                return False
        except:
            pass

        try:
            if g.grid[current_x][current_y + 1] in penalty_pieces[current_piece.label]:
                # print('Penalty')
                return False
        except:
            pass

        try:
            if g.grid[current_x + 1][current_y] in penalty_pieces[current_piece.label]:
                # print('Penalty')
                return False
        except:
            pass

    return True


def generate_simulation(input_file, output_file):
    g, tetrominoes, penalty_pieces, pieces_config = generate_grid(input_file)

    # Order the incoming items based on shape
    incoming_order = ['I', 'O', 'J', 'L', 'T', 'S', 'Z']
    # Piece placement
    score = 0
    for shape in incoming_order:
        print('Shape:',shape)
        for label in tqdm(pieces_config[shape], total=len(pieces_config[shape]), desc='Placing pieces'):
            g.score += search_location(g, label, tetrominoes[label], penalty_pieces)

    # g.display()
    print("Score:", g.score)
    pd.DataFrame(g.output).to_csv(output_file, sep=' ', index=False, header=False)



if __name__ == '__main__':
    generate_simulation()