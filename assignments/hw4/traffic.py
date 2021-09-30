"""
Name: Hannah Rahner
traffic.py

Problem: Create a program for the DOT that analyzes traffic patterns

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""

# Problem: we know we are going to need two loops, one to loop each road
# and one to loop for the days the road the was surveyed

def main():
    total_roads = eval(input("How many roads were surveryed? "))
    total = 0

    for total_roads in range(1, total_roads + 1):
        total_days = eval(input("How many days was road " + str(total_roads) + " surveyed? "))
        total_traffic = 0

        for total_days in range(1, total_days + 1):
            cars = eval(input("How many cars travelled on day " + str(total_days) + "? "))
            total = total + cars
            total_traffic = cars + total_traffic

        average_cars_per_road = round((total_traffic / total_days),2)
        print("Road " + str(total_roads) + " average vehicles per day:", average_cars_per_road)

    avg_total_cars = round((total / total_roads),2)

    print("The total number of vehicles on all roads is:", total)
    print("The average number of vehicles per road is:", round(avg_total_cars,2))
