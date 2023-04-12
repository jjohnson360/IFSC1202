class Car:
    def __init__(self, year, make):
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        self.speed = max(0, self.speed - value)


with open("10.03 Cars.txt", "r") as f:
    year_make = f.readline().strip().split(",")
    car = Car(year_make[0], year_make[1])

    print("Make:{}\nYear: {}\n".format(car.make, car.year))
    print("{:>0}    {:>5}".format("Change", "Speed"))
    for line in f:
        value = int(line.strip())
        if value > 0:
            car.accelerate(value)
            print("{:>6}  {:>7}".format(value, car.speed))
        else:
            car.brake(-value)
            print("{:>6}  {:>7}".format(value, car.speed))
