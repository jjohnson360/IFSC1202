sum = 0
count = 0

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    sum += number
    count += 1

if count == 0:
    print("Sequence Length is 0")
else:
    average = sum / count
    print("The average of the numbers is:", average)