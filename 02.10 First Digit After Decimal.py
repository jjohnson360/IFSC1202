import math

number = float(input("Enter number: "))

fractional_part = number - math.floor(number)

first_digit = int(fractional_part * 10)

print("Tenths value:", first_digit)