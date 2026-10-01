n, s = input().split()
n = int(n)
s2 = ''
for i in range(0, len(s), n):
    s2 += s[i:i + n][::-1]
print(s2)
