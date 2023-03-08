with open('08.11 USPopulation.txt') as f:
    populations = [int(line.strip()) * 1000 for line in f]

print("Year\tPopulation\tChange\tPercent Change")

total_change = 0
min_change = max_change = min_year = max_year = None

for i, population in enumerate(populations):
    year = 1950 + i
    if i == 0:
        change = percent_change = None
    else:
        change = population - populations[i - 1]
        percent_change = round((change / populations[i - 1]) * 100, 2)
        total_change += change
        if min_change is None or change < min_change:
            min_change, min_year = change, year
        if max_change is None or change > max_change:
            max_change, max_year = change, year

    percent_change = f"{percent_change}%" if percent_change is not None else 'N/A'
    print(f"{year}\t{population}\t{change}\t{percent_change}")

average_change = total_change / (len(populations) - 1)
print()
print(f"Average Change = {average_change}")
print(f"Minimum Change = {min_change} ({min_year})")
print(f"Maximum Change = {max_change} ({max_year})")