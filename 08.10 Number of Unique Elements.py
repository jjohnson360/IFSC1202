user_input = input("Enter Values Separated by Spaces: ")
integer_list = user_input.split()
unique_elements = []

for i in range(len(integer_list)):
    found_duplicate = False
    for j in range(len(integer_list)):
        if i != j and integer_list[i] == integer_list[j]:
            found_duplicate = True
            break
    if not found_duplicate:
        unique_elements.append(integer_list[i])

print("Unique Elements:", " ".join(unique_elements))