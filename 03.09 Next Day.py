month = int(input("Enter month: "))
day = int(input("Enter day: "))

if (month == 12 and day == 31):
    month = 1
    day = 1
elif (month in [1, 3, 5, 7, 8, 10] and day == 31) or (month == 2 and day == 28) or (month in [4, 6, 9, 11] and day == 30):
    month += 1
    day = 1
else:
    day += 1

print("Next day", month, "/", day)