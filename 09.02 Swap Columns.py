def print_list(a):
    for row in a:
        for elem in row:
            print(elem, end=" ")
        print()

def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]

a = []
with open("09.02 NumbersList.txt") as f:
    for line in f:
        row = list(map(int, line.split()))
        a.append(row)

print("Original list:")
print_list(a)

i, j = map(int, input("Enter the columns to swap: ").split())

swap_columns(a, i, j)
print("Modified list:")
print_list(a)