from graphics import Point, Line


class Cell:
    def __init__(self,  window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True,
        self.visited = False
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        from_cell_center_x = (self.x1 + self.x2) / 2
        from_cell_center_y = (self.y1 + self.y2) / 2
        from_cell_center = Point(from_cell_center_x, from_cell_center_y)

        to_cell_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) / 2
        to_cell_center = Point(to_cell_center_x, to_cell_center_y)

        line = Line(from_cell_center, to_cell_center)

        if undo:
            self.window.draw_line(line, "gray")
        else:
            self.window.draw_line(line, "red")
