import math


class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        angle1 = math.degrees(math.acos((self.s2 ** 2 + self.s3 ** 2 - self.s1 ** 2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1 ** 2 + self.s3 ** 2 - self.s2 ** 2) / (2 * self.s1 * self.s3)))
        angle3 = math.degrees(math.acos((self.s1 ** 2 + self.s2 ** 2 - self.s3 ** 2) / (2 * self.s1 * self.s2)))
        return [angle1, angle2, angle3]


TriangleList = []

with open("Exam Three Triangles.txt", "r") as file:
    for line in file:
        sides = line.strip().split(",")
        s1 = float(sides[0])
        s2 = float(sides[1])
        s3 = float(sides[2])
        t = Triangle(s1, s2, s3)
        TriangleList.append(t)

# print the table header
print("{:>15}    {:<11}{:<11}{:<11}{:<16}{:<9}{:<11}{:<11}{:<11}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))

# print the data for each triangle
for t in TriangleList:
    angles = t.angles()
    print("{:>15}    {:<11.3f}{:<11.3f}{:<11.3f}{:<16.3f}{:<9.3f}{:<11.3f}{:<11.3f}{:<11.3f}".format(t.type(), t.s1, t.s2, t.s3, t.perimeter(), t.area(), angles[0], angles[1], angles[2]))
