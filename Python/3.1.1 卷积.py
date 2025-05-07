#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_diff import *


An = np.array([-0.8])
Bm = np.array([0.2])
b  = 0
Yn = np.array([0])
Xm = np.array([0])

n     = np.arange(-2, 21, 1)
X1    = np.zeros_like(n, dtype=np.float64)
X2    = np.zeros_like(n, dtype=np.float64)
X1[2] = 1.0 # X[2] is real x[0], we set x[0]=1, this is a pulse
X2[6] = 3.0
Y1    = my_diff(An, Yn, Bm, Xm, b, X1)
Y2    = my_diff(An, Yn, Bm, Xm, b, X2)


axs = new_subplots(2, 2)

axs[0][0].stem(n, X1)
axs[0][0].set_xlim([-2, 20])
axs[0][0].set_ylim([0, 3.1])
axs[0][0].set_ylabel('signal')
axs[0][0].set_title(r'$\delta \left[ n \right] $')
axs[1][0].stem(n, Y1)
axs[1][0].set_xlim([-2, 20])
axs[1][0].set_ylim([0, 1.1])
axs[1][0].set_ylabel('response')

axs[0][1].stem(n, X2)
axs[0][1].set_xlim([-2, 20])
axs[0][1].set_ylim([0, 3.1])
axs[0][1].set_title(r'$3\delta \left[ n-4 \right] $')
axs[1][1].stem(n, Y2)
axs[1][1].set_xlim([-2, 20])
axs[1][1].set_ylim([0, 1.1])

plt.tight_layout()
plt.show()
