m, n = map(int, input("Enter the number of rows and columns: ").split())

arr = []
for i in range(m):
    row = list(map(int, input("Enter a line of data: ").split()))
    arr.append(row)

for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

max_elem = arr[0][0]
max_index = (0, 0)
for i in range(m):
    for j in range(n):
        if arr[i][j] > max_elem:
            max_elem = arr[i][j]
            max_index = (i, j)

print("The maximum value {} occurred in row {} column {}".format(max_elem, max_index[0], max_index[1]))