#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


t = np.arange(-5, 5, 0.01)
x = np.full_like(t, 1, dtype=np.float32)

N = 100
for n in range(1,N+1):
    x += (np.cos(n*np.pi*t) + (2*n*np.pi)*np.sin(n*np.pi*t) - np.cos(n*np.pi*(t-2))) / ((n*np.pi) * (n*np.pi))
    pass


ax = new_subplots(1, 1)

ax.plot(t, x)
ax.set_xlim([-5, 5])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x \left( t \right) $')
ax.set_title(r'$N=100$')

plt.tight_layout()
plt.show()
