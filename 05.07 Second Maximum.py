first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))

first_max = max(first_num, second_num)
second_max = min(first_num, second_num)

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number > first_max:
        second_max = first_max
        first_max = number
    elif number > second_max:
        second_max = number

print("First Maximum:", first_max)
print("Second Maximum:", second_max)