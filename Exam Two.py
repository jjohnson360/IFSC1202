with open("Exam Two Properties.csv", "r") as f:
    property_data = []
    for line in f:
        data = line.strip().split(",")
        data[4] = float(data[4])
        property_data.append(data)

zip_code = input("Enter Zip Code: ")
highest_price = None
lowest_price = None

total_price = 0

num_properties = 0

print("Street".ljust(25), "City".ljust(15), "State".ljust(5), "Zip".ljust(8), "Price")

for property in property_data:
    if property[3] == zip_code:
        print(property[0].ljust(25), property[1].ljust(15), property[2].ljust(5), property[3].ljust(8), "${:.0f}".format(property[4]))

        total_price += property[4]
        num_properties += 1
        if highest_price is None and lowest_price is None:
            highest_price = property[4]
            lowest_price = property[4]
        else:
            if property[4] > highest_price:
                highest_price = property[4]
            if property[4] < lowest_price:
                lowest_price = property[4]

if num_properties > 0:
    average_price = total_price / num_properties
    print("Maximum Price: ${:.0f}".format(highest_price))
    print("Minimum Price: ${:.0f}".format(lowest_price))
    print("Average Price: ${:.0f}".format(average_price))
else:
    print("No properties found")
