#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_diff import *


T  = 0.2
An = np.array([T-1])
Bm = np.array([T])
b  = 0
Yn = np.array([0])
Xm = np.array([0])
t  = np.arange(0, 10, T)
X  = np.ones_like(t)
Y_differential = 1 - np.exp(-1*t)
Y_difference   = my_diff(An, Yn, Bm, Xm, b, X)


ax = new_subplots(1, 1)

ax.plot(t, Y_differential,      label='differential')
ax.plot(t, Y_difference,   'o', label='difference')
ax.set_xlim([0, 10])
ax.set_ylim([0, 1.1])

plt.legend()
plt.tight_layout()
plt.show()
