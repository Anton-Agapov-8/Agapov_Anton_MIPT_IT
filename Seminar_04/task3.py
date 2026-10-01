import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure()  # figsize=(10, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
# names = set()
# for i in range(len(df)):
#     names.add(df['Species'][i])
names = df['Species'].unique()
names = list(names)
names.sort()
parts = []
for name in names:
    parts.append(len(df[df['Species'] == name]) / len(df))

x = sum(df['PetalWidthCm'] <= 1.2)
y = sum(df['PetalWidthCm'] > 1.2) & sum(df['PetalWidthCm'] <= 1.5)
z = sum(df['PetalWidthCm'] > 1.5)

ax1.pie(parts, labels=names, shadow=True, explode=[0.05, 0.05, 0.05])
ax2.pie([x, y, z], labels=['PetalWidthCm <= 1.2', '1.2 < PetalWidthCm <= 1.5', '1.5 < PetalWidthCm'], shadow=True,
        explode=[0.05, 0.05, 0.05], colors=['b', 'r', 'g'])
plt.show()
