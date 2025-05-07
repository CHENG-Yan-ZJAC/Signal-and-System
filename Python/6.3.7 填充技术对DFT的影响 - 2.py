#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_dft import *


n_1  = np.arange(0, 30, 0.5)
xn_1 = 0.9**n_1
Xm_1 = my_dft(xn_1)

n_2  = np.arange(0, 10, 0.5)
xn_2 = 0.9**n_2
Xm_2 = my_dft(xn_2)

n_3  = np.arange(0, 30, 0.5)
xn_3 = 0.9**n_3
xn_3[xn_2.size:] = 0
Xm_3 = my_dft(xn_3)

axs = new_subplots(3, 1)

axs[0].plot(np.abs(Xm_1))
axs[0].set_xlim([0, Xm_1.size-1])
axs[0].set_title(r'$|X[m]|$')

axs[1].plot(np.abs(Xm_2))
axs[1].set_xlim([0, Xm_2.size-1])

axs[2].plot(np.abs(Xm_3))
axs[2].set_xlim([0, Xm_3.size-1])

plt.tight_layout()
plt.show()
