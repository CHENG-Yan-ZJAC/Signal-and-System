#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


t  = np.arange(-4, 4, 0.01)
x1 = np.full_like(t, 0.5, dtype=np.float32)
x2 = np.full_like(t, 0.5, dtype=np.float32)
x3 = np.full_like(t, 0.5, dtype=np.float32)
x4 = np.full_like(t, 0.5, dtype=np.float32)

N = 3
for n in range(1,N+1,2):
    x1 += 2/n/np.pi * np.sin(n*np.pi/2) * np.cos(n*np.pi*t)
    pass

N = 8
for n in range(1,N+1,2):
    x2 += 2/n/np.pi * np.sin(n*np.pi/2) * np.cos(n*np.pi*t)
    pass

N = 20
for n in range(1,N+1,2):
    x3 += 2/n/np.pi * np.sin(n*np.pi/2) * np.cos(n*np.pi*t)
    pass

N = 100
for n in range(1,N+1,2):
    x4 += 2/n/np.pi * np.sin(n*np.pi/2) * np.cos(n*np.pi*t)
    pass


axs = new_subplots(2, 2)

axs[0][0].plot(t, x1); axs[0][0].set_xlim([-4, 4]); axs[0][0].set_title(r'$N=3$')
axs[0][1].plot(t, x2); axs[0][1].set_xlim([-4, 4]); axs[0][1].set_title(r'$N=8$')
axs[1][0].plot(t, x3); axs[1][0].set_xlim([-4, 4]); axs[1][0].set_title(r'$N=20$')
axs[1][1].plot(t, x4); axs[1][1].set_xlim([-4, 4]); axs[1][1].set_title(r'$N=100$')
axs[1][0].set_xlabel(r'$t$')
axs[1][1].set_xlabel(r'$t$')
axs[0][0].set_ylabel(r'$x \left( t \right) $')
axs[1][0].set_ylabel(r'$x \left( t \right) $')

plt.tight_layout()
plt.show()
