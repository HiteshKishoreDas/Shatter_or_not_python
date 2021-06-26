#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:16:26 2020

@author: hitesh
"""

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

gamma = 5./3.
plutodir = os.environ['PLUTO_DIR']
wdir = wd.wdir100   #***************
wdir = wdir + 'output/'

D = pp.pload(0,w_dir=wdir)

lam =  np.zeros(np.size(D.x1),dtype=float)

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
#ut = ((ul * 3.086E+21)/uv)  # in s
#ut = (ut / 3.154e+13)    # in Myr

ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 1.0 # in Myr

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

fig = plt.figure(figsize=(12,12))

n_H = D.rho*UNIT_DENSITY/(lf.MMWt_muH(D.tr1)*CONST_amu)
T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1)

for i in range(np.size(D.x1)):
    lam[i] = lf.lam(T[i],D.tr1[i])

q = n_H*n_H*lam/unit_q
tc = D.prs/(q*(gamma - 1))
cs = np.sqrt(D.prs/D.rho)

plt.plot(D.x1*ul,tc*cs*ul,linewidth = 2)

plt.xlabel('x (in kpc)',fontsize=30)
plt.ylabel(r'$t_{\rm c}\times c_s$',fontsize=35)
#plt.title(r'$\frac{1}{t_{\rm TI}}$ vs. T',fontsize=40)
#plt.ylim(0,800)
#plt.xlim(2740,2780)
plt.legend(fontsize = 25)
plt.tick_params(labelsize=25)
plt.savefig(wdir_script+'/t_cool.png')
plt.show()
plt.close()