# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:43:14 2025

@author: brode
"""

# 1. function k_vector (z)

import numpy as np

def k_vector(z):
    
    """Inputing a scalar value will be converted to a vector with
    a z component equal to said scalar
    
    Insert value z into function to receive an array based on z"""
    
    t = np.array([0.0, 0.0, z ])
    
    return(t)

#k_vector(4.5)

# 2. function vector_sum(u, v)

def vector_sum(u, v):
    
    """inputting two vectors, 
    
    v and u respectively, will generate 
    vector addition between both vectors"""
    
    w = np.zeros(u.shape[0])

    for i in range(u.shape[0]):
        w[i] += u[i] + v[i]
    return(w)

u = np.array([1.0, 3.0, 5.0])

v = np.array([2.0, 4.0, 6.0])
    
#vector_sum(u, v)

# 3. Function to compute the cross product of two vectors manually
def vector_cross_product(a, b):
    """Inputting two vectors, a and b, 
    
    
    will generate a cross product between both vectors."""
    # Manually compute the cross product using the formula
    cross = np.array([ 
        a[1] * b[2] - a[2] * b[1], 
        a[2] * b[0] - a[0] * b[2], 
        a[0] * b[1] - a[1] * b[0]
    ])
    return cross

# 4. Function to compute the vector triple product
def vector_triple_product(a, b, c):
    """Manually compute the vector 
    
    
    triple product a x (b x c)."""
    # Step 1: Compute the cross product of b and c manually
    cross_bc = vector_cross_product(b, c)
    
    # Step 2: Compute the dot product of a with b and a with c manually
    dot_ab = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]  # a . b
    dot_ac = a[0] * c[0] + a[1] * c[1] + a[2] * c[2]  # a . c
    
    # Step 3: Apply the vector triple product formula
    result = dot_ac * b - dot_ab * c
    
    return result

# Test vectors
a = np.array([1.0, 2.0, 3.0])
b = np.array([3.0, 2.0, 1.0])
c = np.array([2.0, 2.0, 2.0])

# Compute the vector triple product
vtp = vector_triple_product(a, b, c)
print("Vector Triple Product:", vtp)