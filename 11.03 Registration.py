# Read data from Courses.txt and store it in a list of dictionaries
courses = []
with open('11.03 Courses.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        courses.append({'code': line[1], 'name': line[2], 'room': line[3], 'times': line[4]})

# Read data from Students.txt and store it in a list of dictionaries
students = []
with open('11.03 Students.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        students.append({'first_name': line[0], 'last_name': line[1], 't_number': line[2]})

# Read data from Registration.txt and store it in a dictionary of lists
registrations = {}
with open('11.03 Registration.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        t_number = line[0]
        course_code = line[1]
        if t_number in registrations:
            registrations[t_number].append(course_code)
        else:
            registrations[t_number] = [course_code]

# Print the list of courses along with their meeting times and rooms
print('Courses:')
print('Code\tName\tRoom\tTimes')
for course in courses:
    print(f"{course['code']}\t{course['name']}\t{course['room']}\t{course['times']}")
print()

# Print the list of students with their registered courses
print('Registrations:')
for student in students:
    t_number = student['t_number']
    print(f"{student['first_name']} {student['last_name']} ({t_number}):")
    if t_number in registrations:
        for course_code in registrations[t_number]:
            course = next((c for c in courses if c['code'] == course_code), None)
            if course:
                print(f"\t{course['name']} ({course_code})")
            else:
                print(f"\tCourse not found: {course_code}")
    else:
        print("\tNo registrations found.")
    print()
