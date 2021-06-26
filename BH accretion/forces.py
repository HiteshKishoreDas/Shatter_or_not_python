#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:50:32 2019

@author: Hitesh Kishore Das
"""

import numpy as np
#import scipy as sc
#from matplotlib import pyplot as plt

def grav_force(m1,m2,r1,r2): # Force experienced by particle 1 due to 2 
    #r1 and r2 are arrays
    e = 0.5 #softening length
    
    G = 1.0
    dr = np.abs(r1-r2)    
    dr2 = dr[0]**2 + dr[1]**2
    
    F = -(G*m1*m2/np.power((dr2 + e**2),1.5) ) * (r2 - r1)
    
    return F

def tot_force(m,r,n): # Total force on ith particle
    # m,r are arrays for N particles
    N = np.size(m)
    
    F_tot = np.zeros(2,dtype=float)
    
    for i in range(N):
        if(i==n):
            continue
        else:
            F_tot += grav_force(m[n],m[i],r[n],r[i])
    
    return F_tot
    

#x = np.linspace(0.,10,num=100)
#x1 = np.zeros((2,100),dtype=float)
#x2 = np.zeros((2,100),dtype=float)
#x2[1,:] = np.copy(x)
#y = grav_force(1.,1.,x1,x2)
#
#plt.plot(x,-1*y[1,:])