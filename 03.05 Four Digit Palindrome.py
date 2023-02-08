def is_palindrome(number):
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10
    if thousands == units and hundreds == tens:
        return "YES"
    else:
        return "NO"

number = int(input("Enter a number: "))
print(is_palindrome(number))