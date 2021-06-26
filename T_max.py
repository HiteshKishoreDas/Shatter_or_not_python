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
#import begend as bg

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

#wdir0 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/'

wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/'
wdir2 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/'
wdir3 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/'

wdir4 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/'
wdir5 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/'
wdir6 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/'

wdir7 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/'
wdir8 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/'
wdir9 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/'
wdir10 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/'

wdir11 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/'
wdir12 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/'
wdir13 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/'

wdir14 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Base/'
wdir15 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamT/'
wdir16 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamZ/'

wdir17 = plutodir+ 'TI_uniform/metallicity/'
wdir18 = plutodir+ 'TI_uniform/metallicity_sec_run/'
wdir19 = plutodir+ 'TI_uniform/metallicity_thd_run/'

wdir20 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/long_run/16384_10/'

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


for wdir in [wdir17]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5
    
    def boxplot(dr,dr0,drx,i,st,shock,flag):
            
        drx = np.multiply(ul,drx)
        
        if (flag):
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot(1,1,1)
            ax.plot(drx,dr,label=str(i),c='tab:red',linewidth=0.15)
            ax.plot(drx,dr0,label='0',c='tab:blue',linewidth=0.15)
            ax.scatter(drx[np.nonzero(shock)],dr[np.nonzero(shock)],s=30,label='shock',marker='o',color='g')
            ax.set_xlabel(r'x (in kpc)')
            ax.set_ylabel(st)
#            ax.set_xlim(0.,10.)
            ax.legend()
            ax.grid()
            ax.set_title(st + ': ' + str(i*dt) + ' Myr')
            fig.savefig(wdir+'Plots/' + st + '/' +st+ '_' + str(i) +'.png')
            ax.cla()
            fig.clf()
            plt.close(fig)
            del(fig)
            del(ax)
    #        gc.collect(2)
        else:
            plt.figure(figsize=(15,15))
            plt.plot(range(np.size(dr)),dr,label=str(i))
            plt.plot(range(np.size(dr0)),dr0,label='0')
            plt.xlabel(r'index')
            plt.ylabel(st)
            plt.legend()
            plt.grid()
            plt.title(st + ': ' + str(i*dt) + ' Myr')
            plt.savefig(wdir+'Plots/' + st + '/' +st+ '_' + str(i) +'.png')
            plt.close()
    #        gc.collect(2)    
        return 0
    
            
    
    #col = ['r','g','k','b']
    #cnt = 0
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Density_min', color='tab:blue')
    ax1.set_ylabel('Temperature_max', color='tab:red')
    ax1.set_xlabel('Position in kpc')
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)

#%%
    
    N = 600
    ln = nlinf['nlast'] - N + 1
    
    T_max = np.zeros(ln, dtype=float)
    T_x = np.zeros(ln, dtype=float)
    
    T_min = np.zeros(ln, dtype=float)
    T_min_x = np.zeros(ln, dtype=float)
    
    P_max = np.zeros(ln, dtype=float)
    P_x = np.zeros(ln, dtype=float)
    
    rho_min = np.zeros(ln, dtype=float)
    rho_x = np.zeros(ln, dtype=float)
    
    t = np.zeros(ln, dtype=float)
        
    for i in range(0, 1):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        
        T_max[i-N] =  T[np.argmax(T)]
        T_x[i-N] = D1.x1[np.argmax(T)]*ul
        
        T_min[i-N] =  T[np.argmin(T)]
        T_min_x[i-N] = D1.x1[np.argmin(T)]*ul
        
        P_max[i-N] = D1.prs[np.argmax(D1.prs)]
        P_x[i-N] = D1.x1[np.argmax(D1.prs)]*ul
        
        rho_min[i-N] = D1.rho[np.argmin(D1.rho)]
        rho_x[i-N] = D1.x1[np.argmin(D1.rho)]*ul
        
        t[i-N] = i

        del(D1)
        
#    map1 = ax1.scatter(T_x,T_max,marker='o',c=t,cmap='jet',label='Temperature')
    map1 = ax1.scatter(T_min_x,T_min,marker='o',c=t,cmap='jet',label='Temperature_min')
#    ax2.scatter(P_x,P_max,marker='x',c=t,cmap='jet',label='Pressure')
#    ax2.scatter(rho_x,rho_min,marker='d',c=t,cmap='jet',label='Density')
    
    ax1.set_yscale('log')
    
    plt.colorbar(map1, ax = ax1,anchor=(1.5,0.0))

    plt.title("Temperature_min")
#    plt.title("Temperature_max and density_min")
#    plt.title("Temperature_max and pressure_max")
    plt.legend()

    plt.savefig(wdir_script+'/T_min.png')
#    plt.savefig(wdir_script+'/Maxmin_Trho.png')
#    plt.savefig(wdir_script+'/Max_TP.png')
    plt.close()
    #    diff = np.max(D1.prs) - np.max(D0.prs)
    ##    if (i!=0):
    #    #plt.scatter(np.log10(i*dt),np.log10(diff))
    #    plt.scatter(i*dt,np.log10(diff))
    #    print(np.log10(diff),diff)    
    #
    ##plt.axis([0,2001,-10,10])
    #    
    #nm = "prs"
    #plt.xlabel('(time in Myr)')
    #plt.ylabel('log(max-min) of '+nm)
    #plt.title("log(max-min) of "+nm+" vs. time for no perturbation")
    #plt.grid()
    #plt.savefig(wdir+'Plots/'+nm+'_diff.png')
    ##plt.show()