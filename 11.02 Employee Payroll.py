class Employee:
    def __init__(self, first, last, id_num, wage):
        self.FirstName = first
        self.LastName = last
        self.IDNumber = id_num
        self.Wage = wage
        self.HoursWorked = 0

    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked * self.Wage
        else:
            overtime = self.HoursWorked - 40
            return (40 * self.Wage) + (overtime * self.Wage * 1.5)

def find_employee(employees, id_num):
    for i in range(len(employees)):
        if employees[i].IDNumber == id_num:
            return i
    return -1

employees = []
with open("11.02 Employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        employee = Employee(data[0], data[1], int(data[2]), float(data[3]))
        employees.append(employee)

with open("11.02 Hours.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        id_num = int(data[0])
        hours = float(data[1])
        index = find_employee(employees, id_num)
        if index != -1:
            employees[index].HoursWorked += hours

print(" First     Last      ID   Hours  Hourly   Weekly")
print("  Name     Name  Number  Worked    Wage      Pay")
for employee in employees:
    weekly_pay = round(employee.WeeklyPay(), 2)
    print(f"{employee.FirstName:>6} {employee.LastName:>8} {employee.IDNumber:>7} {employee.HoursWorked:>7} {employee.Wage:>7} {weekly_pay:>8}")
