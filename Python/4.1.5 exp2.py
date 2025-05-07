#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


t = np.arange(-5, 5, 0.01)
T = 2
a = 0.5
x = np.full_like(t, a/T, dtype=np.float32)

N = 100
for n in range(1,N+1):
    x += 1/n/np.pi * (np.sin(2*n*np.pi*t/T) - np.sin(2*n*np.pi*(t-a)/T))
    pass


ax = new_subplots(1, 1)

ax.plot(t, x)
ax.set_xlim([-5, 5])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x \left( t \right) $')
ax.set_title(r'$N=100$')

plt.tight_layout()
plt.show()
