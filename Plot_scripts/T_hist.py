#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:10:14 2020

@author: hitesh
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

count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir42]:
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
    
    T_cold = 1.0e4
    
#    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    zc = []
    xc = []
    tc = []
    mc = []
    
    N = 0
    
    for i in range(N,N+1):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
#        ln = int(np.size(D1.x1)/2)
#        dln = 30
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        logT = np.log10(T)
        
        dx = D1.x1[1]-D1.x1[0]
        
#        np.histogram(T,bins=100)
        
        plt.figure(figsize=(15,15))
        plt.hist(logT,bins=100)
        plt.xlabel('log T',fontsize=30)
        plt.ylabel(r'# of grids',fontsize=35)
        plt.title(r'Temperature histogram',fontsize=40)
        plt.tick_params(labelsize=25)
#        plt.colorbar()
#        plt.legend(fontsize=25,loc="lower right")
        
        plt.savefig(wdir_script+'/T_hist.png')