count = 0
sum = 0
minimum = float('inf')
maximum = float('-inf')

while True:
    num = float(input("Enter a Value (zero to quit): "))
    if num == 0:
        break

    count += 1
    sum += num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

if count == 0:
    print("No data was entered")
else:
    average = sum / count
    print("Count:", count)
    print("Sum:", sum)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)