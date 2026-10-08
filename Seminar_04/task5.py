import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')

dates = list(map(lambda x: '-'.join(x[:10].split('-')[::-1]), df['time']))

values = list(df['close'])
x = list(range(len(dates)))
plt.plot(x, values, color='g', label='Цены биткоина')
plt.legend()
ax = plt.gca()
ax.set_xticks(x[::200], labels=dates[::200], rotation=-30, fontsize=8)

plt.show()
