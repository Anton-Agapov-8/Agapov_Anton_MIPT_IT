def fib(n):
    if n <= 1:
        return n
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(res[i - 2] + res[i - 1])
    return res[-1]


print(fib(int(input())))
