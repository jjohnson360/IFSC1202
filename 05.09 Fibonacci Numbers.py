n = int(input("Enter Fibonnaci Sequence Number: "))

fib_0 = 0
fib_1 = 1

if n == 0:
    print(fib_0)
elif n == 1:
    print(fib_1)
else:
    for i in range(2, n + 1):
        fib_i = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_i
    print(fib_1)