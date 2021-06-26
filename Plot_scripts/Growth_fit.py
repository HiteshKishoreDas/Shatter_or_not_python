#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
#%%

import os
import numpy as np
import workdir as wd
import lamfn as lf


wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

filn = 16
#N = 100
#M = 0

wi_arr = np.zeros((3,filn),dtype = float)

k_arr = np.zeros(filn,dtype = float)


wdir0 = wd.wdir58 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/output/'
wdir1 = wd.wdir57 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/output/'
wdir2 = wd.wdir56 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/output/'

k_arr[0:3] = [10.*np.pi, 50.*np.pi, 100.*np.pi]

wdir3 = wd.wdir65 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/output/'
wdir4 = wd.wdir63 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/output/'
wdir5 = wd.wdir62 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/output/'
wdir6 = wd.wdir64 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/output/'

k_arr[3:7] = [2.*np.pi, 1.*np.pi, 1.*np.pi, 2.*np.pi]

wdir7 = wd.wdir59 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/output/'
wdir8 = wd.wdir60 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/output/'
wdir9 = wd.wdir61 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/output/'

k_arr[7:10] = [0.1*np.pi, 0.05*np.pi, 0.01*np.pi]

wdir10 = wd.wdir69 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/output/'
wdir11 = wd.wdir71 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/output/'
wdir12 = wd.wdir70 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/output/'

k_arr[10:13] = [10.*np.pi, 10.*np.pi, 10.*np.pi]

wdir13 = wd.wdir66 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Base/output/'
wdir14 = wd.wdir68 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamT/output/'
wdir15 = wd.wdir67 #plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamZ/output/'

k_arr[13:16] = [0.1*np.pi, 0.1*np.pi, 0.1*np.pi]

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
    for wdir in [wdir0, wdir1, wdir2,\
                 wdir3, wdir4, wdir5,\
                 wdir6, wdir7, wdir8, wdir9,\
                 wdir10, wdir11, wdir12,\
                 wdir13, wdir14, wdir15]:
        
        wi_avg,v = growth_fit(wdir,0,100)
        
        wi_arr[0,cntwdir] = wi_avg
        wi_arr[1,cntwdir] = v
        wi_arr[2,cntwdir] = k_arr[cntwdir]
        
        cntwdir = cntwdir +1
        
    np.save(wdir_script+"/wi_arr_fit",wi_arr)
    wi_arrload = np.load(wdir_script+"/wi_arr_fit.npy")