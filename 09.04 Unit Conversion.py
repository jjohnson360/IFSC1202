
from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
to_unit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")

# Read conversion table from file and store in a 2D list
conversion_table = []
with open("09.04 Conversion.txt") as file:
    for line in file:
        conversion_table.append(line.strip().split("\t"))

# Find the index of the from_unit and to_unit in the table
from_unit_index = -1
to_unit_index = -1
for i in range(1, len(conversion_table)):
    if conversion_table[i][0] == from_unit:
        from_unit_index = i
    if conversion_table[0][i] == to_unit:
        to_unit_index = i

# Check if from_unit and to_unit are valid
if from_unit_index == -1:
    print("FromUnit is not valid")
    exit()
if to_unit_index == -1:
    print("ToUnit is not valid")
    exit()

# Perform unit conversion
multiplier = float(conversion_table[from_unit_index][to_unit_index])
result = round(from_value * multiplier, 7)

# Print result
print(f"{from_value} {from_unit} => {result} {to_unit}")
