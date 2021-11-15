"""
Name: Hannah Rahner
factorial.py

Problem: Calculate factorials

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""
import math
def main():
    print("This calculates the factorial of a number")
    num = eval(input("enter a value: "))
    acc = 1
    for n in range(num,1,-1):
        acc = acc * n
    print(acc)

main()
