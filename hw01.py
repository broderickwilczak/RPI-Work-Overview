# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:25:15 2025

@author: brode
"""

from angles import theta

import math

#print("theta is:",theta)

Given_Force = 500

T_AB = (Given_Force)/(math.cos((65-theta)*(math.pi/180))+(math.sin((65-theta)*(math.pi/180))*math.cos((25+theta)*(math.pi/180)))/math.sin((25+theta)*(math.pi/180)))

T_BC = (-T_AB*math.sin((65-theta)*(math.pi/180)))/(math.sin((25+theta)*(math.pi/180)))

T_AC = (-T_BC*math.cos((25+theta)*(math.pi/180)))/(math.cos((theta)*(math.pi/180)))

Ax = -Given_Force

Cy = -T_AC*math.sin((theta)*(math.pi/180)) - T_BC*math.sin((25+theta)*(math.pi/180))

Ay = -Cy