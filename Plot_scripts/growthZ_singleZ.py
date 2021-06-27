#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

wdir_script = os.getcwd()

# os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

Nz = 6
NT = 1000

Z_arr = np.array([0.6])
col_arr = ['tab:blue','tab:red']

Y     = 1.01
T_arr = np.logspace(4,8,num=NT)
q0_arr = np.zeros(NT,dtype=float)
tc0_arr = np.zeros(NT,dtype=float)
w_ic_arr = np.zeros(NT,dtype=float)
w_ib_arr = np.zeros(NT,dtype=float)

T_arr_2 = np.logspace(5,8,num=NT)
q0_arr_2 = np.zeros(NT,dtype=float)
tc0_arr_2 = np.zeros(NT,dtype=float)
w_ic_arr_2 = np.zeros(NT,dtype=float)
w_ib_arr_2 = np.zeros(NT,dtype=float)

gamma = 5./3.
# plutodir = os.environ['PLUTO_DIR']
# wdir = wd.wdir59 #= plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'

# D0 = pp.pload(0,w_dir=wdir+'/output/')

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ut = UNIT_LENGTH/UNIT_VELOCITY
ut = ut/3.154e7
ut = ut/1e6

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH

color_cnt = 0

fig = plt.figure(figsize=(15,12))
ax1 = fig.add_axes([0.15, 0.1, 0.8, 0.8])
ax2 = ax1.inset_axes([0.55, 0.7, 0.4, 0.25])

ax1.set_yscale('symlog')
#ax2.set_yscale('symlog')

ax2.set_ylim(-0.005,0.01)#(-0.01,0.04)
#ax1.set_ylim(-30,42)
ax2.set_xlim(4e6,1e8)
ax1.set_xlim(1e4,1e8)

for Z in Z_arr:
    rho0 = 0.062#D0.rho[0]
    p0 = rho0/(KELVIN*lf.MMWt_mu(Z,Y))#D0.prs[0]
    
#    print(D0.prs[0])
    
    n_H = rho0*UNIT_DENSITY/(lf.MMWt_muH(Z,Y)*CONST_amu)
    for i in range(np.size(T_arr)):
        
#        if i==310:
#            print(Z, T_arr[i],p0*T_arr[i])
        
        # lam = lf.lam(T_arr[2],Z)
        q0_arr[i] = n_H*n_H*lf.lam(T_arr[i],Z)/unit_q
        tc0_arr[i] = p0*T_arr[i]/(q0_arr[i]*(gamma - 1)) # Changed
        w_ib_arr[i] = (2-lf.lamT(T_arr[i],Z))/(gamma*tc0_arr[i])
        w_ic_arr[i] = (-lf.lamT(T_arr[i],Z))/(tc0_arr[i])
        
#        if i==310:
#            print(ut/w_ib_arr[i])
        
        # lam = lf.lam(T_arr_2[2],Z)
        q0_arr_2[i] = n_H*n_H*lf.lam(T_arr_2[i],Z)/unit_q
        tc0_arr_2[i] = p0*T_arr_2[i]/(q0_arr_2[i]*(gamma - 1)) #Changed
        w_ib_arr_2[i] = (2-lf.lamT(T_arr_2[i],Z))/(gamma*tc0_arr_2[i])
        w_ic_arr_2[i] = (-lf.lamT(T_arr_2[i],Z))/(tc0_arr_2[i])
        
    ax1.plot(T_arr,w_ib_arr/ut,label='Isobaric (small-scale)',linewidth = 5,color=col_arr[0])
    ax1.plot(T_arr,w_ic_arr/ut,label='Isochoric (large-scale)',linewidth = 5,linestyle='--',color=col_arr[1])
    
    ax2.plot(T_arr_2,w_ib_arr_2/ut,linewidth = 5,color=col_arr[0])
    ax2.plot(T_arr_2,w_ic_arr_2/ut,linewidth = 5,linestyle='--',color=col_arr[1])
    
    color_cnt +=1
    
zer = np.zeros(np.size(T_arr),dtype=float)
ax1.plot(T_arr,zer,color='k',linewidth = 1,linestyle='--')
ax2.plot(T_arr_2,zer,color='k',linewidth = 1,linestyle='--')


