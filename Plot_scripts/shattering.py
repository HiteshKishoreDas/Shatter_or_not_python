#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:14:30 2020

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = ut*0.01 # in Myr

m = -0.05
c = 0.5

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(50,15))
cnt = -1

for wdir in [wd.wdir73,wd.wdir72]:
    cnt +=1
    if cnt==0:
        D0 = pp.pload(50,w_dir=wdir+'output/')
        ln = int(np.size(D0.x1)/2)
        dln = 3000   #*****************
        
        x10 = D0.x1[ln-dln:ln+dln]
        rho0 = D0.rho[ln-dln:ln+dln]
        
        D = pp.pload(3350,w_dir=wdir+'output/')
    
        x1 = D.x1[ln-dln:ln+dln]
        rho = D.rho[ln-dln:ln+dln]
        
#        ax1 = fig.add_subplot(1, 1, 1)
        ax3 = ax1.twinx()
    
        ax1.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
        ax3.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
        
        ax1.plot(x10*ul,np.log10(rho0),color='tab:red',linestyle='--',linewidth=5,label='Initial density profile')
        ax3.plot(x1*ul,np.log10(rho),color='tab:blue',linewidth=5,label= 'Non-linear stage density profile')
        
        text1 = ax1.yaxis.get_offset_text()
        text1.set_size(25)
        text3 = ax3.yaxis.get_offset_text()
        text3.set_size(25)
        
        ax1.set_ylabel(r'log($\rho$) (Initial density profile)',fontsize=30)
        ax3.set_ylabel(r'log($\rho$) (After onset of Non-linear evolution)',fontsize=30)
        ax1.set_xlabel('x (in kpc)\n(a)',fontsize=35)
        
        ax1.tick_params(labelsize=30)
        ax3.tick_params(labelsize=30)
        
        ax1.set_title('Density profile for case of shattering (NIC_ST)',fontsize=35)
        
        ax1.legend(fontsize=25,loc='upper left')
        ax3.legend(fontsize=25,loc='upper right')
        
#        ax1.set_xlim(1000,5500)
#        ax3.set_xlim(1000,5500)
    
    else:
        D0 = pp.pload(0,w_dir=wdir+'output/')
        
        ln = int(np.size(D0.x1)/2)
        dln = 3000   #*****************
        
        x10 = D0.x1[ln-dln:ln+dln]
        rho0 = D0.rho[ln-dln:ln+dln]
        
        D = pp.pload(1050,w_dir=wdir+'output/')
        
        x1 = D.x1[ln-dln:ln+dln]
        rho = D.rho[ln-dln:ln+dln]
        
#        ax2 = fig.add_subplot(1, 2, 1)
        ax4 = ax2.twinx()
        
        ax2.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
        ax4.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    
        ax2.plot(x10*ul,np.log10(rho0),color='tab:red',linestyle='--',linewidth=5,label='Initial density profile')
        ax4.plot(x1*ul,np.log10(rho),color='tab:blue',linewidth=5,label= 'Non-linear stage density profile')
        
        text2 = ax2.yaxis.get_offset_text()
        text2.set_size(25)
        text4 = ax3.yaxis.get_offset_text()
        text4.set_size(25)
        
        ax2.set_ylabel(r'log($\rho$) (Initial density profile)',fontsize=30)
        ax4.set_ylabel(r'log($\rho$) (After onset of Non-linear evolution)',fontsize=30)
        ax2.set_xlabel('x (in kpc)\n(b)',fontsize=35)
        
        ax2.tick_params(labelsize=30)
        ax4.tick_params(labelsize=30)
        
        ax2.set_title('Density profile for case of no shattering (NIC_UST)',fontsize=35)
        
        ax2.legend(fontsize=25,loc='upper left')
        ax4.legend(fontsize=25,loc='upper right')
        
        ax2.set_xlim(1000,5500)
        ax4.set_xlim(1000,5500)
    
    print(cnt)
    
    
plt.savefig(wdir_script+'/shattering/shattering.png')