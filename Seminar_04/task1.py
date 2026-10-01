import matplotlib.pyplot as plt


# График из моего отчета по лабе 1.1.4
def fact(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res


fig, ax = plt.subplots()
t = 10
data = open("эксперимент_2026-09-08_09-56-58.txt", 'r')
# data = open("симуляция_2026-09-08_10-03-01.txt", 'r')
d = list(map(int, data.readlines()))
decay_num = {}
decays = []
for i in range(0, len(d), t):
    if i + t < len(d):
        decays.append(sum(d[i:i + t]))
    else:
        break
    if decays[-1] not in decay_num:
        decay_num[decays[-1]] = 1
    else:
        decay_num[decays[-1]] += 1
x = []
y = []
decay_num_list = list(decay_num.items())
decay_num_list.sort(key=lambda x: x[0])
for el in decay_num_list:
    x.append(el[0])
    y.append(el[1] / len(d) * t * 100)

ax.bar(x, y)

n_av = sum(d) / len(d) * t
n_sum = 0
for n in decays:
    n_sum += (n - n_av) ** 2
sigma = (t / len(d) * n_sum) ** 0.5
maxx = max(x)
minx = min(x)
x2, y2 = [], []
for i in x:
    j = (n_av ** i) / fact(i) * 2.718281828 ** (-n_av) * 100
    x2.append(i)
    y2.append(j)
ax.plot(x, y2, color="red")

ax.set_xlabel(f'Количество распадов за {t}с.')
ax.set_ylabel('Доля среди всех случаев %')

plt.show()
