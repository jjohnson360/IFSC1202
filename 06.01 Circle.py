import math

def diameter(radius):
    return 2 * radius

def circumference(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius ** 2

with open("06.01 Radius.txt", "r") as f:
    radii = [float(line.strip()) for line in f]

print("{:>15}{:>15}{:>15}{:>15}" .format("Radius", "Diameter", "Circumference", "Area"))

for radius in radii:
    d = diameter(radius)
    c = circumference(radius)
    a = area(radius)
    print("{:>15.5f}{:>15.5f}{:>15.5f}{:>15.5f}" .format(radius, d, c, a))