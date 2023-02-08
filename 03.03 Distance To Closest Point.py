a = int(input("Enter point A: "))

b = int(input("Enter point B: "))

c = int(input("Enter point C: "))

distance_AB = ((b - a))
distance_AC = ((c - a))

closest_distance = min(distance_AB, distance_AC)

print(closest_distance)