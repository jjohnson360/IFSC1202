size = int(input("Enter Size: "))

board = []

board.append(["+"] + ["-"] * size + ["+"])

for i in range(size):
    row = ["|"]
    for j in range(size):
        if (i + j) % 2 == 0:
            row.append("*")
        else:
            row.append(" ")
    row.append("|")
    board.append(row)

board.append(["+"] + ["-"] * size + ["+"])

for row in board:
    print("".join(row))
