s = input("Enter a string: ")
first = s.find('f')
second = s.find('f', first + 1)

if first == -1:
    print("Zero f")
elif second == -1:
    print("One f")
else:
    print(second)