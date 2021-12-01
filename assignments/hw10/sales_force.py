"""
Name: Hannah Rahner
sales_force.py

Problem: write a class to encapsulate the data for a sales person

Certification of Authenticity
I certify that the assignment is entirely my own work. I attended CSL tutoring for this program
"""

from sales_person import SalesPerson


class SalesForce:
    """Create a SalesForce class which draws from the SalesPerson class"""
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as file:
            for info in file:
                info = info.split(", ")
                employee_id = int(info[0])
                name = info[1]
                sales = info[2]
                sales = sales.replace("\n", "")
                sales = sales.split(" ")
                employee_info = SalesPerson(employee_id, name)
                for sale in sales:
                    employee_info.enter_sale(float(sale))
                self.sales_people.append(employee_info)

    def quota_report(self, quota):
        quota_list = []
        for i in self.sales_people:
            employee = []
            employee.append(i.get_id())
            employee.append(i.get_name())
            total = i.total_sales()
            employee.append(total)
            employee.append(i.met_quota(quota))
            quota_list.append(employee)
        return quota_list

    def top_seller(self):
        top_employee = []
        max_value = 0
        for i in self.sales_people:
            if i.total_sales() > max_value:
                max_value = i.total_sales()
        for j in self.sales_people:
            if j.total_sales() == max_value:
                top_employee.append(j)
        return top_employee

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if i.get_id() == employee_id:
                return i
        return None
