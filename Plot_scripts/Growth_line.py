#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

N = 300
M = 0

lt_isobaric = np.zeros(N-M,dtype=float)
lt_isochoric = np.zeros(N-M,dtype=float)
sim_isobaric = np.zeros(N-M,dtype=float)
sim_isochoric = np.zeros(N-M,dtype=float)
t_arr = np.zeros(N-M,dtype=float)

wdir_isobaric = wd.wdir56
wdir_isochoric = wd.wdir61

offset_n = 50

colorarr=['r','b','g']

wi_arr = np.zeros((2,7),dtype = 'float')
cntwdir = 0
for iso in [0,1]:
    
    if (iso == 0):
        wdir = wdir_isobaric
    else:
        wdir = wdir_isochoric
    
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    ut = ((ul * 3.086E+21)/uv)  # in s
    ut = (ut / 3.154e+13)    # in Myr
    
    #ut = 100 # in Myr
    #t = 2.0 * ut  # in Myr
    dt = 0.01*ut # in Myr
    
    m = -0.05
    c = 0.5
          
    slope = 0
    xbar = 0
    ybar = 0
    xybar = 0
    x2bar = 0
    
    wi_avg = 0

    D0 = pp.pload(0,w_dir=wdir+'output/')
    for i in range(M,N):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/')
 
        
        n = int(np.size(D1.x1)/2) + offset_n
        diff = np.abs((D1.rho[n] - 0.0620))/0.0620
        
        y = np.log(diff)
#        print (diff)
        x = i*dt/ut
            
        if (iso == 0):
            lt_isobaric[i-M] = D1.wi[n]*i*dt/ut
            sim_isobaric[i-M] = y
            t_arr[i-M] = i*dt
        else:
            lt_isochoric[i-M] = D1.wi[n]*i*dt/ut
            sim_isochoric[i-M] = y
#            print (y)
        
#        print(np.log(diff),diff)    

#%%

#sim_isobaric = sim_isobaric - sim_isobaric[0]
#sim_isochoric = sim_isochoric - sim_isochoric[0]

lt_isobaric = lt_isobaric + sim_isobaric[0]
lt_isochoric = lt_isochoric + sim_isochoric[0]

offset = 0#0.25

#%%
plt.figure(figsize=(20,20))

width = 10

plt.plot(t_arr,lt_isobaric,color='tab:blue',linewidth=width+15,label=r"(Solid)     Linear theory: Isobaric  k=$2\pi/(2~\rm kpc)$")
plt.plot(t_arr,sim_isobaric,color='tab:red',linewidth=width,label=r"(Solid)     Simulation    : Isobaric  k=$2\pi/(2~\rm kpc)$")

plt.plot(t_arr,lt_isochoric + offset,color='tab:blue',linestyle='--',linewidth=width+10,label=r"(Dashed) Linear theory: Isochoric k=$2\pi/(20~\rm Mpc)$")
plt.plot(t_arr,sim_isochoric + offset,color='tab:red',linestyle='--',linewidth=width,label=r"(Dashed) Simulation    : Isochoric k=$2\pi/(20~\rm Mpc)$")


#plt.legend((lt, sim),
#           ('Linear theory', 'Simulation'),
#           scatterpoints=1,
#           loc='lower right', markerscale=5,
#           ncol=1,
#           fontsize=20)
#
plt.xlabel('Time (Myr)',fontsize=45)
plt.ylabel(r'ln $\frac{\delta\rho}{\rho_{o}}$',fontsize=45)
#plt.title(r'ln $\frac{\delta\rho}{\rho_{o}}$ vs. time',fontsize=50)
plt.tick_params(labelsize=35)
plt.legend(fontsize=30,frameon=False,loc="upper left")
plt.savefig(wdir_script+'/rho_linear.png')