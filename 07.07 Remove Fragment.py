s = input("Enter a string: ")
first = s.find('h')
last = s.rfind('h')
result = s[:first] + s[last+1:]

print(result)