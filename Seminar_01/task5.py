def to10(n, b):
    res = 0
    for i in range(len(n)):
        # print(int(n[len(n) - i - 1]), i)
        res += int(n[len(n) - i - 1]) * b ** i
        # print(res)
    return str(res)


def from10(n, c):
    res = ''
    n = int(n)
    while n >= c:
        res += str(n % c)
        n //= c
    res += str(n)
    return str(res)[::-1]


n = input()
b = int(input())
c = int(input())
n10 = to10(n, b)
nc = from10(n10, c)
print(nc)
