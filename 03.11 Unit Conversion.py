fromValue = float(input("Enter From Value: "))
fromUnit = input("Enter From Unit (in, ft, yd, mi): ")

if fromUnit not in ["in", "ft", "yd", "mi"]:
    print("FromUnit is not valid")
    exit()

toUnit = input("Enter To Unit (in, ft, yd, mi): ")

if toUnit not in ["in", "ft", "yd", "mi"]:
    print("ToUnit is not valid")
    exit()

multiplier = 1.0

if fromUnit == "in" and toUnit == "ft":
    multiplier = 1/12
elif fromUnit == "in" and toUnit == "yd":
    multiplier = 1/36
elif fromUnit == "in" and toUnit == "mi":
    multiplier = 1/63360
elif fromUnit == "ft" and toUnit == "in":
    multiplier = 12
elif fromUnit == "ft" and toUnit == "yd":
    multiplier = 1/3
elif fromUnit == "ft" and toUnit == "mi":
    multiplier = 1/5280
elif fromUnit == "yd" and toUnit == "in":
    multiplier = 36
elif fromUnit == "yd" and toUnit == "ft":
    multiplier = 3
elif fromUnit == "yd" and toUnit == "mi":
    multiplier = 1/1760
elif fromUnit == "mi" and toUnit == "in":
    multiplier = 63360
elif fromUnit == "mi" and toUnit == "ft":
    multiplier = 5280
elif fromUnit == "mi" and toUnit == "yd":
    multiplier = 1760

toValue = round(fromValue * multiplier, 7)

print((fromValue, fromUnit, toValue, toUnit))