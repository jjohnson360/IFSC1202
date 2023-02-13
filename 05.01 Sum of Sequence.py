sum = 0

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    sum += number

print("Sum:", sum)