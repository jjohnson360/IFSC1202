
race_length = float(input("Enter the length of the race in kilometers: "))

race_minutes = int(input("Enter the number of minutes: "))
race_seconds = int(input("Enter the number of seconds: "))


total_time = (race_minutes / 60) + (race_seconds / 3600)

avg_speed = race_length / total_time

print(f"Your average speed was {avg_speed:.2f} kilometers per hour.")