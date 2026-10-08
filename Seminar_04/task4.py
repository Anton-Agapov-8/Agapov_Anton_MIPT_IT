import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def mnk(x, y):
    n = len(x)
    x = np.array(x)
    y = np.array(y)
    x_av = np.sum(x) / n
    y_av = np.sum(y) / n
    xy_av = np.sum(x * y) / n
    xsquare_av = np.sum(x ** 2) / n
    a = (xy_av - x_av * y_av) / (xsquare_av - x_av ** 2)
    b = y_av - a * x_av
    return a, b


df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize=(10, 6))
ax_list = []
for i in range(6):
    ax_list.append(fig.add_subplot(231 + i))

xy_list_list = []
x_list_list = []
y_list_list = []
pairs = (('SepalWidthCm', 'SepalLengthCm'),
         ('SepalLengthCm', 'PetalLengthCm'),
         ('PetalLengthCm', 'PetalWidthCm'),
         ('SepalLengthCm', 'PetalLengthCm'),
         ('SepalWidthCm', 'PetalWidthCm'),
         ('SepalLengthCm', 'PetalWidthCm'))
for i in range(len(pairs)):
    xy_list_list.append([])
    x, y = list(df[pairs[i][0]]), list(df[pairs[i][1]])
    for j in range(len(x)):
        xy_list_list[i].append((x[j], y[j]))
    # print(xy_list_list[i])
    xy_list_list[i].sort(key=lambda x: x[0])
for i in range(len(pairs)):
    x_list_list.append([])
    y_list_list.append([])
    for j in range(len(xy_list_list[i])):
        x_list_list[i].append(xy_list_list[i][j][0])
        y_list_list[i].append(xy_list_list[i][j][1])
for i in range(len(x_list_list)):
    x = np.linspace(min(x_list_list[i]), max(x_list_list[i]), 100)
    a, b = mnk(x_list_list[i], y_list_list[i])
    print(f'Зависимость {pairs[i][1]} от {pairs[i][0]}: a = {a:.3f}, b = {b:.3f}')
    if i == 0:
        ax_list[i].plot(x_list_list[i], y_list_list[i], 'o-', markersize=4, linewidth=0, markeredgecolor='#000000', color='#FF0000', label='Данные')
        ax_list[i].plot(x, a * x + b, 'D-', markersize=0, linewidth=2, color='#008888', label='МНК Аппроксимация')
    else:
        ax_list[i].plot(x_list_list[i], y_list_list[i], 'o-', markersize=4, linewidth=0, markeredgecolor='#000000', color='#FF0000')
        ax_list[i].plot(x, a * x + b, 'D-', markersize=0, linewidth=2, color='#008888')
    ax_list[i].set_title(f'{pairs[i][1]} от {pairs[i][0]}', fontsize=10)
    # ax_list[i].legend()

fig.legend(fontsize=8)
plt.show()
