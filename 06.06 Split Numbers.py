import math

def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2 != 0

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

even_file = open("06.06 Evennumbers.txt", "w")
odd_file = open("06.06 Oddnumbers.txt", "w")
prime_file = open("06.06 Primenumbers.txt", "w")
numbers_file = open("06.06 Numbers.txt", "r")

even_count = 0
odd_count = 0
prime_count = 0
numbers_count = 0

for line in numbers_file:
    num = int(line.strip())
    numbers_count += 1
    if isEven(num):
        even_count += 1
        even_file.write(str(num) + "\n")
    if isOdd(num):
        odd_count += 1
        odd_file.write(str(num) + "\n")
    if isPrime(num):
        prime_count += 1
        prime_file.write(str(num) + "\n")

even_file.close()
odd_file.close()
prime_file.close()
numbers_file.close()

print( even_count, "even numbers")
print(odd_count, "odd numbers")
print(prime_count, "prime numbers")
print(numbers_count, "numbers read")