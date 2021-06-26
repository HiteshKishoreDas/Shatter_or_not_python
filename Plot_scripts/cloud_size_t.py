#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 06:04:46 2020

@author: hitesh
"""

import os
wdir_script = os.getcwd()
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import cloud_size as cld
import lamfn as lf

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
#t = 2.0 * ut  # in Myr
dt = 0.01*ut # in Myr

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

wdir = wd.wdir100

dln = 512

nlinf = pp.nlast_info(w_dir=wdir+'output/')

clds_min = []
clds_max = []
t_list = []
cs_tc_min = []

for t in range(3,nlinf['nlast']):
    
    cloud_s,res = cld.cloud_size(wdir,t,dln,True)
    
    if len(cloud_s) !=0:
        clds_min.append(np.min(cloud_s))
        clds_max.append(np.max(cloud_s))
        t_list.append(3*dt+(t-3)*0.01*dt)
#        t_list.append(t*dt)
        
        D = pp.pload(t,w_dir=wdir+'output/')
        
        n_H = D.rho*UNIT_DENSITY/(lf.MMWt_muH(D.tr1)*CONST_amu)
        T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1)    
    
        lam = lf.lam(T,D.tr1)
        
        q = n_H*n_H*lam/unit_q
        tc = D.prs/(q*(gamma - 1))
        cs = np.sqrt(D.prs/D.rho)
    
        cs_tc_min.append(np.min(tc*cs*ul*1000))

t_list = np.array(t_list)        
res_list = np.zeros_like(t_list) + res*1000
clds_min = np.array(clds_min)
clds_max = np.array(clds_max)

plt.figure(figsize=(10,10))
#plt.yscale('log')
plt.plot(t_list,clds_min*1000,label='Min. cloud size')
plt.plot(t_list,clds_max*1000,label='Max. cloud size')
plt.plot(t_list,res_list,linestyle='dashed',c='k',label='Resolution')
plt.plot(t_list,cs_tc_min,c='k',label=r'c$_{s}$t$_{cool}$')

plt.xlabel('time (Myr)',fontsize=20)
plt.ylabel('Cloud size (pc)',fontsize=20)
plt.legend(fontsize=15)
plt.tick_params(labelsize=15)

plt.ylim (0.,2.5)
#plt.xlim(545,550)

plt.savefig(wdir+'Plots_full_log/cloud_size_t_fast.png')
