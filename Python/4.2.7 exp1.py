#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


w = np.arange(-10*np.pi, 10*np.pi, 0.01)
tau = 0.5; X1 = tau * np.sinc(w*tau / 2 / np.pi)
tau = 1.5; X2 = tau * np.sinc(w*tau / 2 / np.pi)


axs = new_subplots(2, 2)

#plot_mag_phs(w, np.abs(X1), np.angle(X1)/(2*np.pi)*360, axs[0][0], axs[1][0], title=r'$\tau =0.5$',
plot_mag_phs(w, np.abs(X1), np.angle(X1, deg=True), axs[0][0], axs[1][0], title=r'$\tau =0.5$',
		w_xlabel=r'$\omega$ (rad/s)', mag_ylabel=r'$|X(\omega)|$', phs_ylabel=r'$\angle X(\omega)$',
		w_xlim=[-10*np.pi, 10*np.pi], mag_ylim=[-0.2, 2], phs_ylim=[-20, 200],
		phs_yticks_step=180, w_xticks_step=4*np.pi)

plot_mag_phs(w, np.abs(X2), np.angle(X2, deg=True), axs[0][1], axs[1][1], title=r'$\tau =1.5$',
		w_xlabel=r'$\omega$ (rad/s)',
		w_xlim=[-10*np.pi, 10*np.pi], mag_ylim=[-0.2, 2], phs_ylim=[-20, 200],
		phs_yticks_step=180, w_xticks_step=4*np.pi)

plt.tight_layout()
plt.show()
