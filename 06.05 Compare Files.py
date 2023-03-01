file_a = open("06.05 CompareFileA.txt", "r")
file_b = open("06.05 CompareFileB.txt", "r")

diff_count = 0
for line_num, (line_a, line_b) in enumerate(zip(file_a, file_b), start=1):
    if line_a != line_b:
        print(f"Line: {line_num} - File A: {line_a.strip()}\nLine: {line_num} - File B: {line_b.strip()}\n")
        diff_count += 1

print(f"{diff_count} differences")

file_a.close()
file_b.close()