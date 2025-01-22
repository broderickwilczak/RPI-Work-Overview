# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:02:19 2025

@author: brode
"""

from math import pi
basetri=.75
height=.75
length=2
half=.5
diameter=2
radius=diameter/2
rectangle=length*height
triangle=half*basetri*height
semicircle=half*pi*radius**2
area=rectangle+semicircle+triangle
print (area)