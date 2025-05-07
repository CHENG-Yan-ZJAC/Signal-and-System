#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from plot_util import *


H    = signal.lti([1],[1,1])
t, y = signal.step(H, T=np.arange(0,10,0.1))


ax = new_subplots(1, 1)

ax.plot(t, y)
ax.set_xlim([0, 10])
ax.set_ylim([0, 1.1])
ax.set_xlabel(r'$t$ (s)')
ax.set_ylabel(r'$y(t)$')

plt.tight_layout()
plt.show()
