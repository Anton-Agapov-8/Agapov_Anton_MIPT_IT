import numpy as np

# Данные о точках хранятся в отдельном файле.
# В первой строке расположены значения x, во второй строке - соответствующие им значения y

f = open('task6_test.txt', 'r')
data = f.readlines()
x = np.array(list(map(int, data[0].split())))
y = np.array(list(map(int, data[1].split())))

n = x.size
x_av = np.sum(x) / n
y_av = np.sum(y) / n
xy_av = np.sum(x * y) / n
xsquare_av = np.sum(x ** 2) / n

k = (xy_av - x_av * y_av) / (xsquare_av - x_av ** 2)
b = y_av - k * x_av

sign = '+'
if b < 0:
    sign = '-'
print(f'y = {k:.3f} * x {sign} {abs(b):.3f}')
