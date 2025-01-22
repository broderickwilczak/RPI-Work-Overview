# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:57:42 2025

@author: brode
"""

import numpy as np

submitty = True

if (submitty):
    data_array = np.load("data.npy")

else:
    data_array = np.array([104.1, 188.0, 200.0, 291.0])

Bin_0 = 0

Bin_1 = 0

Bin_2 = 0

Bin_3 = 0

Bin_4 = 0

for item in data_array:
    if item < 185.0:
        Bin_0 += 1
    elif item >= 185.0 and item < 195.0:
        Bin_1 += 1
    elif item >= 195.0 and item < 205.0:
        Bin_2 += 1
    elif item >= 205.0 and item < 215.0:
        Bin_3 += 1
    elif item >= 215.0:
        Bin_4 += 1

print(Bin_0)

print(Bin_1)

print(Bin_2)

print(Bin_3)

print(Bin_4)