#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:13:27 2020

@author: hitesh
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import fourier as fr

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
#ut = ((ul * 3.086E+21)/uv)  # in s
#ut = (ut / 3.154e+13)    # in Myr

ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 1.0 # in Myr

count = 2
c_arr = ['tab:red','tab:blue','tab:red','tab:blue']
ls_arr = ['solid','solid','dashed','dashed']
mark_arr = ['o','^','o','^']
label_arr = ['Unstable','Stable','Unstable (periodic)','Stable (periodic)']
title_arr = ['Pure eigenmode','Mixed eigenmode','Random noise']

fig,ax = plt.subplots(1,3,figsize=(40,10))
ax[0].set_ylabel(r'$E_k$',fontsize=25)

cnt = 0

for wdir_arr in [[wd.wdir72,wd.wdir73,wd.wdir82,wd.wdir83],\
                 [wd.wdir74,wd.wdir75],\
                 [wd.wdir76,wd.wdir77],]:
    
    ax[cnt].set_xscale('log')
    ax[cnt].set_yscale('log')
    
    ax[cnt].tick_params(labelsize=20)
    
    ax[cnt].set_xlabel(r'k',fontsize=25)
    ax[cnt].set_title(title_arr[cnt],fontsize=30)
    
    clr = 0
    
    for wdir in wdir_arr:
        nlinf = pp.nlast_info(w_dir=wdir)
        E_arr,k_bin = fr.fourier_bin(wdir,nlinf['nlast'])
        
        ax[cnt].plot(k_bin,E_arr,c=c_arr[clr],linewidth=3,linestyle=ls_arr[clr],label=label_arr[clr]+str(' (')+str(t*dt)+' Myr)')
        ax[cnt].scatter(k_bin,E_arr,c=c_arr[clr],marker=mark_arr[clr],s=50)
        
        clr +=1 
    
    ax[cnt].legend(fontsize=20)
    
    cnt+=1

plt.savefig(wdir_script+'/Fourier.png')
plt.show()
plt.close()

