"""
Name: Hannah Rahner
threeDoorsGame.py

Problem: uses class, instance variables, and constructors and pull this class to another
program threeDoorGame.py

Certification of Authenticity
I certify that the assignment is entirely my own work. Attended the CSL for tutoring and contacted
TA Ashley Woods for assistance
"""

from graphics import GraphWin, Point, Text, Rectangle
from button import Button
from random import randint


def main():
    # create graphics window
    win = GraphWin("Three Button Game", 600, 600)

    # draw the labels first, so they are not covered by the color of rectangles
    text_one = "Door 1"
    text_two = "Door 2"
    text_three = "Door 3"

    # create rectangles
    rec_one = Rectangle(Point(50, 250), Point(150, 350))
    rec_two = Rectangle(Point(250, 250), Point(350, 350))
    rec_three = Rectangle(Point(450, 250), Point(550, 350))

    # use the button class and draw to the window
    button_one = Button(rec_one, text_one)
    button_one.draw(win)

    button_two = Button(rec_two, text_two)
    button_two.draw(win)

    button_three = Button(rec_three, text_three)
    button_three.draw(win)

    # insert the text at the top and bottom of the window
    top_text = Text(Point(300, 100), "I have a secret door")
    top_text.setSize(20)
    top_text.draw(win)

    bottom_text = Text(Point(300, 550), "Click to choose my door.")
    bottom_text.setSize(15)
    bottom_text.draw(win)

    # create a random secret door using the randint from random
    door = randint(1, 3)
    click = win.getMouse()

    # create the button conditions
    if button_one.is_clicked(click):
        if door == 1:
            button_one.set_label("Door 1")
            button_one.color_button("lime")
            top_text.setText("You Win!")
        else:
            button_one.set_label("Door 1")
            button_one.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(door) + " is my secret door")

    elif button_two.is_clicked(click):
        if door == 2:
            button_one.set_label("Door 2")
            button_two.color_button("lime")
            top_text.setText("You Win!")
        else:
            button_two.set_label("Door 2")
            button_two.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(door) + " is my secret door")

    elif button_three.is_clicked(click):
        if door == 3:
            button_three.set_label("Door 3")
            button_three.color_button("lime")
            top_text.setText("You Win!")
        else:
            button_three.set_label("Door 3")
            button_three.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(door) + " is my secret door")

    # displaying the closing message
    bottom_text.setText("Click anywhere to close")

    win.getMouse()
    win.close()

main()