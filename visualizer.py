import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.ticker import FuncFormatter
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt, mpld3
import pylab

from manager import get_sorted_mean_price


data_list = get_sorted_mean_price(['khu vuc ban dat', 'ho chi minh'])[:-1]

print(data_list)

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = [data[0] for data in data_list]
performance = [data[1] for data in data_list]

y_pos = np.arange(len(people))

error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('price * 1000 per m2')
ax.set_title('Auto land')

plt.show()

# mpld3.show()
