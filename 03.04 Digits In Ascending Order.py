def is_ascending(number):
    first_digit = number // 100
    second_digit = (number // 10) % 10
    third_digit = number % 10
    if first_digit < second_digit and second_digit < third_digit:
        return "YES"
    else:
        return "NO"

number = int(input("Enter a number: "))
print(is_ascending(number))