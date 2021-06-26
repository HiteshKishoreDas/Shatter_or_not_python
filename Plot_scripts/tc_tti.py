#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:25:36 2020

@author: hitesh
"""

import numpy as np
from matplotlib import pyplot as plt

import lamfn as lf
import workdir as wd
#import os
#os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

wdir = wd.wdir102 ############

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

dt = 0.0001*ut#1.0 # in Myr 

nlinf = pp.nlast_info(w_dir=wdir+'output/')

for i in range(nlinf['nlast']+1):
    D = pp.pload(i,w_dir=wdir+'output/')
    
    tcool_arr = lf.tcool(D)*ut
    tti_arr = lf.tti(D)*ut
    
    plt.figure(figsize=(8,8))
    
    plt.yscale('log')
    plt.xlabel('x (kpc)',fontsize=15)
    plt.ylabel('timescale (Myr)',fontsize=15)
    plt.title('t = '+str(np.round(i*dt,4))+' Myr',fontsize=20)
    
    plt.plot(D.x1*ul,tcool_arr,label=r't$_{\rm cool}$')
    plt.plot(D.x1*ul,tti_arr,label=r't$_{\rm TI}$')
    
    plt.legend(fontsize=15)
    
    plt.savefig(wdir+'/Plots_full_log/tc_tti/tc_tti_'+str(i)+'.jpg')
    plt.close()