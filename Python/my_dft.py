#!/usr/bin/python3


import numpy as np


def my_dft(x:np.ndarray) -> np.ndarray:
    X = np.zeros_like(x, dtype=np.complex64)
    N = x.size
    n = np.arange(0, x.size)
    for m in range(0, x.size):
        X[m] = np.dot(x, np.exp(0-1.0j*2*np.pi*m*n/N))
    return X


def my_idft(X:np.ndarray) -> np.ndarray:
    x = np.zeros_like(X, dtype=np.float64)
    M = X.size
    m = np.arange(0, X.size)
    for n in range(0, X.size):
        x[n] = np.dot(X, np.exp(0+1.0j*2*np.pi*m*n/M)) / M
        pass
    return x
