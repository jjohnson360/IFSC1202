import math

number = float(input("Enter a number: "))

fractional_part = number - math.floor(number)
result = round(fractional_part, 10)

print("Fractional part:", result)