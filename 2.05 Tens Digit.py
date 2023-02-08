number = int(input("Enter a number: "))

tens_digit = (number // 10) % 10

output = "Tens digit of {} is: {}".format(number, tens_digit)

print(output)