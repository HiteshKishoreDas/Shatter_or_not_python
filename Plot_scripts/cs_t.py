#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:20:42 2020

@author: hitesh
"""

import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf
import pyPLUTO as pp

offset_n = 50

colorarr=['tab:red','tab:blue','tab:green','tab:orange']
    
wdir_list = [wd.wdir116]
label_list = ['50000']

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

dt = 1e-6*ut # in Myr

CONST_amu = 1.66053886e-24
CONST_kB = 1.3806505e-16
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


cnt = -1

plt.figure(figsize=(20,20))

for wdir in wdir_list:
    cnt +=1

    nlinf = pp.nlast_info(w_dir=wdir+'output/')

    cs_tcool = np.zeros(nlinf['nlast']+1,dtype=float)

    t_arr = np.zeros(nlinf['nlast']+1,dtype=float)

    for i in range(nlinf['nlast']+1):
        D = pp.pload(i,w_dir=wdir+'output/')   
        
        n = int(np.size(D.x1)/2) + offset_n

        tcool_arr = lf.tcool(D)
        cs_arr = lf.cs(D)
        
        cs_tcool_arr = tcool_arr*cs_arr*ul
        
#        y = cs_tcool[n]
#        x = i*dt/ut

        t_arr[i] = i*dt
        
        cs_tcool[i] = cs_tcool_arr[n]
    #%%

    width = 10

    plt.plot(t_arr,cs_tcool,color=colorarr[cnt],linewidth=width,label=r"c$_s$ t$_{\rm cool}$: "+label_list[cnt])

plt.xlabel('Time (Myr)',fontsize=45)
plt.ylabel(r'ln $\frac{\delta\rho}{\rho_{o}}$',fontsize=45)
plt.tick_params(labelsize=35)
plt.legend(fontsize=30,frameon=False,loc="center right")
plt.savefig('cs_tcool_t.png')
