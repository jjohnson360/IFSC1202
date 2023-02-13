largest = None

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    if largest is None or number > largest:
        largest = number

if largest is None:
    print("No numbers were entered.")
else:
    print("Maximum:", largest)