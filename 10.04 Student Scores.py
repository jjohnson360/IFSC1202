class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        total = 0
        count = 0
        for grade in self.Grades:
            if grade != "":
                total += float(grade)
                count += 1
        if count != 0:
            return round(total / count, 2)
        else:
            return 0

    def TotalAverage(self):
        total = 0
        count = 0
        for grade in self.Grades:
            if grade != "":
                total += float(grade)
            count += 1
        return round(total / count, 2)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

def print_header():
    print("{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
    print("{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format("Name", "Name", "Number", "Average", "Average", "Grade"))

def print_divider():
    print("-" * 12, "-" * 12, "-" * 12, "-" * 12, "-" * 12, "-" * 12)

def print_student(student):
    print("{:>12} {:>12} {:>12} {:>12.2f} {:>12.2f} {:>12}".format(student.FirstName, student.LastName, student.TNumber, student.RunningAverage(), student.TotalAverage(), student.LetterGrade()))

filename = "10.04 StudentScores.txt"

print_header()
print_divider()

with open(filename, 'r') as file:
    for line in file:
        data = line.strip().split(',')
        firstname = data[0]
        lastname = data[1]
        tnumber = data[2]
        scores = data[3:]

        student = Student(firstname, lastname, tnumber, scores)
        print_student(student)
