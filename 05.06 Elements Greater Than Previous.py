count = 0
previous = None

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    if previous is not None and number > previous:
        count += 1
    previous = number

print("Number of Values Greater Than the Previous:", count)