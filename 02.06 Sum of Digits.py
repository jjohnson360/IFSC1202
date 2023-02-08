number = int(input("Enter a three-digit number: "))

if number >= 100 and number < 1000:
    units_digit = number % 10
    tens_digit = (number // 10) % 10
    hundreds_digit = (number // 100)
    sum_of_digits = units_digit + tens_digit + hundreds_digit
    output = "Sum of the digits {}".format(sum_of_digits)

    print(output)