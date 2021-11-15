"""
Name: Hannah Rahner
hello.py

Problem: print hello, world! to the screen

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""


def main():
    print("This program illustrates a chaotic function")
    # this is where users enter a value
    x = eval(input("enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)


main()


