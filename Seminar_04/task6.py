import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')

dates = list(map(lambda x: '-'.join(x[:10].split('-')[::-1]), df['time']))

values = list(df['close'])
x = list(range(len(dates)))
plt.plot(x, values, color='g', label='Цены биткоина')
z = np.polyfit(x, values, 8)
p = np.poly1d(z)
y = p(x)
plt.plot(x, y, 'rD:', markersize=0, label='Аппроксимация полиномом 8 степени')
plt.legend(loc='upper left', fontsize=8)
ax = plt.gca()
ax.set_xticks(x[::200], labels=dates[::200], rotation=-30, fontsize=8)

plt.show()
