s = input().split()
print(' '.join([' '.join(s[i:i + 2][::-1]) for i in range(0, len(s), 2)]))
