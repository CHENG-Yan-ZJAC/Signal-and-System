#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


w  = np.arange(-50, 50, 0.01)
X  = (np.sin(w/2) / (w/2))
RC = 0.5;   Y1 = 1 / (1 + RC * w * 1.0j) * (np.sin(w/2) / (w/2))
RC = 0.001; Y2 = 1 / (1 + RC * w * 1.0j) * (np.sin(w/2) / (w/2))


axs = new_subplots(2, 3)

plot_mag_phs(w, np.abs(X),  np.angle(X, deg=True),  axs[0][0], axs[1][0], title='signal',
		w_xlabel=r'$\omega$ (rad/s)', mag_ylabel=r'$|X(\omega)|$', phs_ylabel=r'$\angle X(\omega)$',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-200, 200], w_xticks_step=10*np.pi)
plot_mag_phs(w, np.abs(Y1), np.angle(Y1, deg=True), axs[0][1], axs[1][1], title='response, RC=0.5',
		w_xlabel=r'$\omega$ (rad/s)', mag_ylabel=r'$|Y(\omega)|$', phs_ylabel=r'$\angle Y(\omega)$',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-200, 200], w_xticks_step=10*np.pi)
plot_mag_phs(w, np.abs(Y2), np.angle(Y2, deg=True), axs[0][2], axs[1][2], title='response, RC=0.001',
		w_xlabel=r'$\omega$ (rad/s)', mag_ylabel=r'$|Y(\omega)|$', phs_ylabel=r'$\angle Y(\omega)$',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-200, 200], w_xticks_step=10*np.pi)

plt.tight_layout()
plt.show()
