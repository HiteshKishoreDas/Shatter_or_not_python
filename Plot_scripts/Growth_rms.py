#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import numpy as np

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'
wdir2 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/output/'
wdir3 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/output/'

wdir4 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/output/'
wdir5 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/output/'
wdir6 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/output/'

wdir7 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k10pi/Base/output/'
wdir8 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k10pi/Same_lamT/output/'
wdir9 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k10pi/Same_lamZ/output/'

wdir10 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/output/'
wdir11 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/output/'
wdir12 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/output/'

wdir13 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/output/'
wdir14 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/output/'
wdir15 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/output/'
wdir16 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/output/'

filn = 12
N = 300
M = 0

wi_arr = np.zeros((2,filn),dtype = 'float')

reg = np.zeros((filn,N-M-1,2),dtype=float)

cntwdir = 0
for wdir in [wdir1,wdir2,wdir3,\
             wdir4,wdir5,wdir6,\
             wdir7,wdir8,wdir9,\
             wdir10,wdir11,wdir12]:#,\
             #wdir13,wdir14,wdir15,wdir16]:
    
    nlinf = pp.nlast_info(w_dir=wdir)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    slope = 0
    wi_avg = 0
    
    D0 = pp.pload(0,w_dir=wdir)
    for i in range(M,N):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir) 

        n = int(np.size(D1.x1)/2) 
        diff = (D1.rho[n] - 0.0620)/0.0620
        
        y = np.log(diff)

        x = i*dt/ut
        
        
        if (i==M):
            y0 = y
        else:
            slope = slope + ((y - y0)*ut/dt)**2
            reg[cntwdir,i-M-1,1] = ((y - y0)*ut/dt)**2
            reg[cntwdir,i-M-1,0] = D1.wi[n]**2
            
            y0 = y
            wi_avg = wi_avg + D1.wi[n]
            
    
    wi_arr[0,cntwdir] = wi_avg/(N-M-1)
    wi_arr[1,cntwdir] = np.sign(wi_arr[0,cntwdir])*np.sqrt(slope/(N-M-1))
    cntwdir = cntwdir +1
    
np.save(wdir_script+"/wi_arr",wi_arr)
wi_arrload = np.load(wdir_script+"/wi_arr.npy")