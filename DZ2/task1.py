num_list = list(map(int, input().split()))
cards = num_list[1:]
num = -1
for i in range(len(cards) - 1):
    if cards[i + 1] - cards[i] != 1:
        num = cards[i] + 1
        break
if num == -1:
    num = num_list[0]
print(num)
