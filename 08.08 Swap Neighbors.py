values = input("Enter Values Separated by Spaces: ")
lst = values.split()
n = len(lst)

if n % 2 == 0:
    end = n
else:
    end = n - 1

for i in range(0, end, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

print(' '.join(lst))