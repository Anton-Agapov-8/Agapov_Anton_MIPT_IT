n = int(input())
a = list(map(int, input().split()))
av = sum(a) / len(a)
min_dist = max(a)
ans = -1
for el in a:
    dist = abs(el - av)
    if dist < min_dist:
        ans = el
        min_dist = dist
print(ans)
