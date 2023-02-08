first_number = input("Enter first 2 digit number: ")
second_number = input("Enter second 2 digit number: ")

merged_number = int(first_number[0] + second_number[0] + first_number[1] + second_number[1])

output = "Merged number: {}".format(merged_number)

print(output)