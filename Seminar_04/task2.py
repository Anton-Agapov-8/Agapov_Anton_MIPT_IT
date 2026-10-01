import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

pos = 0

scale = 10

size = 10000

values1 = np.random.normal(pos, 10, 100)
values2 = np.random.normal(pos, 10, 1000)
values3 = np.random.normal(pos, 10, 10000)
values4 = np.random.normal(pos, 10, 100000)
values5 = np.random.normal(pos, 10, 1000000)
values6 = np.random.normal(pos, 10, 10000000)

ax1.hist(values1, 10, density=True)
ax2.hist(values2, 100, density=True)
ax3.hist(values3, 1000, density=True)
ax4.hist(values4, 1000, density=True)
ax5.hist(values5, 1000, density=True)
ax6.hist(values6, 1000, density=True)

ax1.set_title('100 точек')
ax2.set_title('1000 точек')
ax3.set_title('10000 точек')
ax4.set_title('100000 точек')
ax5.set_title('1000000 точек')
ax6.set_title('10000000 точек')

plt.show()