"""
Name: Hannah Rahner
weighted_average.py

Problem: develop a program that uses data from a text file

Certification of Authenticity
I certify that the assignment is entirely my own work.
I did attend CSCI tutoring in the CSL for this assignment
"""

def weighted_average(in_file_name, out_file_name):
    in_file_name = open(in_file_name, "r")
    lines = in_file_name.readlines()
    out_file_name = open(out_file_name, "w")
    final_average = []

# format the txt file
    for i in lines:
        values = i.split(": ")
        names = values[0]
        weights_and_grades = values[1]
        weights_and_grades = weights_and_grades.split(" ")
        weights_and_grades[len(weights_and_grades)-1] = weights_and_grades[len(weights_and_grades)-1].strip("\n")

# convert the second part of the string to ints
        sum_weights = 0
        for j in range(len(weights_and_grades)):
            weights_and_grades[j] = int(weights_and_grades[j])

# set up the stepping for weights and grades
        weights = weights_and_grades[0::2]
        grades = weights_and_grades[1::2]

# sum the weights
        for k in range(len(weights)):
            sum_weights += weights[k]

# sum the grades
        sum_grades = 0
        for l in range(len(grades)):
            sum_grades += grades[l]

# create if statements for when sum weights is <, >, = 100 and calculate student's average
        if sum_weights < 100:
            error_output_one = (names + "'s average: " + "Error: The weights are less than 100." + "\n")
            out_file_name.write(error_output_one)
        if sum_weights > 100:
            error_output_two = (names + "'s average: " + "Error: The weights are more than 100." + "\n")
            out_file_name.write(error_output_two)
        if sum_weights == 100:
            average = 0
            for avg in range(len(weights)):
                average += (weights[avg] * grades[avg])
            average = round((average / 100), 1)
            final_average.append(average)
            output_students = names + "'s average: " + str(average) + "\n"
            out_file_name.write(output_students)

# calculate class average and write to new file
    class_average = sum(final_average) / len(final_average)
    output_class = "Class average: " + str(round(class_average, 1))
    out_file_name.write(output_class)

# call the function
def main():
    weighted_average("grades.txt", "avg.txt")

main()
