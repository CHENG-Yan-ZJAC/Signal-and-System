#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_dft import *


n_1  = np.arange(0, 10)
xn_1 = np.ones(10)
Xm_1 = my_dft(xn_1)

n_2  = np.arange(0, 20)
xn_2 = np.where(n_2<10, 1, 0)
Xm_2 = my_dft(xn_2)

n_3  = np.arange(0, 110)
xn_3 = np.where(n_3<10, 1, 0)
Xm_3 = my_dft(xn_3)


axs = new_subplots(3, 1)

axs[0].stem(n_1, np.abs(Xm_1))
axs[0].set_xlim([0, 9])
axs[0].set_ylim([-0.5, 10.5])
axs[0].set_title(r'$|X[m]|$')

axs[1].stem(n_2, np.abs(Xm_2))
axs[1].set_xlim([0, 19])
axs[1].set_ylim([-0.5, 10.5])

axs[2].stem(n_3, np.abs(Xm_3))
axs[2].set_xlim([0, 109])
axs[2].set_ylim([-0.5, 10.5])

plt.tight_layout()
plt.show()
