def get_unit_index(unit, units_list):
    try:
        return units_list.index(unit) + 1
    except ValueError:
        print(f"{unit} is not valid")
        exit()

from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
to_unit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")

conversion_table = [line.strip().split("\t") for line in open("09.04 Conversion.txt")]
units_list = [row[0] for row in conversion_table]

from_unit_index = get_unit_index(from_unit, units_list)
to_unit_index = get_unit_index(to_unit, units_list)

multiplier = float(conversion_table[from_unit_index][to_unit_index])
result = round(from_value * multiplier, 7)

print(f"{from_value} {from_unit} => {result} {to_unit}")
