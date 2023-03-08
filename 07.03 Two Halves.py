s = input("Enter a string: ")
half = (len(s) + 1) // 2
new_s = s[half:] + s[:half]
print(new_s)