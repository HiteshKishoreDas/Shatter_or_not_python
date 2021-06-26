#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
import numpy as np
import workdir as wd
import lamfn as lf

import pyPLUTO as pp

filn = 16
#N = 100
#M = 0

CONST_amu = 1.66053886e-24
CONST_kB = 1.3806505e-16
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ul = 100 # in kpc
ut = UNIT_LENGTH/UNIT_VELOCITY   # in sec
ut = ut/3.154e7   # in yrs
ut = ut/1e6       # in Myr
dt = ut*1e-2 # in Myr

def growth_fit(wdir,M,N):
#    nlinf = pp.nlast_info(w_dir=wdir+ 'output/')

    fit_arr = np.zeros((2,N-M),dtype = float)
    
    wi_avg = 0
    
    offset_n = 50
    
    D0 = pp.pload(0,w_dir=wdir+ 'output/')
    n = int(np.size(D0.x1)/2) + offset_n
#    if (np.abs(D0.rho[n] - 0.0620)/0.0620 < 0.0):
#        n = int(np.size(D0.x1)/2) - offset_n
        
    for i in range(M,N):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+ 'output/') 

        diff = np.abs(D1.rho[n] - 0.0620)/0.0620
        
        y = np.log(diff)

        x = i*dt/ut
        
#        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
#        
#        lamT_arr = lf.lamT(T,D1.tr1)
#        tc = lf.tcool(D1)
#        
#        wi = (2.-lamT_arr)/tc
        
        fit_arr[1,i-M] = y
        fit_arr[0,i-M] = x        
        
        if (i==M):
            y0 = y
        else:
#            slope = slope + ((y - y0)*ut/dt)**2
            
            y0 = y
            wi_avg = wi_avg + D1.wi[n]
    
    v = np.polyfit(fit_arr[0,:],fit_arr[1,:],1)
    
    return wi_avg/(N-M-1)*(1/ut),v[0] * (1/ut)

if __name__ =='__main__':
    cntwdir = 0
    for wdir in [wd.wdir116]:
        
        wi_avg,v = growth_fit(wdir,0,100)
        
        print('Theoretical: ',wi_avg)
        print('Fitted     : ',v) 