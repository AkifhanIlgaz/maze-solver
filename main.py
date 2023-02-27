from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
    c1 = Cell(50, 50, 100, 100, win, has_left_wall=False)
    c2 = Cell(100, 100, 150, 150, win,
              has_left_wall=False, has_right_wall=False)
    c3 = Cell(200, 200, 250, 250, win)
    c1.draw()
    c2.draw()
    c3.draw()

    win.wait_for_close()


main()
