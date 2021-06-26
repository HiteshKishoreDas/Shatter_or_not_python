#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:20:46 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:01:02 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

def two_scales(ax1, x, data1, data2, c1, c2):
    ax2 = ax1.twinx()
    
    ax1.plot(x, data1, color=c1,label='Density')
    ax1.set_xlabel('Position (in kpc)',fontsize=25)
    ax1.set_ylabel('Density', color='tab:red',fontsize=25)
    
    ax2.plot(x, data2, color=c2,label = r'$\Delta Z$')
    ax2.set_ylabel(r'$ \Delta Z $', color='tab:blue',fontsize=25)
    
    ax1.tick_params(labelsize=15)
    ax2.tick_params(labelsize=15)
    
    return ax1, ax2

fig, ax1 = plt.subplots(2,3,figsize=(60,20))
count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir33,wd.wdir34,wd.wdir35]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
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
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    nt = 100

    D1 = pp.pload(nt,w_dir=wdir+'output/') # Loading the data into a pload object D.
    
    ln = int(np.size(D1.x1)/2)
    dln = 30
        
    zfluc0 = D0.tr1 - (m*D0.x1 + c)
    zfluc = D1.tr1 - (m*D1.x1 + c)
    
    rho0 = D0.rho
    rho = D1.rho
    
    x0 = D0.x1
    
    ax1[0,count], ax2 = two_scales(ax1[0,count], x0*ul, rho0, zfluc0, 'tab:red', 'tab:blue')
#    ax1[0,count].set_xlim(195.,205.)
    ax1[0,count].set_ylim(0.0612,0.0628)
    ax2.set_ylim(-0.04,0.04)
    ax1[0,count].legend(loc='upper right',fontsize=15)
    ax2.legend(loc='upper left',fontsize=15)
    ax2.set_title(r'With $\Delta\phi = '+phi_arr[count]+'$ at t=0',fontsize=20)
    
    ax1[1,count], ax2 = two_scales(ax1[1,count], x0*ul, rho, zfluc, 'tab:red', 'tab:blue')
#    ax1[1,count].set_xlim(195.,205.)
    ax1[1,count].set_ylim(0.0612,0.0628)
    ax2.set_ylim(-0.04,0.04)
    ax2.set_title(r'With $\Delta\phi = '+phi_arr[count]+'$ at t=100 Myr',fontsize=20)
    
    count +=1
    
plt.savefig(wdir_script+'/Phase_isochoric.png')