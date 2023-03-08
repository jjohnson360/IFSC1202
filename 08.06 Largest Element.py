values = input("Enter Values Separated by Spaces: ").split()
for i in range(len(values)):
    values[i] = int(values[i])

max_value = values[0]
max_index = 0
for i in range(1, len(values)):
    if values[i] > max_value:
        max_value = values[i]
        max_index = i

print("Largest Value:", max_value)
print("Index of Largest Value:", max_index)