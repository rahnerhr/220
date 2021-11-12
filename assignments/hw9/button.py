"""
Name: Hannah Rahner
button.py

Problem: uses class, instance variables, and constructors and pull this class to another
program threeDoorGame.py

Certification of Authenticity
I certify that the assignment is entirely my own work. I attended CSL tutoring for this program and
contacted TA Ashley Woods
"""

from graphics import Text


class Button:
    """This class creates a button that will be manipulated in the Three Doors Game"""

    def __init__(self, shape, text):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), text)
        self.text.setSize(15)
        self.drawn = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, text):
        return self.text.setText(text)

    def color_button(self, color):
        self.shape.setFill(color)

    def draw(self, win):
        if not self.drawn:
            self.shape.draw(win)
            self.text.draw(win)
            self.drawn = True

    def undraw(self):
        if self.drawn:
            self.shape.undraw()
            self.text.undraw()
            self.drawn = False

    def is_clicked(self, point):
        x_1 = point.getX()
        y_1 = point.getY()

        boundary_left = self.shape.getP1()
        left_x = boundary_left.getX()
        left_y = boundary_left.getY()

        boundary_right = self.shape.getP2()
        right_x = boundary_right.getX()
        right_y = boundary_right.getY()

        if (left_x <= x_1 <= right_x) and (left_y <= y_1 <= right_y):
            return True
        return False
