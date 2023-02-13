def main():
    n = int(input("Enter Number of Cards: ").strip())
    total = n * (n + 1) // 2
    sum_of_remaining = 0
    for i in range(n-1):
        sum_of_remaining += int(input("Enter card: ").strip())
    missing_card = total - sum_of_remaining
    print("Missing card: ", missing_card)

if __name__ == '__main__':
    main()