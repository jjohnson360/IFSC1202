def main():
    n = int(input("Enter N: ").strip())
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, n+1):
        factorial *= i
        sum_of_factorials += factorial
    print("The sum of Factorials", sum_of_factorials)

if __name__ == '__main__':
    main()