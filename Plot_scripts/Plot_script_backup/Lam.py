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
#matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir4 = plutodir+ 'TI_uniform/metallicity/output/'
wdir5 = plutodir+ 'TI_uniform/metallicity_sec_run/output/'
wdir6 = plutodir+ 'TI_uniform/metallicity_thd_run/output/'



colorarr=['r','b','y']

M = 100
N = 200

plt.figure(figsize=(12,12))
cntwdir = 0
for wdirT in [wdir4,wdir5,wdir6]:
    
    nlinf = pp.nlast_info(w_dir=wdirT)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5
    
    for i in range(M,N):
        D1 = pp.pload(i,w_dir=wdirT)
        n = int(np.size(D1.x1)/2) 

        sim = plt.scatter(i*dt,D1.lamT[n],marker = 'o',s=15,color=colorarr[cntwdir])  
    
    cntwdir = cntwdir+1
    
nmg = r'$\Lambda_{T}$'
nm = 'lamT'
plt.xlabel('Time (in Myr)',fontsize=30)
plt.ylabel(nmg,fontsize=30)
plt.title(nmg,fontsize = 40)
plt.tick_params(labelsize=20)
plt.axis([95,205,0.125,0.320])
#plt.grid()
plt.savefig(wdir_script+'/'+nm+'_linear.png')
plt.close()


plt.figure(figsize=(12,12))
cntwdir = 0
for wdirZ in [wdir4,wdir5,wdir6]:
    
    nlinf = pp.nlast_info(w_dir=wdirZ)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5
    
    for i in range(M,N):
        D1 = pp.pload(i,w_dir=wdirZ)
        n = int(np.size(D1.x1)/2) 

        sim = plt.scatter(i*dt,D1.lamZ[n],marker = 'o',s=15,color=colorarr[cntwdir])  
    
    cntwdir = cntwdir+1
    
nmg = r'$\Lambda_{Z}$'
nm = 'lamZ'
plt.xlabel('Time (in Myr)',fontsize=30)
plt.ylabel(nmg,fontsize=30)
plt.title(nmg,fontsize = 40)
plt.tick_params(labelsize=20)
plt.axis([95,205,0.095,0.165])
#plt.grid()
plt.savefig(wdir_script+'/'+nm+'_linear.png')
plt.close()

#%%