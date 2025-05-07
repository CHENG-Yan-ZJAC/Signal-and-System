#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


W = np.arange(-3*np.pi, 3*np.pi, 0.01)
T = 1;    X_1 = 1 / (1 - (-0.5)**T * np.exp(-1.0j*W))
T = 0.2;  X_2 = 1 / (1 - (-0.5)**T * np.exp(-1.0j*W))
T = 0.05; X_3 = 1 / (1 - (-0.5)**T * np.exp(-1.0j*W))


axs = new_subplots(2, 1)

plot_mag_phs(W, np.abs(X_1), np.angle(X_1, deg=True), axs[0], axs[1],
		mag_line_fmt='-', phs_line_fmt='-', mag_line_label='T=1', phs_line_label='T=1',
		w_xlabel=r'$\Omega $ (rad/s)', mag_ylabel=r'$|X(\Omega)|$', phs_ylabel=r'$\angle X(\Omega)$',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-5, 35], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=1*np.pi)

plot_mag_phs(W, np.abs(X_2), np.angle(X_2, deg=True), axs[0], axs[1],
		mag_line_fmt='g-.', phs_line_fmt='g-.', mag_line_label='T=0.2', phs_line_label='T=0.2')

plot_mag_phs(W, np.abs(X_3), np.angle(X_3, deg=True), axs[0], axs[1],
		mag_line_fmt='r--', phs_line_fmt='r--', mag_line_label='T=0.05', phs_line_label='T=0.05')

plt.legend()
plt.tight_layout()
plt.show()
