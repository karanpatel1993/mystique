from tetris.engine.grid import generate_grid


def search_location(g, label, current_piece, penalty_pieces):
    # Try to place the piece in the grid
    for row in range(g.N):
        for col in range(g.M):
            current_piece.start_point = [row, col]
            print('Start point:', current_piece.start_point)
            current_piece.set_cells()
            for orientation in current_piece.cells_occupied.keys():
                if healthcheck(current_piece, orientation, g, penalty_pieces):
                    g.place_the_piece(label, current_piece.cells_occupied[orientation])
                    return
    return


def healthcheck(current_piece, orientation, g, penalty_pieces):
    """"
    Validate the current piece orientation with the constraints
    """
    # Check if the piece is within the grid boundaries
    min_x, min_y, max_x, max_y = 0, 0, g.N - 1, g.M - 1
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        if current_x < min_x or current_x > max_x or current_y < min_y or current_y > max_y:
            print("The piece is placed outside the grid")
            return False

    # Check if the piece is not placed on a forbidden cell or overlapping on an already placed piece
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        if g.grid[current_x][current_y] != '0':
            print("The piece is placed either on a forbidden area or overlapping with another piece")
            return False

    # Check if the piece to not adjacent to a penalty piece
    for cell in current_piece.cells_occupied[orientation]:
        current_x, current_y = cell
        # Check cells on all sides - Lazy solution
        try:
            if g.grid[current_x][current_y - 1] in penalty_pieces[current_piece.label]:
                return False
        except:
            pass

        try:
            if g.grid[current_x - 1][current_y] in penalty_pieces[current_piece.label]:
                return False
        except:
            pass

        try:
            if g.grid[current_x][current_y + 1] in penalty_pieces[current_piece.label]:
                return False
        except:
            pass

        try:
            if g.grid[current_x + 1][current_y] in penalty_pieces[current_piece.label]:
                return False
        except:
            pass

    return True


def generate_simulation():
    g, tetrominoes, penalty_pieces = generate_grid()
    print(g.grid)
    print(tetrominoes)

    # Sample piece placement
    for label in tetrominoes:
        # search_location(g, tetrominoes[label].shape, tetrominoes[label], penalty_pieces)
        # g.display()
        search_location(g, label, tetrominoes[label], penalty_pieces)
        g.display()



if __name__ == '__main__':
    generate_simulation()