def is_prime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def main():
    a = int(input("Enter A: ").strip())
    b = int(input("Enter B: ").strip())
    for n in range(a, b+1):
        if is_prime(n):
            print(n)

if __name__ == '__main__':
    main()