# Shading the regions
ax1.axvspan(1e4, 1.68e4, alpha=0.3, color='lightgray')
ax1.axvspan(1.68e4, 3e4, alpha=0.3, color='gray')
ax1.axvspan(3e4, 5e4, alpha=0.3, color='lightgray')
ax1.axvspan(5e4, 6.75e4, alpha=0.3, color='gray')
ax1.axvspan(6.75e4, 9.5e4, alpha=0.3, color='lightgray')
ax1.axvspan(9.5e4, 1.35e5, alpha=0.3, color='gray')
ax1.axvspan(1.35e5, 2.1e5, alpha=0.3, color='lightgray')
ax1.axvspan(2.1e5, 7e5, alpha=0.3, color='gray')
ax1.axvspan(7e5, 9e5, alpha=0.3, color='lightgray')
ax1.axvspan(9e5, 5.25e6, alpha=0.3, color='gray')
ax1.axvspan(5.25e6, 8.5e6, alpha=0.3, color='lightgray')
ax1.axvspan(8.5e6, 2.5e7, alpha=0.3, color='gray')
ax1.axvspan(2.5e6, 1e8, alpha=0.3, color='lightgray')

ax2.axvspan(1e5, 1.35e5, alpha=0.3, color='gray')
ax2.axvspan(1.35e5, 2.1e5, alpha=0.3, color='lightgray')
ax2.axvspan(2.1e5, 7e5, alpha=0.3, color='gray')
ax2.axvspan(7e5, 9e5, alpha=0.3, color='lightgray')
ax2.axvspan(9e5, 5.25e6, alpha=0.3, color='gray')
ax2.axvspan(5.25e6, 8.5e6, alpha=0.3, color='lightgray')
ax2.axvspan(8.5e6, 2.5e7, alpha=0.3, color='gray')
ax2.axvspan(2.5e6, 1e8, alpha=0.3, color='lightgray')


ax1.text(1.39e4,-0.10*280,r"$\mathbf{I}$",ha='center', va='center',fontsize=20)
ax1.text(5.8e4,-0.15*280,r"$\mathbf{I}$",ha='center', va='center',fontsize=20)

ax1.text(2.2e4,-0.15*280,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax1.text(1.1e5,-0.05*120,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax1.text(3.8e5,-0.05*50,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax1.text(2e6,-0.05*50,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax1.text(1.5e7,-0.05*50,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)

ax1.text(3.8e4,-0.15*280,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax1.text(8.1e4,-0.15*280,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax1.text(1.7e5,-0.05*120,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax1.text(8e5,-0.05*50,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax1.text(6.8e6,-0.05*50,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax1.text(5e7,-0.05*50,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)

#ax2.text(1.15e5,0.035/5,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
#ax2.text(4.5e5,0.035/5,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax2.text(4.6e6,-0.035/9,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)
ax2.text(1.5e7,-0.035/9,r"$\mathbf{II}$",ha='center', va='center',fontsize=20)

#ax2.text(1.7e5,0.035/5,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
#ax2.text(8e5,0.035/5,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax2.text(6.8e6,-0.035/9,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)
ax2.text(5e7,0.-0.035/9,r"$\mathbf{III}$",ha='center', va='center',fontsize=20)

ax1.set_xscale('log')
ax2.set_xscale('log')


ax1.set_xlabel('Temperature (K)',fontsize=30)
ax1.set_ylabel(r'Growth Rate ($Myr^{-1}$)',fontsize=35)
#ax1.set_title(r'Growth rate vs. T',fontsize=40)

ax1.legend(fontsize = 30,loc='lower right')
ax1.tick_params(labelsize=25)
ax2.tick_params(labelsize=20)
ax1.indicate_inset_zoom(ax2,linewidth=3)
mark_inset(ax1, ax2, loc1=1, loc2=3, fc="none", ec="0.5",lw=3)

ax1.tick_params(axis="y", direction="inout", length=8, width=2)
ax1.tick_params(axis="x", direction="inout", length=8, width=2)
ax1.tick_params(axis="x", which='minor', direction="in", length=4, width=1)

plt.savefig(wdir_script+'/wvT_singleZ.png')