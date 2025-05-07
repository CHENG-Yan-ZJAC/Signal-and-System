#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_diff import *


An = np.array([-0.8]); Bm = np.array([0.2]); b  = 0
Yn = np.array([0]);    Xm = np.array([0])

n  = np.arange(-2, 21, 1)
X  = np.zeros_like(n, dtype=np.float64)
X[2:] = 1.0
Yd = my_diff(An, Yn, Bm, Xm, b, X)
h  = np.array([0.0, 0.2, 0.16, 0.128, 0.1024, 0.0819, 0.0655, 0.0524, 0.0419, 0.0336, 0.0268])
Yc = np.convolve(X, h, mode='full')


axs = new_subplots(2, 1)

axs[0].stem(n, X)
axs[0].set_xlim([-2, 20])
axs[0].set_ylim([0, 1.1])
axs[0].set_ylabel('x')
axs[1].plot(n, Yd, '*', c='r', label='diff')
axs[1].plot(n, Yc[:n.shape[0]], 'o', markerfacecolor='none', markeredgecolor='b', label='conv')
axs[1].set_xlim([-2, 20])
axs[1].set_ylim([0, 1.1])
axs[1].set_ylabel('y')

plt.legend()
plt.tight_layout()
plt.show()
