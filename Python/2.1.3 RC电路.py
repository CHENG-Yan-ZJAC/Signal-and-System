#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


t  = np.arange(0, 10, 0.01)
RC = 1;   y1 = 1 - np.exp(-1 * t / RC)
RC = 0.1; y2 = 1 - np.exp(-1 * t / RC)


ax = new_subplots(1, 1)

ax.plot(t, y1,       label='RC=1')
ax.plot(t, y2, '--', label='RC=0.1')
ax.set_xlim([0, 10])
ax.set_title(r'$1-e^{-\frac{t}{RC}}$')

plt.legend()
plt.tight_layout()
plt.show()
