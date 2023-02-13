
def is_prime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter N: ").strip())
    if is_prime(n):
        print("PRIME")
    else:
        print("COMPOSITE")

if __name__ == '__main__':
    main()
