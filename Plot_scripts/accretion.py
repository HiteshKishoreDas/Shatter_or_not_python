#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 02:21:37 2020

@author: hitesh
"""
import numpy as np
import matplotlib.pyplot as plt
import cloud_size as cld
import lamfn as lf
import fourier as fr
#import pandas as pd

import pyPLUTO as pp
import workdir as wd


ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
#t = 2.0 * ut  # in Myr
dt = 0.00001*ut # in Myr   #******************

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

wdir = wd.wdir123#wd.wdir123]  ###############3
# wtag_list = ['Unstable','Unstable']
dln = 512 # Not used if periodic

fig = plt.figure(figsize=(15,5))
#fig,ax = plt.subplots(2,3,figsize=(60,40))

ax1 = fig.add_axes([0.05, 0.1, 0.25, 0.8])
ax2 = fig.add_axes([0.35, 0.1, 0.25, 0.8])
ax3 = fig.add_axes([0.65, 0.1, 0.3, 0.8])

# ax4 = fig.add_axes([0.05, 0.5, 0.25, 0.4])
# ax5 = fig.add_axes([0.35, 0.5, 0.25, 0.4])
# ax6 = fig.add_axes([0.65, 0.5, 0.3, 0.4])

ax = [ax1,ax2,ax3]#,[ax4,ax5,ax6]]
    
nlinf = pp.nlast_info(w_dir=wdir+'output/') 

clds_min = []
clds_max = []
t_list = []
cs_tc_min = []

rho_max_list = []
mass_list = []

for t in range(0,nlinf['nlast']):
    
    cloud_s,res = cld.cloud_size(wdir,t,dln,True)
    
    D = pp.pload(t,w_dir=wdir+'output/')
    
    if len(cloud_s) !=0:
        clds_small = np.min(cloud_s)
        clds_big = np.max(cloud_s)

        clds_min.append(clds_small)
        clds_max.append(clds_big)
        t_list.append(t*dt)
        
        n_H = D.rho*UNIT_DENSITY/(lf.MMWt_muH(D.tr1,D.tr2)*CONST_amu)
        T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)    
    
        lam = lf.lam(T,D.tr1)
        
        q = n_H*n_H*lam/unit_q
        tc = D.prs/(q*(gamma - 1))
        cs = np.sqrt(D.prs/D.rho)
    
        cs_tc_min.append(np.min(tc*cs*ul))

        rho_max = np.max(D.rho)
        rho_max_list.append(rho_max)
        mass_list.append(rho_max*clds_big*3.0856775807e18)

t_list = np.array(t_list)        
res_list = np.zeros_like(t_list) + res*1000    # in pc
clds_min = np.array(clds_min)*1000
clds_max = np.array(clds_max)*1000
cs_tc_min = np.array(cs_tc_min)*1000

clds_min /= cs_tc_min
clds_max /= cs_tc_min

rho_max_list = np.array(rho_max_list)
mass_list = np.array(mass_list)


###### Plot cloud size/min(cs*tcool) with time ######


ax[0].set_yscale('log')
ax[0].plot(t_list,clds_min,label='Min. cloud size',c='b',linestyle=':',linewidth=0.5)
ax[0].plot(t_list,clds_max,label='Max. cloud size',c='r',linestyle=':',linewidth=0.5)
# ax[wtag_i][0].plot(t_list,cs_tc_min,c='k',label=r'c$_{s}$t$_{cool}$',linestyle=':')
# ax[wtag_i][0].plot(t_list,res_list,linestyle='dashed',c='k',label='Resolution')

N = 5

N_hlf = int((N-1)/2)

clds_min_avg = np.zeros_like(clds_min)
clds_max_avg = np.zeros_like(clds_max)
# cs_tc_avg = np.zeros_like(cs_tc_min)

for n in range(-N_hlf, N_hlf+1):
    clds_min_avg += np.roll(clds_min,n)
    clds_max_avg += np.roll(clds_max,n)
    # cs_tc_avg += np.roll(cs_tc_min,n)

clds_min_avg = clds_min_avg/N
clds_max_avg = clds_max_avg/N
# cs_tc_avg = cs_tc_avg/N

clds_min_avg = clds_min_avg[N_hlf:-N_hlf]
clds_max_avg = clds_max_avg[N_hlf:-N_hlf]
# cs_tc_avg = cs_tc_avg[N_hlf:-N_hlf]
t_list_avg = t_list[N_hlf:-N_hlf]


ax[0].plot(t_list_avg,clds_min_avg,c='b',label='Min. cloud size (Rolling avg)')
ax[0].plot(t_list_avg,clds_max_avg,c='r',label='Max. cloud size (Rolling avg)')
# ax[wtag_i][0].plot(t_list_avg,cs_tc_avg,c='k',label=r'c$_{s}$t$_{cool}$ (Rolling avg)')

ax[0].set_xlabel('time (Myr)',fontsize=15)
ax[0].legend(fontsize=10)
ax[0].set_ylabel('Cloudsize/min(cs*tcool) ',fontsize=15)
ax[0].tick_params(labelsize=10)



###### Plot density with time ######

ax[1].set_yscale('log')
ax[1].plot(t_list,rho_max_list,label='Max. density',c='b',linestyle=':')

N = 5

N_hlf = int((N-1)/2)

rho_max_avg = np.zeros_like(rho_max_list)

for n in range(-N_hlf, N_hlf+1):
    rho_max_avg += np.roll(rho_max_list,n)

rho_max_avg = rho_max_avg/N
rho_max_avg = rho_max_avg[N_hlf:-N_hlf]
ax[1].plot(t_list_avg,rho_max_avg,c='b',label='Max. density (Rolling avg)')

ax[1].set_xlabel('time (Myr)',fontsize=15)
ax[1].legend(fontsize=10)
ax[1].set_ylabel(r'Max density (amu cm$^{-1}$)',fontsize=15)
ax[1].tick_params(labelsize=10)



###### Plot mass with time ######

ax[2].set_yscale('log')
ax[2].plot(t_list,mass_list,label='Mass',c='b',linestyle=':')

N = 5

N_hlf = int((N-1)/2)

mass_avg = np.zeros_like(mass_list)

for n in range(-N_hlf, N_hlf+1):
    mass_avg += np.roll(mass_list,n)

mass_avg = mass_avg/N
mass_avg = mass_avg[N_hlf:-N_hlf]
ax[2].plot(t_list_avg,mass_avg,c='b',label='Mass (Rolling avg)')

ax[2].set_xlabel('time (Myr)',fontsize=15)
ax[2].legend(fontsize=10)
ax[2].set_ylabel('Mass (amu)',fontsize=15)
ax[2].tick_params(labelsize=10)

plt.savefig('plot_accretion.png')
