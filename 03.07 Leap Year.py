def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "LEAP YEAR"
    else:
        return "COMMON YEAR"

year = int(input("Enter year: "))
print(is_leap_year(year))