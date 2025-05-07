#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from plot_util import *


H = signal.TransferFunction([2], [1,2])
w = np.arange(0.1, 100, 0.01)
w, mag, phase = H.bode(w=w)


fig, axs = plt.subplots(2, 2, figsize=(8,4))

axs[0][0].plot(w, mag)
axs[0][0].set_xlim([0.1, 100])
axs[0][0].set_ylim([-40, 1])
axs[0][0].set_xscale('log')
axs[0][0].set_ylabel(r'$|H(i\omega)|$')
axs[0][0].grid(True)
axs[1][0].plot(w, phase)
axs[1][0].set_xlim([0.1, 100])
axs[1][0].set_ylim([-90, 0])
axs[1][0].set_yticks([-90, -45, 0], ['-90','-45','0'])
axs[1][0].set_xscale('log')
axs[1][0].set_ylabel(r'$\angle H(i\omega)$ (deg)')
axs[1][0].set_xlabel(r'$\omega$ (rad/s)')
axs[1][0].grid(True)
axs[0][1].plot(w, mag)
axs[0][1].set_xlim([0.1, 100])
axs[0][1].set_ylim([-40, 1])
axs[0][1].grid(True)
axs[1][1].plot(w, phase)
axs[1][1].set_xlim([0.1, 100])
axs[1][1].set_ylim([-90, 0])
axs[1][1].set_yticks([-90, -45, 0], ['-90','-45','0'])
axs[1][1].set_xlabel(r'$\omega$ (rad/s)')
axs[1][1].grid(True)

plt.tight_layout()
plt.show()
