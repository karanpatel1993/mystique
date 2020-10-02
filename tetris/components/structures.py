class Grid:
    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.grid = [['0' for m in range(M)] for n in range(N)]
        self.forbidden_cells = None
        self.score = 0

    def set_forbidden_cells(self, cell):
        y,x = [int(i) for i in cell]
        self.grid[x][y] = '-1'    # set -1 for cells which are forbidden

    def place_the_piece(self, label, cells):
        for point in cells:
            place_x, place_y = point
            self.grid[place_x][place_y] = label

    def display(self):
        for row in self.grid:
                print(row)

    def generate_score(self):
        pass


class Piece:
    def __init__(self, label, shape):
        self.label = label
        self.shape = shape
        self.start_point = None
        self.orientation = None
        self.cells_occupied = None

    def set_cells(self):
        x,y = self.start_point
        if self.shape == 'I':
            self.cells_occupied = {'1': [(x, y), (x, y+1), (x, y+2), (x, y+3)],
                                    '2': [(x, y), (x+1, y), (x+2, y), (x+3, y)]
                                   }
        elif self.shape == 'O':
            self.cells_occupied = {'1': [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
                                   }
        elif self.shape == 'T':
            self.cells_occupied = {'1': [(x, y), (x, y+1), (x, y+2), (x+1, y+1)],
                                   '2': [(x, y), (x+1, y), (x+2, y), (x+1, y-1)],
                                   '3': [(x, y), (x, y+1), (x, y+2), (x-1, y+1)],
                                   '4': [(x, y), (x-1, y), (x-2, y), (x-1, y+1)]
                                   }
        elif self.shape == 'J':
            self.cells_occupied = {'1': [(x, y), (x+1, y), (x+2, y), (x+2, y-1)],
                                   '2': [(x, y), (x, y-1), (x, y-2), (x-1, y-2)],
                                   '3': [(x, y), (x-1, y), (x-2, y), (x-2, y+1)],
                                   '4': [(x, y), (x, y+1), (x, y+2), (x+1, y+2)]
                                   }
        elif self.shape == 'L':
            self.cells_occupied = {'1': [(x, y), (x+1, y), (x+2, y), (x+2, y+1)],
                                   '2': [(x, y), (x, y-1), (x, y-2), (x+1, y-2)],
                                   '3': [(x, y), (x-1, y), (x-2, y), (x-2, y-1)],
                                   '4': [(x, y), (x, y+1), (x, y+2), (x-1, y+2)]
                                   }
        elif self.shape == 'S':
            self.cells_occupied = {'1': [(x, y), (x, y-1), (x+1, y-1), (x+1, y-2)],
                                   '2': [(x, y), (x-1, y), (x-1, y-1), (x-2, y-1)]
                                   }
        elif self.shape == 'Z':
            self.cells_occupied = {'1': [(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)],
                                   '2': [(x, y), (x+1, y), (x+1, y-1), (x+2, y-1)]
                                   }