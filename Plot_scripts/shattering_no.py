#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:21:25 2020

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

wdir = wd.wdir41

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
#ut = ((ul * 3.086E+21)/uv)  # in s
#ut = (ut / 3.154e+13)    # in Myr

ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 1.0 # in Myr

m = -0.05
c = 0.5

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

D0 = pp.pload(0,w_dir=wdir+'output/')

D = pp.pload(900,w_dir=wdir+'output/')

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
#
#ax1.set_yscale('log')
#ax2.set_yscale('log')

ax1.plot(D0.x1*ul,np.log10(D0.rho),color='tab:orange',linewidth=5,label='Initial density profile')
ax2.plot(D.x1*ul,np.log10(D.rho),color='tab:blue',linewidth=5,label= 'Non-linear stage density profile')

ax1.set_ylabel(r'log($\rho$) (Initial density profile)',fontsize=30)
ax2.set_ylabel(r'log($\rho$) (Non-linear stage density profile)',fontsize=30)
ax1.set_xlabel(r'x (in kpc)',fontsize=30)

ax1.tick_params(labelsize=25)
ax2.tick_params(labelsize=25)

ax1.set_title('Density profile for case of no shattering',fontsize=35)

ax1.legend(fontsize=20,loc='upper left')
ax2.legend(fontsize=20,loc='upper right')

ax1.set_xlim(1000,5500)
ax2.set_xlim(1000,5500)

plt.savefig(wdir_script+'/shattering_no.png')

