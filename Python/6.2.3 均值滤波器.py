#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


def mean_filter(N, W):
	H = 1
	for i in range(1, N):
		H = H + np.exp(-1.0j * i * W)
		pass
	H = H / N
	return H

W  = np.arange(-3*np.pi, 3*np.pi, 0.01)
N1 = 2;  H1 = mean_filter(N1, W)
N2 = 5 ; H2 = mean_filter(N2, W)
N3 = 20; H3 = mean_filter(N3, W)


axs = new_subplots(2, 3)

plot_mag_phs(W, np.abs(H1), np.angle(H1, deg=True), axs[0][0], axs[1][0], title='N={}'.format(N1),
		w_xlabel=r'$\Omega $ (rad/s)', mag_ylabel=r'$|H(\Omega)|$', phs_ylabel=r'$\angle H(\Omega)$',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-0.1, 1.1], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=2*np.pi)

plot_mag_phs(W, np.abs(H2), np.angle(H2, deg=True), axs[0][1], axs[1][1], title='N={}'.format(N2),
		w_xlabel=r'$\Omega $ (rad/s)',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-0.1, 1.1], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=2*np.pi)

plot_mag_phs(W, np.abs(H3), np.angle(H3, deg=True), axs[0][2], axs[1][2], title='N={}'.format(N3),
		w_xlabel=r'$\Omega $ (rad/s)',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-0.1, 1.1], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=2*np.pi)

plt.tight_layout()
plt.show()
