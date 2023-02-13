def main():
    n = int(input("Enter N: ").strip())
    count = 0
    for i in range(n):
        num = int(input("Enter Number {}: ".format(i + 1)).strip())
        if num == 0:
            count += 1
    print("Number of zeros :", count)

if __name__ == '__main__':
    main()