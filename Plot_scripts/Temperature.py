#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:44:43 2020

@author: Hitesh Kishore Das
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd
#import begend as bg


os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


for wdir in [wd.wdir58]:
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
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)

    offset_n = 50
    n = int(np.size(D0.x1)/2) + offset_n

    plt.plot(D0.x1,T0)    
    print(np.max(T0))
    print(T0[n])
    print(np.average(T0))
    