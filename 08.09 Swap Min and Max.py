lst = [int(x) for x in input("Enter Values Separated by Spaces: ").split()]

min_idx = max_idx = 0

for i in range(len(lst)):
    if lst[i] < lst[min_idx]:
        min_idx = i
    if lst[i] > lst[max_idx]:
        max_idx = i

lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]

print("Swapped Minimum and Maximum:", " ".join(str(x) for x in lst))