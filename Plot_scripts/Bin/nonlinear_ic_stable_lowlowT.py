#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:53:49 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as mticker

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

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

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.



wdir = wd.wdir88   #*****************

nlinf = pp.nlast_info(w_dir=wdir+'output/')
D0 = pp.pload(0,w_dir=wdir+'output/')

lam0 =  np.zeros(np.size(D0.x1),dtype=float)

n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1)*CONST_amu)
T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
for i in range(np.size(D0.x1)):
    lam0[i] = lf.lam(T0[i],D0.tr1[i])
q0 = n_H0*n_H0*lam0/unit_q
tc0 = D0.prs/(q0*(gamma - 1))
tc_min = np.min(tc0)*ut

fig,ax = plt.subplots(3,3,figsize=(45,30))
cnt = 0
#t_arr = np.array([550,2700,3355])
#t_arr = np.array([400,1500,3000])
t_arr = np.array([0,60,200])

for t in t_arr:
#        nlinf = pp.nlast_info(w_dir=wdir)
    D = pp.pload(t,w_dir=wdir+'output/')
    
    T  = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1)
    
    ln = int(np.size(D.x1)/2)
    dln = 4000
    
    rho = np.copy(D.rho)
    T = np.copy(T)
    vx1 = np.copy(D.vx1* UNIT_VELOCITY)
    tr1 = np.copy(D.tr1)
    x1 = np.copy(D.x1)
    
    ntc = t/tc_min
    
    col = 'tab:green'
    
    if cnt!=0:
        ax[cnt,0].set_yscale('log')
    else:
        ax[cnt,0].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        
    ax[cnt,0].plot(x1*ul,rho,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    if cnt==2:
        ax[cnt,0].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,0].set_ylabel(r'$\rho$ (amu/$cm^3$)',fontsize=35)
    ax[cnt,0].tick_params(labelsize=25)
    text = ax[cnt,0].yaxis.get_offset_text()
    text.set_size(25)
    
    
    
    if cnt!=0:
        ax[cnt,1].set_yscale('log')
    else:
        ax[cnt,1].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        formatter = mticker.ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-3,2))
        ax[cnt,1].yaxis.set_major_formatter(formatter)
        
    ax[cnt,1].plot(x1*ul,T,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    
    if cnt==2:
        ax[cnt,1].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,1].set_ylabel(r'T (K)',fontsize=35)
    ax[cnt,1].tick_params(labelsize=25)
    text = ax[cnt,1].yaxis.get_offset_text()
    text.set_size(25)
    
    
    ax[cnt,2].plot(x1*ul,vx1,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    
    if cnt ==2:
        ax[cnt,2].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,2].set_ylabel(r'$V_x$ (cm/s)',fontsize=35)
    ax[cnt,2].tick_params(labelsize=25)
    text = ax[cnt,2].yaxis.get_offset_text()
    text.set_size(25)
    ax[cnt,2].legend(fontsize=35,loc='upper right')
    ax[cnt,2].yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    
    cnt +=1

plt.savefig(wdir_script+'/nonlinear_stable_ic_lowT.png')
