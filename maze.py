from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []

        if seed:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)

    def create_cells(self):
        for i in range(self.num_cols):
            column_cells = []
            for j in range(self.num_rows):
                column_cells.append(Cell(self.window))
            self.cells.append(column_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        cell_x1 = self.x1 + i * self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y

        self.cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(0.005)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows -
                                      1].has_bottom_wall = False

        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            possible_visiting_cells = []
            possible_directions = 0

            # Check left neighbor
            if i > 0 and self.cells[i-1][j].visited == False:
                possible_visiting_cells.append((i-1, j))
                possible_directions += 1

            # Check right neighbor
            if i < self.num_cols - 1 and self.cells[i+1][j].visited == False:
                possible_visiting_cells.append((i+1, j))
                possible_directions += 1

            # Check top neighbor
            if j > 0 and self.cells[i][j-1].visited == False:
                possible_visiting_cells.append((i, j-1))
                possible_directions += 1

            # Check bottom neighbor
            if j < self.num_rows - 1 and self.cells[i][j+1].visited == False:
                possible_visiting_cells.append((i, j+1))
                possible_directions += 1

            if possible_directions == 0:
                self.draw_cell(i, j)
                return

            direction = random.randrange(possible_directions)
            next_cell = possible_visiting_cells[direction]

            # left
            if next_cell[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False

            # right
            if next_cell[0] == i+1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False

            # up
            if next_cell[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # down
            if next_cell[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False

            self.break_walls_r(next_cell[0], next_cell[1])

    def reset_cells_visited(self):
        for column in self.cells:
            for cell in column:
                cell.visited = False
