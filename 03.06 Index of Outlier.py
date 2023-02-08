def find_different(a, b, c):
    if a == b:
        return 3
    elif a == c:
        return 2
    elif b == c:
        return 1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(f"{find_different(a, b, c)}")