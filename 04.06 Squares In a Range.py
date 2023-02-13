def main():
    a = int(input("Enter A: ").strip())
    b = int(input("Enter B: ").strip())
    for i in range(a, b+1):
        print("{}*2={}".format(i, i**2))

if __name__ == '__main__':
    main()