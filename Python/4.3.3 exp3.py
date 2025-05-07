#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from my_fourier import *
from plot_util import *


t    = np.arange(-20, 20, 0.01)
x    = np.where(t<-1, 0, np.where(t<1, 2, np.where(t<2, 1, 0)))
X, w = my_fourier(x, t, w_range=(-6*np.pi, 6*np.pi))


axs = new_subplots(3, 1)

axs[0].plot(t, x)
axs[0].set_xlim([-20, 20])
axs[0].set_ylim([-0.2, 2.2])
axs[0].set_xlabel(r'$t$')
axs[0].set_ylabel(r'$x(t)$')

plot_mag_phs(w, np.abs(X), np.angle(X, deg=True), axs[1], axs[2],
		mag_ylabel=r'$|X(\omega)|$', phs_ylabel=r'$\angle X(\omega)$',
		w_xlim=[-6*np.pi, 6*np.pi], mag_ylim=[-2, 6], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=2*np.pi)

plt.tight_layout()
plt.show()
