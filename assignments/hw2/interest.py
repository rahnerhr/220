"""
Name: Hannah Rahner
interest.py

Problem: Write a program that computes the monthly interest charge on a credit card account.
Include annual interest rate,number of days in billing cycle, previous balance,
payment amount, and day of the billing cycle the in which the payment was made

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""

def main():
    # User Input Section
    air = input("enter a number between 1 and 100:")
    # step two: users enter the number of days in the billing cycle; variable = days
    month_days = input("enter the number of days in billing month:")
    # step three: users enter the previous balance; variable = principal
    principal = input("enter the previous balance from the credit card statement:")
    # step four: users enter the payment amount; variable = payment
    payment = input("enter the amount paid on the credit card:")
    # step five: users enter the day of the month in which payment was made; variable = payment_day
    payment_day = input("enter the day of the month in which the payment was made:")

    a_1 = float(principal) * float(month_days)
    b_1 = float(payment) * (float(month_days)-float(payment_day))
    c_1 = float(a_1) - float(b_1)
    avg_daily_balance = c_1 / float(month_days)
    monthly_interest_rate = float(air) / 12
    total_monthly_interest = avg_daily_balance * (monthly_interest_rate/100)
    print(round(total_monthly_interest,2))
