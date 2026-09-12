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


f = open('input6.txt', 'r')
data = list(f.readlines())
num_base = int(data[2])
nums = list(map(lambda x: int(to10(x, num_base)), data[0].split()))
sign = data[1]
res = nums[0]
for i in range(1, len(nums)):
    if '+' in sign:
        res += nums[i]
    elif '*' in sign:
        res *= nums[i]
    elif '-' in sign:
        res -= nums[i]
f.close()
with open('output6.txt', 'w') as f2:
    f2.write(from10(str(res), num_base))
