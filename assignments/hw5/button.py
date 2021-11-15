from graphics import GraphWin, Rectangle, Point, Text

def draw_button(button_text, point_one, point_two, win):
    outline = Rectangle(point_one, point_two)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)

    label.draw(win)

def main():
    win = GraphWin("test button", 700, 500)
    win.setCoord(0,0,10,10)

    draw_button("Button One", Point(2,1), Point(4,3),win)
    draw_button("Button Two", Point(6,1), Point(8,3), win)

