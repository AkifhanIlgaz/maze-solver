from cell import Cell
import time


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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        self.cells = [0] * self.num_cols

        for i in range(len(self.cells)):
            self.cells[i] = [Cell(self.window)] * self.num_rows

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
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows -
                                      1].has_bottom_wall = False

        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
