count = 0

while True:
    number = int(input("Enter a Number (zero to quit): "))
    if number == 0:
        break
    if number % 2 == 0:
        count += 1

print("Number of Even Values:", count)