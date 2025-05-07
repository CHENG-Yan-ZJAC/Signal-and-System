#!/usr/bin/python3


import numpy as np


def my_diff(An:np.ndarray, Yn:np.ndarray, Bm:np.ndarray, Xm:np.ndarray, b:float, X:np.ndarray) -> np.ndarray:
    Yn = np.flipud(Yn)
    Xm = np.flipud(Xm)
    Y = np.zeros_like(X)
    for i in range(X.shape[0]):
        Y[i] = b*X[i] + np.dot(Bm, Xm) - np.dot(An, Yn)
        Yn = np.append(Yn, Y[i])[1:]
        Xm = np.append(Xm, X[i])[1:]
        pass
    return Y
