class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price

    def inventory_value(self):
        return self.units_on_hand * self.price

with open("10.02 Inventory.txt", "r") as file:
    lines = file.readlines()

items = []
for line in lines:
    item_data = line.strip().split(",")
    description = item_data[0]
    units_on_hand = int(item_data[1])
    price = float(item_data[2])
    item = RetailItem(description, units_on_hand, price)
    items.append(item)

print("{:>25} {:>20} {:>10} {:>20}".format("Description", "Units On Hand", "Price", "Inventory Value"))
for item in items:
    print("{:>25} {:>20} {:>10.2f} {:>20.2f}".format(item.description, item.units_on_hand, item.price, item.inventory_value()))
