# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:59:56 2025

@author: brode
"""

import numpy as np

A = np.load("matrix.npy")

x = np.load("vector.npy")

v = np.zeros(A.shape[0])
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        v[i] += A[i,j]*x[j]
        
np.save("result.npy", v)