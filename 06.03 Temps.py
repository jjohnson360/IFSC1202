def FahrToCel(fahr):
    return (fahr - 32) * 5 / 9

with open("06.03 FTemps.txt", "r") as fin, open("06.03 CTemps.txt", "w") as fout:
    count = 0
    
    for line in fin:
        
        fahr = float(line)
        cel = FahrToCel(fahr)
        
        fout.write(f"{cel:5.1f}\n")
        count += 1

print(f"{count} records written")