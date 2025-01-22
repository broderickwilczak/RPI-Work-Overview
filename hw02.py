# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:59:39 2025

@author: brode
"""

# 1. initial mechanism and simulaton data

import numpy as np

linklengths = np.array([0.4, 0.2, 0.1 ])

    # angle

theta0 = np.array([0.0, 0.0, 0.0 ])

    # angular velocity

omega0 = np.array([0.5, 0.1, 0.1 ])

num_links = len(omega0)

    # angular acceleration

alpha0 = np.array([0.0, -0.15, 0.0 ])

    # time

total_duration = 8.0

num_steps = 100

interval_size = total_duration / num_steps

time_moments = np.arange(0.0, total_duration + interval_size, interval_size)

num_rows = len(time_moments)

# 2. angular kinematics

    # alpha

alpha = np.zeros((num_rows, 3))

for i in range(num_rows):
    alpha[i] = alpha0

#print(alpha)

    # omega

omega = np.zeros((num_rows, num_links))

for i, t in enumerate(time_moments):
    for j in range(num_links):
        omega[i, j] = omega0[j] + alpha0[j] * t

#print(omega)

    # theta

theta = np.zeros((num_rows, num_links))

for i, t in enumerate(time_moments):
    for j in range(num_links):
        theta[i, j] = theta0[j] + omega0[j] * t + 0.5 * alpha0[j] * t**2
        
#print(theta)

# 3. cartesian kinematics

    #RR array
    
RR = np.zeros((num_rows, num_links + 1, 3))

RR[:, 0, :] = [0.0, 0.0, 0.0]

for i, t in enumerate(time_moments):
    for j in range(1, num_links + 1):
        x = np.sum(linklengths[:j] * np.cos(np.cumsum(theta[i, :j])))
        y = np.sum(linklengths[:j] * np.sin(np.cumsum(theta[i, :j])))
        RR[i, j, :] = [x, y, 0.0]
        
#print(RR)

# Invoke the following from the command prompt to 
# see the animation:  >>> %matplotlib qt
L = 0.0 
dt = 0.0
DISPLAY = False
ANIMATE = False
# ============================================================ 
# VISUALIZATIONS 
# ============================================================ 
# 
if (DISPLAY): 
    from hw02_display import plot_3_trajectories 
    plot_3_trajectories(RR, L) 
if (ANIMATE): 
    # Execute ">>> %matplotlib qt" at the command prompt 
    # to observe the animation in a separate window 
    import matplotlib.pyplot as plt 
    from hw02_display import animate_3_links 
    anim = animate_3_links(RR, L, dt) 
    plt.show()


        