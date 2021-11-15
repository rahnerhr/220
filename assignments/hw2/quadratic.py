"""
Name: Hannah Rahner
quadratic.py

Problem: Calculate the roots of a quadratic function

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""
import math


def main():
    print("This program calculate the roots of a quadratic function")
    a, b, c = eval(input("enter the coefficients a,b,and c:"))
    root_disc = math.sqrt((math.pow(b, 2)) - 4 * a * c)  # dot notation
    den = 2 * a
    root1 = ((-b) + (root_disc)) / den
    root2 = ((-b) - (root_disc)) / den
    print("the roots are", root1, root2)


main()
