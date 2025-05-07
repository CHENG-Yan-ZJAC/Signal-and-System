#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt

from plot_util import *


t   = np.arange(0, 5, 0.01)
x_t = 0.5**t
w   = np.arange(-3*np.pi, 3*np.pi, 0.01)
X_w = -1 / (np.log(0.5) - w*1.0j)

n   = np.arange(0,26)
x_n = 0.5**(0.2*n)
W   = np.arange(-3*np.pi, 3*np.pi, 0.01)
X_W = 1 / (1 - 0.5*np.exp(-1.0j*W))


axs = new_subplots(3, 2)

axs[0][0].plot(t, x_t)
axs[0][0].set_xlim([0, 5])
axs[0][0].set_ylim([0, 1.1])
axs[0][0].set_ylabel(r'$x(t)$')
axs[0][0].set_yticks(np.array([0,0.5,1]), ['0','0.5','1'])

plot_mag_phs(w, np.abs(X_w), np.angle(X_w, deg=True), axs[1][0], axs[2][0],
		w_xlabel=r'$\omega $ (rad/s)', mag_ylabel=r'$|X(\omega)|$', phs_ylabel=r'$\angle X(\omega)$',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-0.5, 2.5], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=1*np.pi)

axs[0][1].stem(n, x_n)
axs[0][1].set_xlim([0, 25])
axs[0][1].set_ylim([0, 1.1])
axs[0][1].set_ylabel(r'$x[n]$')
axs[0][1].set_yticks(np.array([0,0.5,1]), ['0','0.5','1'])

plot_mag_phs(w, np.abs(X_W), np.angle(X_W, deg=True), axs[1][1], axs[2][1],
		w_xlabel=r'$\Omega $ (rad/s)', mag_ylabel=r'$|X(\Omega)|$', phs_ylabel=r'$\angle X(\Omega)$',
		w_xlim=[-3*np.pi, 3*np.pi], mag_ylim=[-0.5, 2.5], phs_ylim=[-220, 220],
		phs_yticks_step=180, w_xticks_step=1*np.pi)

plt.tight_layout()
plt.show()
