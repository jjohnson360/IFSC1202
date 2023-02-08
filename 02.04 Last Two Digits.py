number = int(input("Enter a number greater than zero: "))
if number > 0:
    last_two_digits = number % 100
    formatted_last_two_digits = "{:02d}".format(last_two_digits)
    print("Last two digits:", formatted_last_two_digits)
else:
    print("Enter a number.")
