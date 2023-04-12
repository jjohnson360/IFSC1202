class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = ""

with open("10.01 Pets.txt", "r") as file:
    lines = file.readlines()

pets = []
for line in lines:
    pet_data = line.strip().split(",")
    pet = Pet()
    pet.name = pet_data[0]
    pet.type = pet_data[1]
    pet.age = pet_data[2]
    pets.append(pet)

print("{:>8} {:>8} {:>8}".format("Name", "Type", "Age"))
for pet in pets:
    print("{:>8} {:>8} {:>8}".format(pet.name, pet.type, pet.age))