class VendingItem:
    def __init__(self, Name, InitialCount, CostPerItem):
        self.Name = Name
        self.InitialCount = InitialCount
        self.CostPerItem = CostPerItem
        self.SoldCount = 0
        self.LostCount = 0

    def InitialValue(self):
        return self.InitialCount * self.CostPerItem

    def SoldValue(self):
        return self.SoldCount * self.CostPerItem

    def LostValue(self):
        return self.LostCount * self.CostPerItem


class Vending:
    def __init__(self):
        self.VendingList = []
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0

    def load_vending_items_from_file(self, filename):
        with open(filename) as file:
            for line in file:
                name, count, price = line.strip().split(',')
                count = int(count)
                price = float(price)
                item = VendingItem(name, count, price)
                self.VendingTotalInitialValue += item.InitialValue()
                self.VendingTotalInitialCount += count
                self.VendingList.append(item)

    def print_vending(self):
        print("{:<9} {:<9} {:<9} {:<10} {:<9} {:<9} {:<9} {:<9}".format(
            "", "Initial", "Price", "Initial", "Sold", "Sold", "Lost", "Lost"))
        print("{:<9} {:<9} {:<9} {:<10} {:<9} {:<9} {:<9} {:<9}".format(
            "Product", "Count", "Per Item", "Value", "Count", "Value", "Count", "Value"))
        print("")
        for item in self.VendingList:
            print("{:<9} {:<9} {:<8.2f}  {:<9.2f}  {:<9} {:<8.2f}  {:<9} {:<8.2f}".format(
                item.Name, item.InitialCount, item.CostPerItem, item.InitialValue(),
                item.SoldCount, item.SoldValue(), item.LostCount, item.LostValue()))
        print("")
        print("{:<9} {:<9} {:<9} {:<9.2f}  {:<9} {:<8.2f}  {:<9} {:<8.2f}".format(
            "Total", self.VendingTotalInitialCount, "", self.VendingTotalInitialValue,
            self.VendingTotalSoldCount, self.VendingTotalSoldValue,
            self.VendingTotalLostCount, self.VendingTotalLostValue))

    def find_product(self, producttofind):
        for i, item in enumerate(self.VendingList):
            if item.Name == producttofind:
                return i
        return -1

    def update_vending(self, productname):
        index = self.find_product(productname)
        if index >= 0:
            item = self.VendingList[index]
            if item.SoldCount < item.InitialCount:
                item.SoldCount += 1
                self.VendingTotalSoldCount += 1
                self.VendingTotalSoldValue += item.CostPerItem
            else:
                item.LostCount += 1
                self.VendingTotalLostCount += 1
                self.VendingTotalLostValue += item.CostPerItem

vending = Vending()
vending.load_vending_items_from_file('Final Project Vending.txt')
with open('Final Project Sales.txt', 'r') as f:
    for line in f:
        product_name = line.strip()
        vending.update_vending(product_name)
vending.print_vending()