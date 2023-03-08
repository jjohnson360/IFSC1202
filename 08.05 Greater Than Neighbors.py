s = input("Enter Values Separated by Spaces: ")

a = s.split()
for i in range(len(a)):
    a[i] = int(a[i])

count = 0

for i in range(1, len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        count += 1

print(count)