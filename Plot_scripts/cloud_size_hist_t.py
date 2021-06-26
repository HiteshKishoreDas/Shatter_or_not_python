#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:37:03 2020

@author: hitesh
"""
import os
wdir_script = os.getcwd()
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
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


wdir = wd.wdir100
            
nlinf = pp.nlast_info(w_dir=wdir+'output/')

dln = 0

 for t in range(900,nlinf['nlast']):
    
    cloud_s,res = cld.cloud_size(wdir,t,dln,True)
    
    D = pp.pload(t,w_dir=wdir+'output/')
        
    T = D.prs/D.rho*cld.KELVIN*lf.MMWt_mu(D.tr1)
    
    ln = int(np.size(D.x1)/2)
    dln = 3000   #*****************
    
    x1 = D.x1*ul
    
    if len(cloud_s)!=0:
        fig,ax = plt.subplots(2,1,figsize=(12,12))
        
    #    ax[0].set_title(label_arr[cnt],fontsize=25)
                
        ax[0].set_yscale('log')
        ax[0].plot(x1,T)
        ax[0].set_xlabel('x (kpc)',fontsize=20)
        ax[0].set_ylabel('T (K)',fontsize=20)
        ax[0].tick_params(labelsize=15)
        
        cloud_s = np.array(cloud_s)*1000 # in pc
        
        bnw = res*1000/100.
        bin_list = np.arange(min(cloud_s)-5*bnw, max(cloud_s)+5*bnw, bnw)
        hist=np.histogram(cloud_s,bins=bin_list)
        ax[1].plot(hist[1][:-1]+bnw/2.,hist[0],linewidth=3)
        ax[1].scatter(hist[1][:-1]+bnw/2.,hist[0])
        
        ax[1].minorticks_on()
        ax[1].set_xlabel('Cloud size (pc)\nSpatial resolution: '\
          +str(np.round(res*1000,4))+' pc',fontsize=20)
        ax[1].set_ylabel('Count',fontsize=20)
        ax[1].tick_params(labelsize=15)
        
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
        
        ax[0].set_title('t = '+str(np.round(3*dt + (t-3)*0.01*dt,4))+' Myr')
    
    plt.savefig(wdir+'Plots_full_log/cloud_hist/cloud_hist_'+str(t)+'.png')
    plt.close()