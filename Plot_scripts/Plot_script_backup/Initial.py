#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

wdir_script = os.getcwd()

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'
wdir2 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/output/'
wdir3 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/output/'

wdir4 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/output/'
wdir5 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/output/'
wdir6 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/output/'

wdir7 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/output/'
wdir8 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/output/'
wdir9 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/output/'
wdir10 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/output/'

wdir11 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/output/'
wdir12 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/output/'
wdir13 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/output/'

wdir14 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Base/output/'
wdir15 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamT/output/'
wdir16 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamZ/output/'

def same(X,Y):
    
    Y_arr = np.zeros(np.size(X),dtype=float)
    
    for i in range(np.size(X)):
        Y_arr[i] = Y
    return Y_arr

for wdir in [wdir9]:
    
    nlinf = pp.nlast_info(w_dir=wdir)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5

    N = 300
    M = 0
    D0 = pp.pload(0,w_dir=wdir)

   
    
    fig = plt.figure(figsize=(13,15))
    
    ax1 = fig.add_axes([0.1, 0.1, 0.75, 0.2])
    ax2 = fig.add_axes([0.1, 0.35, 0.75, 0.2])
    ax3 = fig.add_axes([0.1, 0.6, 0.75, 0.05])
    ax4 = fig.add_axes([0.1, 0.65, 0.75, 0.15])
#    ax.set_yscale('log')
   
    rho0 = (np.max(D0.rho)+np.min(D0.rho))/2.0
    p0 = (np.max(D0.prs)+np.min(D0.prs))/2.0
    
    width = 6
    
    n = int(np.size(D0.x1)/2)
    
    ax1.plot(D0.x1*ul, same(D0.x1,rho0),linewidth=width,c='tab:blue')
    ax1.plot(D0.x1*ul,D0.rho,linestyle='--',linewidth=width,c='tab:orange')
    ax1.scatter(D0.x1[n]*ul, D0.rho[n],marker='o',zorder=3,s=200,c='tab:green')
    
    ax2.plot(D0.x1*ul, same(D0.x1,p0),linewidth=width,c='tab:blue')
    ax2.plot(D0.x1*ul,D0.prs,linestyle='--',linewidth=width,c='tab:orange')
    
    ax3.plot(D0.x1*ul, same(D0.x1,0.0),linewidth=width,c='tab:blue')
    ax3.plot(D0.x1*ul, D0.tr1 - (m*D0.x1+c),linestyle='--',linewidth=width,c='tab:orange')
    
    ax4.plot(D0.x1*ul, D0.tr1,label = 'Background',linewidth=width,c='tab:blue')
    ax4.plot(D0.x1*ul, m*D0.x1+c,linestyle='--',label = 'With perturbation',linewidth=width,c='tab:orange')

    ax1.set_xlabel(r'x (in kpc)',fontsize=25)
    
    ax1.set_ylabel(r'$\rho$',fontsize=25)
    ax2.set_ylabel(r'$p$',fontsize=25)
    ax3.set_ylabel(r'$\Delta Z$',fontsize=25)
    ax4.set_ylabel(r'$Z$',fontsize=25)
    
    ax4.axes.get_xaxis().set_ticks([])
    
    ax1.tick_params(labelsize=15)
    ax2.tick_params(labelsize=15)
    ax3.tick_params(labelsize=15)
    ax4.tick_params(labelsize=15)
    
    ax4.legend(fontsize=20)

#    ax.set_title(st + ': ' + str(i*dt) + ' Myr')
    plt.savefig(wdir_script+'/initial.png')
    plt.show()
#%%