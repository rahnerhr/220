"""
Name: Hannah Rahner
mean.py

Problem: Create a program that calculates  root mean square average, harmonic
mean, and geometric mean

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""
# HW #3 Questions:

# 1: The program will evaluate three different methods for calculating the mean.

# 2: The user will input a variety of numbers when prompted, and the program will output
# three different averages: rms, harmonic, and geometric; calculated from their
# respective formulas. In order to test the program the user will input 4 numbers
# with values: 10,5,2, and 5 this should yield 6.205, 4.0, ad 4.729, respectively.

# 3: First the program will prompt the user to enter a variety of numbers.
# The program will then apply these numbers to each of the formulas. It will be easier
# if the loop dependent part of the equations are simplified into new variable names.
# Then, you can call the variables in the loop when coding the formulas (outside the loop)
# for each mean (rms, harmonic, and geometric). Lastly, we will ask the program to print the
# solutions for each equation to the screen and also round each variable to three
# decimal places.

import math

def main():

# prompt user to input a number of values
    number_of_values = eval(input("How many numbers would you like to average? "))

# initial conditions needed for loop:
    sum_rms = 0
    sum_harmonic = 0
    geometric = 1

    for value in range(number_of_values):
        value = eval(input("Enter Value:"))

# assign variables to the loop dependent aspects of the equations:
        sum_rms += value ** 2
        sum_harmonic += 1 / value
        geometric = geometric * value


# mean formulas
    average_rms = math.sqrt(sum_rms / number_of_values)
    print(round(average_rms,3))

    average_harmonic = number_of_values / sum_harmonic
    print(round(average_harmonic,3))

    average_geometric = (geometric)**(1/number_of_values)
    print(round(average_geometric,3))
