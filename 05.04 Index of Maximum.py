largest = 0
index = 0
max_index = 0

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    index += 1
    if largest is None or number > largest:
        largest = number
        max_index = index

print("Maximum:", largest)
print("Index of Maximum:", max_index)