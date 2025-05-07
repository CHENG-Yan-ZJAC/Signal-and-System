#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


w  = np.arange(-50, 50, 0.01)
RC = 1;     H1 = 1 / (1 + RC * w * 1.0j)
RC = 0.1;   H2 = 1 / (1 + RC * w * 1.0j)
RC = 0.001; H3 = 1 / (1 + RC * w * 1.0j)


axs = new_subplots(2, 3)

plot_mag_phs(w, np.abs(H1), np.angle(H1, deg=True), axs[0][0], axs[1][0], title=r"$RC=1$",
		w_xlabel=r'$\omega$ (rad/s)', mag_ylabel=r'$|H(\omega)|$', phs_ylabel=r'$\angle H(\omega)$',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-110, 110], w_xticks_step=10*np.pi)
plot_mag_phs(w, np.abs(H2), np.angle(H2, deg=True), axs[0][1], axs[1][1], title=r"$RC=0.1$",
		w_xlabel=r'$\omega$ (rad/s)',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-110, 110], w_xticks_step=10*np.pi)
plot_mag_phs(w, np.abs(H3), np.angle(H3, deg=True), axs[0][2], axs[1][2], title=r"$RC=0.001$",
		w_xlabel=r'$\omega$ (rad/s)',
		mag_ylim=[-0.1, 1.1], phs_ylim=[-110, 110], w_xticks_step=10*np.pi)

plt.tight_layout()
plt.show()
