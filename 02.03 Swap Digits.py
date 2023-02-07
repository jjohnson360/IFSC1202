number = int(input("Enter a two-digit number: "))

first_digit = number // 10

second_digit = number % 10

new_number = second_digit * 10 + first_digit

print("Swapped number:", new_number)