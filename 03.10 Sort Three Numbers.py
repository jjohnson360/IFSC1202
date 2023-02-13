def main():
    n = int(input("Enter N: ").strip())
    product = 1
    for i in range(n):
        num = int(input("Enter Number {}: ".format(i + 1)).strip())
        product *= num
    print(product)

if __name__ == '__main__':
    main()