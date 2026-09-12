f = open("input.txt", 'r')
data = f.read()
dot_flag = False
k = 0
for i in range(len(data)):
    if data[i] in {'.', '!', '?'}:
        dot_flag = True
        if i == len(data):
            k += 1
    if dot_flag and data[i] not in {'.', '!', '?'}:
        dot_flag = False
        k += 1
print(k)
