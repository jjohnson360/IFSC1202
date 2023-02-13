max_value = 0
count = 0

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    if number > max_value:
        max_value = number
        count = 1
    elif number == max_value:
        count += 1

print("Maximum:", max_value)
print("Number of Occurrences", count,)