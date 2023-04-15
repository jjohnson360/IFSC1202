class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price

    def inventory_value(self):
        return self.units_on_hand * self.price

def print_inventory(items):
    print(f"{'Description':>0} {'Units On Hand':>20} {'Price':>20} {'Inventory Value':>20}")
    for item in items:
        print(f"{item.description:>11} {item.units_on_hand:>20} {item.price:>20.2f} {item.inventory_value():>20.2f}")

def find_inventory(items, description):
    for i, item in enumerate(items):
        if item.description == description:
            return i
    return -1

def update_inventory(items, description, new_price):
    index = find_inventory(items, description)
    if index != -1:
        items[index].price = new_price

with open('11.01 Inventory.txt', 'r') as f:
    items = []
    for line in f:
        data = line.strip().split(',')
        item = RetailItem(data[0], int(data[1]), float(data[2]))
        items.append(item)

print("")
print_inventory(items)

with open('11.01 InventoryUpdate.txt', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        update_inventory(items, data[0], float(data[1]))

print("\n")
print_inventory(items)