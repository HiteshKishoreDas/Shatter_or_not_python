#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:55:05 2020

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

labelsize=40
ticksize=35
titlesize=45 
offsetsize=35

count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

sim_list = ['Unstable isobaric mode','Unstable isochoric mode','Stable isochoric mode']
sub_list = ['(a)','(b)','(c)']

cnt = -1
fig, ax = plt.subplots(1,3,figsize=(50,15))
for wdir in [wd.wdir58,wd.wdir72,wd.wdir73]:
    cnt +=1
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    ut = ((ul * 3.086E+21)/uv)  # in s
    ut = (ut / 3.154e+13)    # in Myr
    
#    ut = 100 # in Myr
#    t = 2.0 * ut  # in Myr
    dt = ut*0.01 # in Myr
    
    m = -0.01
    c = 0.5
    
    noch = 0.5
    
    T_cold = 10**4.1
    
#    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    zc = []
    xc = []
    tc = []
    mc = []
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    lam0 =  np.zeros(np.size(D0.x1),dtype=float)

    n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1,D0.tr2)*CONST_amu)
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)
    for i in range(np.size(D0.x1)):
        lam0[i] = lf.lam(T0[i],D0.tr1[i])
    q0 = n_H0*n_H0*lam0/unit_q
    tc0 = D0.prs/(q0*(gamma - 1))
    tc_min = np.min(tc0)*ut
    
    ln = int(np.size(D0.x1)/2)
    if cnt!=0:
        dln = 3000
    else:
        dln = 1500
    
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1,D1.tr2)
        dx = D1.x1[1]-D1.x1[0]
        
        x1 = D1.x1[ln-dln:ln+dln]
        T = T[ln-dln:ln+dln]
        rho = D1.rho[ln-dln:ln+dln]
        tr1 = D1.tr1[ln-dln:ln+dln]
        
        for j in range(np.size(x1)):
            if (T[j] < T_cold):
               xc.append(x1[j]*ul)
               zc.append(tr1[j])
               tc.append(i*dt/tc_min)
               mc.append(rho[j]*dx)

    cz = np.array(zc)
    tc = np.array(tc)
    xc = np.array(xc)
    mc = np.array(mc)
    
    scat = ax[cnt].scatter(tc,xc,c=zc,cmap='magma',vmin=0.3,vmax=0.6)
    
    ax[cnt].set_xlabel(r't ($\times t_{\rm cool}$)',fontsize=labelsize)
    ax[cnt].set_ylabel(r'x (kpc)',fontsize=labelsize)
    ax[cnt].set_title(sim_list[cnt],fontsize=titlesize)
    ax[cnt].tick_params(labelsize=ticksize)
    
cbar = fig.colorbar(scat)
cbar.ax.tick_params(labelsize=ticksize)
cbar.set_label(label='Metallicity',fontsize=labelsize)
#plt.legend(fontsize=25,loc="lower right")

plt.savefig(wdir_script+'/cold_mass/cold_mass_xt.png')