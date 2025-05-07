#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_dft import *


n_1  = np.arange(0, 50)
xn_1 = np.where(n_1<10, 1, 0)
Xm_1 = my_dft(xn_1)

n_2  = np.arange(0, 100)
xn_2 = np.where(n_2<20, 1, 0)
Xm_2 = my_dft(xn_2)

n_3  = np.arange(0, 250)
xn_3 = np.where(n_3<50, 1, 0)
Xm_3 = my_dft(xn_3)


axs = new_subplots(3, 1)

axs[0].plot(n_1, np.abs(Xm_1))
axs[0].set_xlim([0, 50])
axs[0].set_title(r'$|X[m]|$')

axs[1].plot(n_2, np.abs(Xm_2))
axs[1].set_xlim([0, 100])

axs[2].plot(n_3, np.abs(Xm_3))
axs[2].set_xlim([0, 250])

plt.tight_layout()
plt.show()
