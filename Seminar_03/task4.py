size, symb = input().split()
size = int(size)
for i in range(1, round(size / 2) + 1):
    print(symb * i)
for i in range(round(size / 2), size):
    print(symb * (round(size - i)))
