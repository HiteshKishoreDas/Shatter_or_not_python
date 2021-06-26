#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

Nz = 6
NT = 50
Z_arr = np.linspace(0.2,0.7,num = Nz)
T_arr = np.logspace(6,8,num=NT)
q0_arr = np.zeros(NT,dtype=float)
tc0_arr = np.zeros(NT,dtype=float)
w_arr = np.zeros(NT,dtype=float)

gamma = 5./3.
plutodir = os.environ['PLUTO_DIR']
wdir = wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'

D0 = pp.pload(0,w_dir=wdir)

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH

fig = plt.figure(figsize=(12,12))
for Z in Z_arr:
    p0 = D0.prs[0]
    rho0 = D0.rho[0]
    n_H = rho0*UNIT_DENSITY/(lf.MMWt_muH(Z)*CONST_amu)
    for i in range(np.size(T_arr)):
        lam = lf.lam(T_arr[2],Z)
        q0_arr[i] = n_H*n_H*lf.lam(T_arr[i],Z)/unit_q
        tc0_arr[i] = p0/(q0_arr[i]*(gamma - 1))
        w_arr[i] = (2-lf.lamT(T_arr[i],Z))/gamma*tc0_arr[i]
    plt.plot(T_arr,w_arr,label='Z = ' + str(Z),linewidth = 2)
    
plt.xscale('log')
plt.xlabel('Temperature (in K)',fontsize=30)
plt.ylabel(r'$\frac{1}{t_{\rm TI}}$',fontsize=35)
plt.title(r'$\frac{1}{t_{\rm TI}}$ vs. T',fontsize=40)
plt.legend(fontsize = 25)
plt.tick_params(labelsize=25)
plt.savefig(wdir_script+'/t_TI.png')