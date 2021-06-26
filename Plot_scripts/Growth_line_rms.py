#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd

import pyPLUTO as pp

N = 300
M = 0

lt_isochoric = np.zeros(N-M,dtype=float)
sim_isochoric = np.zeros(N-M,dtype=float)
t_arr = np.zeros(N-M,dtype=float)

wdir_isochoric = wd.wdir116

colorarr=['r','b','g']

wi_arr = np.zeros((2,7),dtype = 'float')
cntwdir = 0
    
wdir = wdir_isochoric

nlinf = pp.nlast_info(w_dir=wdir+'output/')

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
#t = 2.0 * ut  # in Myr
dt = 1e-6*ut # in Myr

m = -0.05
c = 0.5
        
slope = 0
xbar = 0
ybar = 0
xybar = 0
x2bar = 0

wi_avg = 0

offset_n = 50

D0 = pp.pload(0,w_dir=wdir+'output/')

T  = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)
       
lamT_arr = lf.lamT(T,D0.tr1)
tc = lf.tcool(D0)
    
wi = (2.-lamT_arr)/tc

for i in range(M,N):#nlinf['nlast']+1):
    D1 = pp.pload(i,w_dir=wdir+'output/')
    n = int(np.size(D1.x1)/2) + offset_n

    sum = 0.0
    rho_bg = 0.062
    
    rho_avg = np.average(D1.rho)
    rho_rms = np.sqrt(np.average( (D1.rho-rho_avg)**2 ))/rho_avg

    diff = rho_rms
    y = np.log(diff)

    x = i*dt/ut

    t_arr[i-M] = i*dt
    
    lt_isochoric[i-M] = wi[n]*i*dt/ut
    sim_isochoric[i-M] = y


lt_isochoric = lt_isochoric + sim_isochoric[0]

offset = 0#0.25

#%%
plt.figure(figsize=(20,20))

width = 10

plt.plot(t_arr,lt_isochoric + offset,color='tab:blue',linewidth=width+10,label=r"(Dashed) Linear theory")
plt.plot(t_arr,sim_isochoric + offset,color='tab:red',linewidth=width,label=r"(Dashed) Simulation")

plt.xlabel('Time (Myr)',fontsize=45)
plt.ylabel(r'ln $\frac{\rm RMS \delta\rho}{\rho_{avg}}$',fontsize=45)
plt.tick_params(labelsize=35)
plt.legend(fontsize=30,frameon=False,loc="upper left")
plt.savefig('rho_linear_rms.png')