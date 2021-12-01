"""
Name: Hannah Rahner
sales_person.py

Problem: write a class to encapsulate the data of a sales person

Certification of Authenticity
I certify that the assignment is entirely my own work. I attended CSL tutoring for this program
"""


class SalesPerson:
    """ Write a class to encapsulate the data for a sales person """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = str(new_name)

    def enter_sale(self, new_sale):
        self.sales.append(new_sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            total += self.sales[i]
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other_employee):
        if self.total_sales() < other_employee.total_sales():
            value = -1
        elif self.total_sales() > other_employee.total_sales():
            value = 1
        else:
            value = 0
        return value

    def __str__(self):
        output = str(self.employee_id) + "-"
        output += str(self.name) + ":"
        output += str(self.total_sales())
        return output
