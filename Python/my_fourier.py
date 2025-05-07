#!/usr/bin/python3


import numpy as np


def my_fourier(x:np.ndarray, t:np.ndarray, w_range:tuple=(-5*np.pi, 5*np.pi), num:int=500) -> tuple:
    w = np.linspace(w_range[0], w_range[1], num+1)
    F = np.zeros_like(w, dtype=np.complex64)
    dt = t[1] - t[0]
    for n in range(F.size):
        F[n] = np.dot(x, np.exp(0-w[n]*t*1.0j)) * dt
        pass
    return (F, w)
