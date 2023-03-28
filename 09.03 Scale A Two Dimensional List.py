def print_list(a):
    for row in a:
        for elem in row:
            print(elem, end=" ")
        print()

def scale_list(a, s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= s

a = []
with open("09.03 NumbersList.txt") as f:
    for line in f:
        row = list(map(int, line.split()))
        a.append(row)

print("Original list:")
print_list(a)

s = int(input("Enter scale value: "))
scale_list(a, s)

print("Scaled list:")
print_list(a)
