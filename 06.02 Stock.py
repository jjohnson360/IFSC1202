def percentchange(today, yesterday):
    return (today - yesterday) / yesterday * 100

with open("06.02 Stock.txt", "r") as f:

    print(f"{'Price':<10} {'Change':>10}")
    yesterday_price = float(f.readline())

    print(f"{yesterday_price:<10.2f}")

    for line in f:
        today_price = float(line)
        change = percentchange(today_price, yesterday_price)
        print(f"{today_price:<10.2f}  {change:>10.2f}%")
        yesterday_price = today_price