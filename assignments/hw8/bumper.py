"""
Name: Hannah Rahner
bumper.py

Problem: bumper car simulation

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""

from random import randint, randrange
from math import sqrt
from graphics import GraphWin, Circle, Point, Text


def get_random(move_amount):
    start = move_amount * -1
    stop = move_amount
    return randint(start, stop)


# returns Boolean based on the collision of the two balls
def did_collide(ball, ball_two):
    point_one = ball.getCenter()
    point_two = ball_two.getCenter()
    x_1 = point_one.getX()
    x_2 = point_two.getX()
    y_1 = point_one.getY()
    y_2 = point_two.getY()
# used the distance formula
    distance = sqrt(((x_1 - x_2) ** 2) + (y_1 - y_2) ** 2)

    r_1 = ball.getRadius()
    r_2 = ball_two.getRadius()
    total_radius = r_1 + r_2

    if distance > total_radius:
        return False
    else:
        return True


# returns True if ball hits the top or bottom of the window wall, False otherwise
def hit_vertical(ball, win):
    point = ball.getCenter()
    x_1 = point.getX()
    r_1 = ball.getRadius()
    if x_1 + r_1 >= 400:
        return True
    elif x_1 - r_1 <= 0:
        return True
    else:
        return False


# returns True if ball hits the left of right of the window, False otherwise
def hit_horizontal(ball, win):
    point = ball.getCenter()
    y_1 = point.getY()
    r_1 = ball.getRadius()
    if y_1 + r_1 >= 400:
        return True
    elif y_1 - r_1 <= 0:
        return True
    else:
        return False


def get_random_color():
    colors = ["red", "orange", "yellow", "lime", "aqua", "fuchsia", "pink"]
    random_color = colors[randrange(7)]
    return random_color


def main():
    win = GraphWin("Bumper Car Simulation", 400, 400)
    win.setBackground("white")

    ball = Circle(Point(10, 20), 10)
    ball2 = Circle(Point(110, 120), 10)

    ball.draw(win)
    ball2.draw(win)

    ball.setFill(get_random_color())
    ball2.setFill(get_random_color())

    x_move = get_random(10)
    y_move = get_random(10)
    x_2_move = get_random(10)
    y_2_move = get_random(10)

# different collision options and how the ball should react
    runs = 0
    while runs < 500:

        ball.move(x_move, y_move)
        ball2.move(x_2_move, y_2_move)

        if did_collide(ball, ball2):
            x_move = x_move * -1
            y_move = y_move * -1
            x_2_move = x_2_move * -1
            y_2_move = y_2_move * -1
            ball.setFill(get_random_color())
            ball2.setFill(get_random_color())

        if hit_vertical(ball, win):
            x_move = x_move * -1
            ball.setFill(get_random_color())

        if hit_horizontal(ball, win):
            y_move = y_move * -1
            ball.setFill(get_random_color())

        if hit_vertical(ball2, win):
            x_2_move = x_2_move * -1
            ball2.setFill(get_random_color())

        if hit_horizontal(ball2, win):
            y_2_move = y_2_move * -1
            ball2.setFill(get_random_color())

        runs = runs + 1

# closing message
    close = Text(Point(200, 350), "Click anywhere to close")
    close.setTextColor("black")
    close.draw(win)

    win.getMouse()
    win.close()

main()