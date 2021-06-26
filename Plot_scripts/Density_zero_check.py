#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:58:24 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:35:12 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir17]:
    nlinf = pp.nlast_info(w_dir=wdir+'output_last/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.01
    c = 0.5
    
    peak = 0.0

    for i in range(900,nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output_last/') # Loading the data into a pload object D.
        
        zer = D1.rho[D1.rho == 0.0]
        sz = np.size(zer)
        print(sz)
        if (sz != 0):
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            count += 1

print("Number of times zero is encountered: "+str(count))
