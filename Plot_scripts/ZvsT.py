#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:51:50 2020

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

count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir56]:
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
    
    noch = 0.5
    
    T_cold = 10**4.1
    
#    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    z = []
    x = []
    T = []
    t = []
    
    for i in range(0,nlinf['nlast']+1,20):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
#        ln = int(np.size(D1.x1)/2)
#        dln = 30
        
        Temp  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        
        for j in range(np.size(D1.x1)):
            x.append(D1.x1[j]*ul)
            z.append(D1.tr1[j])
            t.append(i*dt/ut*100)
            T.append(Temp[j])
           
#        plt.scatter(i*dt/ut*100,m_cold/m_tot,color='tab:blue')
#        plt.scatter(i*dt/ut,m_hot,color='tab:red')

z = np.array(z)
T = np.array(T)
x = np.array(x)
t = np.array(t)

#%%

#fig, ax = plt.subplots(figsize=(15,15))
#
#scat = ax.scatter(T,z,c=t,cmap='magma')
#
#plt.xscale("log")
#plt.xlabel('T (K)',fontsize=35)
#plt.ylabel(r'Z ($Z_\odot$)',fontsize=35)
#plt.title(r'Z vs. T in isobaric regime',fontsize=40)
#ax.tick_params(labelsize=30)
#
#cbar = fig.colorbar(scat)
#cbar.ax.tick_params(labelsize=20)
#cbar.set_label(label='Time (Myr)',fontsize=30)
##plt.legend(fontsize=25,loc="lower right")
#
#plt.savefig(wdir_script+'/ZTt_isobaric.png')

#%%

fig, ax = plt.subplots(figsize=(15,15))

scat = ax.scatter(T,z,c=t,cmap='magma')

plt.xscale("log")
plt.xlabel('T (K)',fontsize=35)
plt.ylabel(r'Z ($Z_\odot$)',fontsize=35)
plt.title(r'Z vs. T in isochoric regime',fontsize=40)
ax.tick_params(labelsize=30)

cbar = fig.colorbar(scat)
cbar.ax.tick_params(labelsize=20)
cbar.set_label(label='Time (Myr)',fontsize=30)
#plt.legend(fontsize=25,loc="lower right")

plt.savefig(wdir_script+'/ZTt_isochoric_ST2.png')
