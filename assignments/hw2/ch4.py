"""
Name: Hannah Rahner
ch4.py

Problem: Chapter 4 materials

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""
# import graphics
from graphics import GraphWin,Point, Circle
def main():
    win = GraphWin("Window 1", 700, 500)

    pointA = Point(250,250)

    circleA = Circle(pointA,50)
    circleA.setFill("red")


    circleB = circleA.clone()
    circleB.move(200,0)

#draw
    circleA.draw(win)
    circleB.draw(win)

    mouse_event = win.getMouse()
    print(mouse_event)

main()
