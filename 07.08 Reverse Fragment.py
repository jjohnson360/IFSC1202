s = input("Enter a string: ")
first = s.find('h')
last = s.rfind('h')
result = s[:first+1] + s[first+1:last][::-1] + s[last:]

print(result)