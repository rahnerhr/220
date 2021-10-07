"""
Name: Hannah Rahner
greetings.py

Problem: Create a program that displays an animation of a heart with an arrow
going through it.

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""

from graphics import *

def main():
    win = GraphWin("Valentine's Day Greeting", 600, 600)
    win.setBackground("pink")

    heart = Polygon(Point(300,125), Point(350,75), Point(425,75),
                    Point(475,125), Point(475,200), Point(300, 375),
                    Point(125, 200), Point(125, 125), Point(175, 75),
                    Point(250, 75), Point(300, 125))

    heart.setFill("red")
    heart.setOutline("white")
    heart.draw(win)

    message_location = Point(win.getWidth() - 300, win.getHeight() - 100)
    message = Text(message_location, "HAPPY VALENTINE'S DAY!!")
    message.setFace("times roman")
    message.setSize(35)
    message.setTextColor("white")
    message.draw(win)

    heart_message_location = Point(win.getWidth() - 300, win.getHeight() - 380)
    heart_message = Text(heart_message_location, "BE MINE")
    heart_message.setSize(30)
    heart_message.setFace("times roman")
    heart_message.setTextColor("white")
    heart_message.draw(win)

    arrow = Line(Point(10,470), Point(70,440))
    arrow.setArrow("last")
    arrow.draw(win)

    for i in range(20):
        arrow.move(25,-25)
        time.sleep(.25)

    closing_message_location = Point(win.getWidth()-300, win.getHeight()-50)
    closing_message = Text(closing_message_location, "Click anywhere to close")
    closing_message.setSize(15)
    closing_message.setFace("times roman")
    closing_message.setTextColor("white")
    closing_message.draw(win)

    win.getMouse()

main()
