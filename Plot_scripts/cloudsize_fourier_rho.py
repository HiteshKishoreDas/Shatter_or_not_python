#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 02:21:37 2020

@author: hitesh
"""
import os
wdir_script = os.getcwd()
import numpy as np
import matplotlib.pyplot as plt
import cloud_size as cld
import lamfn as lf
import fourier as fr
#import pandas as pd

#os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp
import workdir as wd
#plutodir = os.environ['PLUTO_DIR']

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
#t = 2.0 * ut  # in Myr
dt = 0.0001*ut # in Myr   #******************

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

wdir_list = [wd.wdir72,wd.wdir73]
wtag_list = ['20k','50k']
dln = 512 # Not used if periodic

fig = plt.figure(figsize=(15,10))
#fig,ax = plt.subplots(2,3,figsize=(60,40))

ax1 = fig.add_axes([0.05, 0.1, 0.25, 0.4])
ax2 = fig.add_axes([0.35, 0.1, 0.25, 0.4])
ax3 = fig.add_axes([0.65, 0.1, 0.3, 0.4])

ax4 = fig.add_axes([0.05, 0.5, 0.25, 0.4])
ax5 = fig.add_axes([0.35, 0.5, 0.25, 0.4])
ax6 = fig.add_axes([0.65, 0.5, 0.3, 0.4])

ax = [[ax1,ax2,ax3],[ax4,ax5,ax6]]

for wtag_i,wdir in enumerate(wdir_list):
    
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ###### Density plots ######
    
    for i in range(1,5):
        n1 = int(i*nlinf['nlast']/4.0)
        D = pp.pload(n1,w_dir=wdir+'output/')
        ax[wtag_i][0].plot(D.x1,D.rho,label='t = '+str(np.round(n1*dt,6))+' Myr')

        if wtag_i==1:
            ax[wtag_i][0].legend(fontsize=10)
        else:
            ax[wtag_i][0].set_xlabel('x (kpc)',fontsize=15)
    
    ###### Fourier plots ######
    
    for j in range(1,5):
        n2 = int(j*nlinf['nlast']/4.0)
        E_arr,k_bin = fr.fourier_bin(wdir,n2)
        ax[wtag_i][1].plot(k_bin,E_arr,label='t = '+str(np.round(n2*dt,6))+' Myr')
        ax[wtag_i][1].scatter(k_bin,E_arr)
        
        ax[wtag_i][1].set_xscale('log')
        ax[wtag_i][1].set_yscale('log')
    
    ###### Cloud size plots ######    
    
    clds_min = []
    clds_max = []
    t_list = []
    cs_tc_min = []
    
    for t in range(0,nlinf['nlast']):
        
        cloud_s,res = cld.cloud_size(wdir,t,dln,True)
        
        D = pp.pload(t,w_dir=wdir+'output/')
        
        if len(cloud_s) !=0:
            clds_min.append(np.min(cloud_s))
            clds_max.append(np.max(cloud_s))
            t_list.append(t*dt)
            
            n_H = D.rho*UNIT_DENSITY/(lf.MMWt_muH(D.tr1,D.tr2)*CONST_amu)
            T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)    
        
            lam = lf.lam(T,D.tr1)
            
            q = n_H*n_H*lam/unit_q
            tc = D.prs/(q*(gamma - 1))
            cs = np.sqrt(D.prs/D.rho)
        
            cs_tc_min.append(np.min(tc*cs*ul))
    
    t_list = np.array(t_list)        
    res_list = np.zeros_like(t_list) + res*1000    # in pc
    clds_min = np.array(clds_min)*1000
    clds_max = np.array(clds_max)*1000
    cs_tc_min = np.array(cs_tc_min)*1000
    
#    np.save('array_output/t_list'+wtag_list[wtag_i],t_list)
#    np.save('array_output/res_list'+wtag_list[wtag_i],res_list)
#    np.save('array_output/clds_min'+wtag_list[wtag_i],clds_min)
#    np.save('array_output/clds_max'+wtag_list[wtag_i],clds_max)
#    np.save('array_output/cs_tc_min'+wtag_list[wtag_i],cs_tc_min)
    
    ax[wtag_i][2].set_yscale('log')
    ax[wtag_i][2].plot(t_list,clds_min,label='Min. cloud size',c='b',linestyle=':')
    ax[wtag_i][2].plot(t_list,clds_max,label='Max. cloud size',c='r',linestyle=':')
    ax[wtag_i][2].plot(t_list,cs_tc_min,c='k',label=r'c$_{s}$t$_{cool}$',linestyle=':')
    ax[wtag_i][2].plot(t_list,res_list,linestyle='dashed',c='k',label='Resolution')
    
    N = 5
    
    N_hlf = int((N-1)/2)

    clds_min_avg = np.zeros_like(clds_min)
    clds_max_avg = np.zeros_like(clds_max)
    cs_tc_avg = np.zeros_like(cs_tc_min)
    
    for n in range(-N_hlf, N_hlf+1):
        clds_min_avg += np.roll(clds_min,n)
        clds_max_avg += np.roll(clds_max,n)
        cs_tc_avg += np.roll(cs_tc_min,n)
    
    clds_min_avg = clds_min_avg/N
    clds_max_avg = clds_max_avg/N
    cs_tc_avg = cs_tc_avg/N
    
    clds_min_avg = clds_min_avg[N_hlf:-N_hlf]
    clds_max_avg = clds_max_avg[N_hlf:-N_hlf]
    cs_tc_avg = cs_tc_avg[N_hlf:-N_hlf]
    t_list_avg = t_list[N_hlf:-N_hlf]
    
    #clds_min_avg = pd.rolling_mean(clds_min,N,center=True) 
    #clds_min_avg = pd.Series(clds_min).rolling(window=N).mean().iloc[N-1:].values
    #clds_max_avg = pd.Series(clds_max).rolling(window=N).mean().iloc[N-1:].values
    #cs_tc_avg = pd.Series(cs_tc_min).rolling(window=N).mean().iloc[N-1:].values
    
    #print(clds_min)
    #print(clds_min_avg[:6])
    
    ax[wtag_i][2].plot(t_list_avg,clds_min_avg,c='b',label='Min. cloud size (Rolling avg)')
    ax[wtag_i][2].plot(t_list_avg,clds_max_avg,c='r',label='Max. cloud size (Rolling avg)')
    ax[wtag_i][2].plot(t_list_avg,cs_tc_avg,c='k',label=r'c$_{s}$t$_{cool}$ (Rolling avg)')

    if wtag_i==0:
        ax[wtag_i][2].set_xlabel('time (Myr)',fontsize=15)
    else:
        ax[wtag_i][2].legend(fontsize=10)
    ax[wtag_i][2].set_ylabel('Cloud size (pc)',fontsize=15)
    ax[wtag_i][2].tick_params(labelsize=10)

#plt.ylim (0.,2.5)
#plt.xlim(545,550)

plt.savefig(wdir_script+'/Cloud_size/cloudsize_fourier_rho.png')
