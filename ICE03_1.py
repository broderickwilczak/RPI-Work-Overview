# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:59:15 2025

@author: brode
"""

import numpy as np

import math

u = np.array([0.5, -0.6, 1.3])

abs_u = 0

for number in u:
    abs_u += number**2

u /= math.sqrt(abs_u)

print (u)