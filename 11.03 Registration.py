class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.CourseList = []


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        new_student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(new_student)

    def find_student(self, studenttofind):
        for i, student in enumerate(self.Studentlist):
            if student.TNumber == studenttofind:
                return i
        return -1

    def print_student_list(self):
        print("{:<15} {:<15} {:<15} {:<15} {:<49} {:<19} {:<40} ".format("First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Time", ))

        for student in self.Studentlist:
            print("{:<14} {:<15} {:<15}".format(student.FirstName, student.LastName, student.TNumber))
            for course in student.CourseList:
                print("                                                {:<0}{:<11}{:<50}{:<20}{:<20}".format(course.department, course.number, course.name, course.room, course.meetingtimes))

    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                student_info = line.strip().split(',')
                self.add_student(student_info[0], student_info[1], student_info[2])


class Course:
    def __init__(self, department, number, name, room, meetingtimes):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingtimes = meetingtimes


class CourseList:
    def __init__(self):
        self.Courselist = []

    def add_course(self, department, number, name, room, meetingtimes):
        new_course = Course(department, number, name, room, meetingtimes)
        self.Courselist.append(new_course)

    def find_course(self, departmenttofind, numbertofind):
        for i, course in enumerate(self.Courselist):
            if course.department == departmenttofind and course.number == numbertofind:
                return i
        return -1

    def add_course_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                course_info = line.strip().split(',')
                self.add_course(course_info[0], course_info[1], course_info[2], course_info[3], course_info[4])


mycourselist = CourseList()
mycourselist.add_course_from_file('11.03 Courses.txt')

mystudentlist = StudentList()
mystudentlist.add_student_from_file('11.03 Students.txt')

with open('11.03 Registration.txt', 'r') as file:
    for line in file:
        reg_info = line.strip().split(',')
        department = reg_info[0]
        course_number = reg_info[1]
        student_tnumber = reg_info[2]

        course_index = mycourselist.find_course(department, course_number)
        if course_index != -1:
            selected_course = mycourselist.Courselist[course_index]
            student_index = mystudentlist.find_student(student_tnumber)
            if student_index != -1:
                mystudentlist.Studentlist[student_index].CourseList.append(selected_course)

mystudentlist.print_student_list()
