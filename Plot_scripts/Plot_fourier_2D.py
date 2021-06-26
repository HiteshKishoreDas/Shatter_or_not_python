#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:44:36 2020

@author: hitesh
"""
import os

wdir_script = os.getcwd()
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import fourier as fr

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
title_arr = ['Single eigenmode','Mixed eigenmode','Random noise']

#fig,ax = plt.subplots(1,3,figsize=(40,10))
#ax[0].set_ylabel(r'$E_k$',fontsize=25)

cnt = -1

wdir_list = [[wd.wdir72,wd.wdir73,wd.wdir82,wd.wdir83],\
             [wd.wdir74,wd.wdir75],\
             [wd.wdir76,wd.wdir77],]

wdir_list_test = [wd.wdir72,wd.wdir73]

t_skip = 15
nbin = 20

for wdir_set in wdir_list:    
    cnt+=1
    clr = -1
    for wdir in wdir_set:
        clr +=1
    
        nlinf = pp.nlast_info(w_dir=wdir+'output/')
        
        kt_bin_arr = fr.fourier_kt_imshow(wdir,t_skip,nbin)
    
        plt.figure(figsize=(10,5))
        #plt.axis('off')
        #plt.yscale('symlog')
        plt.title(title_arr[cnt]+': '+label_arr[clr],fontsize=20)
        plt.imshow(kt_bin_arr,vmin=-2,vmax=5,extent=[0,nlinf['nlast'],nbin-2,0],aspect='auto')#,interpolation='none')
        plt.colorbar()
        plt.xlabel('t (Myr)',fontsize=20)
        plt.ylabel('k',fontsize=20)
        plt.savefig(wdir_script+'/Fourier/Fourier2d_'+title_arr[cnt]+'_'+label_arr[clr]+'.png')
    
#
#plt.show()
#plt.close()
    
