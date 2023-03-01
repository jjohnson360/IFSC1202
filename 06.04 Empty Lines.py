with open('06.04 EmptyLinesInput.txt', 'r') as input_file, open('06.04 EmptyLinesOutput.txt', 'w') as output_file:
    lines_read = 0
    lines_written = 0

    for line in input_file:
        lines_read += 1

        if not line.strip():
            continue

        output_file.write(line)

        lines_written += 1

print(f"{lines_read} records read")
print(f"{lines_written} records written")