#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *
from my_fourier import *


t    = np.arange(0,50,0.01)
x    = 0.9**t
X, w = my_fourier(x, t)


axs = new_subplots(2, 1)

axs[0].plot(t, x)
axs[0].set_xlim([0, 50])
axs[0].set_ylim([-0.1, 1.1])
axs[0].set_xlabel(r'$t$ (s)')
axs[0].set_ylabel(r'$x(t)$')

axs[1].plot(w, np.abs(X))
axs[1].set_xlim([-2*np.pi, 2*np.pi])
axs[1].set_ylim([-0.1, 10.1])
axs[1].set_xlabel(r'$\omega$ (rad/s)')
axs[1].set_ylabel(r'$|X(\omega)|$')
axs[1].set_xticks(np.array([-2*np.pi,-np.pi,0,np.pi,2*np.pi]), [r'$-2\pi$',r'$-\pi$',r'$0$',r'$\pi$',r'$2\pi$'])

plt.tight_layout()
plt.show()
