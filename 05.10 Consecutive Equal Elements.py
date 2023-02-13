numbers = []
num = int(input("Enter a Number (zero to quit): "))
while num != 0:
    numbers.append(num)
    num = int(input("Enter a Number (zero to quit): "))

if len(numbers) == 0:
    print("Sequence Length is 0")
else:
    max_count = 1
    max_num = numbers[0]
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            count += 1
            if count > max_count:
                max_count = count
                max_num = numbers[i]
        else:
            count = 1
    print("", max_num, "Repeated", max_count, "Times")