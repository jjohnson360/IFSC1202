from math import sqrt, atan, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return round(sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2), 7)

    def midpoint(self, other):
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y)

    def x_angle(self, other):
        slope = (other.y - self.y) / (other.x - self.x)
        angle = atan(slope) * 180 / pi
        return round(angle, 7)


print(f"{'Point A':>20} {'Point B':>20} {'Distance':>20} {'Midpoint':>20} {'Angle':>20}")
print(f"{'-' * 15:>20} {'-' * 15:>20} {'-' * 15:>20} {'-' * 15:>20} {'-' * 15:>20}")

with open("10.05 Points.txt", "r") as file:
    for line in file:
        points = line.strip().split(",")
        pointA = Point(float(points[0]), float(points[1]))
        pointB = Point(float(points[2]), float(points[3]))

        distance = pointA.distance(pointB)
        midpoint = pointA.midpoint(pointB)
        angle = pointA.x_angle(pointB)

        print(f"{str(pointA):>20} {str(pointB):>20} {distance:>20.7f} {str(midpoint):>20} {angle:>20.7f}")
