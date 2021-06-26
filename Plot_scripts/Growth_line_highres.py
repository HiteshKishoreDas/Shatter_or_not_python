#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf
import pyPLUTO as pp

offset_n = 50

colorarr=['tab:red','tab:blue','tab:green','tab:orange']
    
wdir_list = [wd.wdir117,wd.wdir118,wd.wdir119,wd.wdir116]
label_list = ['20000','30000','40000','50000']

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

dt = 1e-6*ut # in Myr

CONST_amu = 1.66053886e-24
CONST_kB = 1.3806505e-16
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

m = -0.05
c = 0.5
        
slope = 0
xbar = 0
ybar = 0
xybar = 0
x2bar = 0

wi_avg = 0

cnt = -1

plt.figure(figsize=(20,20))

for wdir in wdir_list:
    cnt +=1

    nlinf = pp.nlast_info(w_dir=wdir+'output/')

    lt_isochoric = np.zeros(nlinf['nlast']+1,dtype=float)
    sim_isochoric = np.zeros(nlinf['nlast']+1,dtype=float)
    t_arr = np.zeros(nlinf['nlast']+1,dtype=float)
    
    D0 = pp.pload(1,w_dir=wdir+'output/')
    n = np.argmax(D0.rho)  #int(np.size(D1.x1)/2) + offset_n

    D0 = pp.pload(0,w_dir=wdir+'output/')
    # n = int(np.size(D0.x1)/2) + offset_n

    T  = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)

    lamT_arr = lf.lamT(T,D0.tr1)
    tc = lf.tcool(D0)

    wi = (2.-lamT_arr)/tc

    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/')   

        diff = np.abs((D1.rho[n] - 0.0620))/0.0620
        
        y = np.log(diff)
        x = i*dt/ut

        t_arr[i] = i*dt/ut*100
        
        lt_isochoric[i] = wi[n]*i*dt/ut
        
        sim_isochoric[i] = y
    

    lt_isochoric = lt_isochoric - (lt_isochoric[0]-sim_isochoric[0])

    offset = 0#0.25

    #%%

    width = 10

    plt.plot(t_arr,lt_isochoric + offset,color='k',linewidth=width-5,linestyle='dashed',label=r"Linear theory: "+label_list[cnt])
    plt.plot(t_arr,sim_isochoric + offset,color=colorarr[cnt],linewidth=width,label=r"Simulation    : "+label_list[cnt])

plt.xlabel('Time (Myr)',fontsize=45)
plt.ylabel(r'ln $\frac{\delta\rho}{\rho_{o}}$',fontsize=45)
plt.tick_params(labelsize=35)
plt.legend(fontsize=30,frameon=False,loc="center right")
plt.savefig('rho_linear_diffres.png')
