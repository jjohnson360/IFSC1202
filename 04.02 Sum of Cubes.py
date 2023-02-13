def main():
    n = int(input("Enter Number: ").strip())
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3
    print(sum_of_cubes)

if __name__ == '__main__':
    main()