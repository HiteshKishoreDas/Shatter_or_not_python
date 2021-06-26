#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:35:12 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

plt.figure(figsize=(15,15))
count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir17]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.01
    c = 0.5
    
    peak = 0.0
    
#    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
#        ln = int(np.size(D1.x1)/2)
#        dln = 30
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        
        dx = D1.x1[1]-D1.x1[0]
        
        m_tot = np.sum(np.multiply(D1.rho,dx))
        
        m_cold_arr = np.zeros(np.size(D1.x1),dtype=float)
        m_hot_arr = np.zeros(np.size(D1.x1),dtype=float)
        
        for j in range(np.size(D1.x1)):
            if (T[j] < 1e4):
                m_cold_arr[j] = D1.rho[j]*dx
                m_hot_arr[j] = 0.0
            else:
                m_hot_arr[j] = D1.rho[j]*dx
                m_cold_arr[j] = 0.0
        
        m_cold = np.sum(m_cold_arr)
        m_hot = np.sum(m_hot_arr)
        
        plt.scatter(i*dt/ut*100,m_cold/m_tot,color='tab:blue')
#        plt.scatter(i*dt/ut,m_hot,color='tab:red')
        
plt.xlabel('Time (in Myr)',fontsize=30)
plt.ylabel(r'Cold mass fraction',fontsize=35)
plt.title(r'Cold mass fraction vs. time',fontsize=40)
plt.tick_params(labelsize=25)
#plt.legend(fontsize=25,loc="lower right")

plt.savefig(wdir_script+'/Cold_mass.png')