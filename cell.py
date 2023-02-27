from graphics import Point, Line


class Cell:
    def __init__(self,  x1, y1, x2, y2, window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True,):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.window = window

    def draw(self):
        if self.has_left_wall:
            self.window.draw_line(Line(Point(self.x1, self.y1),
                                       Point(self.x1, self.y2)), "black")

        if self.has_right_wall:
            self.window.draw_line(Line(Point(self.x2, self.y1),
                                       Point(self.x2, self.y2)), "black")

        if self.has_top_wall:
            self.window.draw_line(Line(Point(self.x1, self.y1),
                                       Point(self.x2, self.y1)), "black")

        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(self.x1, self.y2),
                                       Point(self.x2, self.y2)), "black")
