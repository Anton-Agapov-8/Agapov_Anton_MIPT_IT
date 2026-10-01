from random import randrange, gauss
from math import tan

import numpy as np
import matplotlib.pyplot as plt


def generate_data(s, e, a, n):
    x_array = np.linspace(s, e, n)
    y_array = []
    for x in x_array:
        sigma = abs(a * x) ** 0.5
        y_array.append(gauss(a * x, sigma))
    y_array = np.array(y_array)
    return x_array, y_array


s0, e0 = randrange(-1000, 1000), randrange(-1000, 1000)
a = tan(randrange(-int(np.pi / 2 * 1000), int(np.pi / 2 * 1000)) / 1000)
b = randrange(-1000, 1000)
s = min(s0, e0)
e = max(s0, e0)
n = int(input())
x, y = generate_data(s, e, a, n)

x_av = np.sum(x) / n
y_av = np.sum(y) / n
xy_av = np.sum(x * y) / n
xsquare_av = np.sum(x ** 2) / n

a = (xy_av - x_av * y_av) / (xsquare_av - x_av ** 2)
b = y_av - a * x_av

print('Данные:')
print('X \t Y')
for i in range(n):
    print(f'{x[i]:.3f}\t{y[i]:.3f}')
sign = '+'
if b < 0:
    sign = '-'
print('Аппроксимация:')
print(f'y = {a:.3f} * x {sign} {abs(b):.3f}')

x2 = np.linspace(s, e, 100)
y2 = x2 * a + b
plt.plot(x, y, "gD:", linewidth=2, label='Сгенерированные данные')
plt.plot(x2, y2, 'r-', label=f'Аппроксимация МНК: $y = {a:.3f} \\cdot x {sign} {abs(b):.3f}$')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
