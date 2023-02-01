timestamp1 = (6 * 3600) + (1 * 60) + 30
timestamp2 = (6 * 3600) + (2 * 60) + 10

timestamp3 = (2 * 3600) + (3 * 60) + 4
timestamp4 = (4 * 3600) + (7 * 60) + 28

timestamp5 = (10 * 3600) + (8 * 60) + 2
timestamp6 = (10 * 3600) + (8 * 60) + 2

difference_1 = timestamp2 - timestamp1
difference_2 = timestamp4 - timestamp3
difference_3 = timestamp6 - timestamp5

print("seconds between timestamps:", difference_1)
print("seconds between timestamps:", difference_2)
print("seconds between timestamps:", difference_3)