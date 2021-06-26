#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:17:02 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 05:02:17 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


for wdir in [wd.wdir91]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    ln = int(np.size(D0.x1)/2)#+ 250 + 265
    dln = 500
    
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/')
        
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        
        lamT_arr = lf.lamT(T,D1.tr1)
        tc = lf.tcool(D1)
        
        tti = tc/(2.-lamT_arr)
        
        tti = tti[ln-dln:ln+dln]*ut
        x1 = D1.x1[ln-dln:ln+dln]*ul
        rho = D1.rho[ln-dln:ln+dln]
        
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_subplot(1,1,1)
        ax2 = ax1.twinx()
        ax1.set_zorder(10)
        ax1.patch.set_visible(False)
        
        ax1.plot(x1,tti,label=r'$t_{\rm TI}$',c='tab:red',linewidth=0.5)
        ax2.plot(x1,rho,label='Density',c='tab:blue',linewidth=0.5)
              
        ax1.set_xlabel(r'x (in kpc)')
        ax1.set_ylabel(r'$t_{\rm TI}$ (Myr)')
        ax2.set_ylabel('Density')
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
        ax1.set_title(r'$t_{\rm TI}$ and $\rho$: ' + str(i*dt) + ' Myr')
        fig.savefig(wdir+'Plots_full_log/' + 'tti_rho' + '/' +'tti_rho'+ '_' + str(i) +'.png')
        
        ax1.cla()
        fig.clf()
        plt.close(fig)
        del(fig)
        del(ax1)
    
        del(D1)
