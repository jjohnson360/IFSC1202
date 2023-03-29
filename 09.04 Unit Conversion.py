FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (mm, cm, m, km, in, ft, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, ft, yd, mi): ")

with open("09.04 Conversion.txt") as f:
    lines = f.readlines()

conv_table = []
for line in lines:
    conv_table.append(line.strip().split())

from_unit_row_index = None
for i in range(1, len(conv_table)):
    if FromUnit == conv_table[i][0]:
        from_unit_row_index = i
        break

if from_unit_row_index is None:
    print("FromUnit is not valid")
    exit()

to_unit_col_index = None
for j in range(1, len(conv_table[0])):
    if ToUnit == conv_table[0][j]:
        to_unit_col_index = j
        break

if to_unit_col_index is None:
    print("ToUnit is not valid")
    exit()

multiplier = float(conv_table[from_unit_row_index][to_unit_col_index])
result = round(FromValue * multiplier, 7)

print(FromValue, FromUnit, "=>", result, ToUnit)