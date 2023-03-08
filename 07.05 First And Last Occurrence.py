s = input("Enter a string: ")
first = s.find('f')
last = s.rfind('f')

if first == -1:
    print(0)
elif first == last:
    print(first)
else:
    print(first, last)