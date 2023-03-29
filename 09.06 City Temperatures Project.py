temps = []
with open('09.06 CityTemps.txt', 'r') as file:
    for line in file:
        if line.strip() != '':
            row = line.strip().split()
            temps.append(row)

# Calculate the Average Temperature for each location
for i in range(len(temps)):
    total = 0
    for j in range(1, len(temps[i])):
        total += int(temps[i][j])
    avg_temp = total // (len(temps[i])-1)
    temps[i].append(str(avg_temp))

# Print the Results
print('{:<8}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}'.format('City', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', 'Avg'))
for row in temps:
    print('{:<8}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}{:<9}'.format(*row))
