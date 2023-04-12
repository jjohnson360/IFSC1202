class Employee:
    def __init__(self, first_name, last_name, id_number, hours_worked, wage):
        self.FirstName = first_name
        self.LastName = last_name
        self.IDNumber = id_number
        self.HoursWorked = hours_worked
        self.Wage = wage

    def WeeklyPay(self):
        if self.HoursWorked > 40:
            regular_pay = 40 * self.Wage
            overtime_pay = (self.HoursWorked - 40) * (self.Wage * 1.5)
            return round(regular_pay + overtime_pay, 2)
        else:
            return round(self.HoursWorked * self.Wage, 2)

print(f"{'First':>8} {'Last':>8} {'ID':>8} {'Hours':>8} {'Hourly':>8} {'Weekly':>8}")
print(f"{'Name':>8} {'Name':>8} {'Number':>8} {'Worked':>8} {'Wage':>8} {'Pay':>8}")

with open("10.06 Payroll.txt", "r") as file:
    for line in file:
        employee_data = line.strip().split(",")
        first_name, last_name, id_number, hours_worked, wage = employee_data
        employee = Employee(first_name, last_name, id_number, int(hours_worked), float(wage))
        weekly_pay = employee.WeeklyPay()
        print(f"{employee.FirstName:>8} {employee.LastName:>8} {employee.IDNumber:>8} {employee.HoursWorked:>8.2f} {employee.Wage:>8.2f} {weekly_pay:>8.2f}")
