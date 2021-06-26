#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib.pyplot as plt

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'
wdir2 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/output/'
wdir3 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/output/'

wdir4 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/output/'
wdir5 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/output/'
wdir6 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/output/'

wdir7 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/output/'
wdir8 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/output/'
wdir9 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/output/'
wdir10 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/output/'

wdir11 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/output/'
wdir12 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/output/'
wdir13 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/output/'

wdir14 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Base/output/'
wdir15 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamT/output/'
wdir16 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamZ/output/'


N = 500
M = 0

lt_isobaric = np.zeros(N-M,dtype=float)
lt_isochoric = np.zeros(N-M,dtype=float)
sim_isobaric = np.zeros(N-M,dtype=float)
sim_isochoric = np.zeros(N-M,dtype=float)
t_arr = np.zeros(N-M,dtype=float)

wdir_isobaric = wdir3
wdir_isochoric = wdir6

colorarr=['r','b','g']

wi_arr = np.zeros((2,7),dtype = 'float')
cntwdir = 0
for iso in [0,1]:
    
    if (iso == 0):
        wdir = wdir_isobaric
    else:
        wdir = wdir_isochoric
    
    nlinf = pp.nlast_info(w_dir=wdir)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5
          
    slope = 0
    xbar = 0
    ybar = 0
    xybar = 0
    x2bar = 0
    
    wi_avg = 0
    
    D0 = pp.pload(0,w_dir=wdir)
    for i in range(M,N):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir)
 
        
        n = int(np.size(D1.x1)/2)
        diff = (D1.rho[n] - 0.0620)/0.0620
        
        y = np.log(diff)

        x = i*dt/ut
            
        if (iso == 0):
            lt_isobaric[i-M] = D1.wi[n]*i*dt/ut
            sim_isobaric[i-M] = y
            t_arr[i-M] = i*dt/ut*100
        else:
            lt_isochoric[i-M] = D1.wi[n]*i*dt/ut
            sim_isochoric[i-M] = y
        
#        print(np.log(diff),diff)    



sim_isobaric = sim_isobaric - sim_isobaric[0]
sim_isochoric = sim_isochoric - sim_isochoric[0]

offset = 0.25

plt.figure(figsize=(16,16))

width = 8

#plt.plot(t_arr,lt_isobaric,color='b',linewidth=width+1,label=r"Linear theory: Isobaric k=$100\pi$")
#plt.plot(t_arr,sim_isobaric,color='r',linewidth=width,label=r"Simulation: Isobaric k=$100\pi$")

plt.plot(t_arr,lt_isochoric + c,color='b',linestyle='--',linewidth=width+1,label=r"Linear theory: Isochoric k=$0.01\pi$")
plt.plot(t_arr,sim_isochoric + c,color='r',linestyle='--',linewidth=width,label=r"Simulation: Isochoric k=$0.01\pi$")


#plt.legend((lt, sim),
#           ('Linear theory', 'Simulation'),
#           scatterpoints=1,
#           loc='lower right', markerscale=5,
#           ncol=1,
#           fontsize=20)
#
plt.xlabel('Time (in Myr)',fontsize=40)
plt.ylabel(r'log $\frac{\delta\rho}{\rho_{o}}$',fontsize=45)
plt.title(r'$\frac{\delta\rho}{\rho_{o}}$ vs. time',fontsize=50)
plt.tick_params(labelsize=35)
plt.legend(fontsize=25,loc="lower right")
#plt.savefig(wdir_script+'/rho_linear.png')