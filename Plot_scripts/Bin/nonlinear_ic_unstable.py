#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:41:37 2020

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

wdir = wd.wdir82

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

D0 = pp.pload(0,w_dir=wdir+'output/')

lam0 =  np.zeros(np.size(D0.x1),dtype=float)

n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1)*CONST_amu)
T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
for i in range(np.size(D0.x1)):
    lam0[i] = lf.lam(T0[i],D0.tr1[i])
q0 = n_H0*n_H0*lam0/unit_q
tc0 = D0.prs/(q0*(gamma - 1))
tc_min = np.min(tc0)*ut

fig,ax = plt.subplots(3,4,figsize=(55,30))
cnt = 0
t_arr = np.array([200,750,1500])

for t in t_arr:
#        nlinf = pp.nlast_info(w_dir=wdir)
    D = pp.pload(t,w_dir=wdir+'output/')
    
    T  = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1)
    
    ln = int(np.size(D.x1)/2)
    dln = 4000
    
    rho = D.rho#[ln-dln:ln+dln]
    T = T#[ln-dln:ln+dln]
    vx1 = D.vx1 * UNIT_VELOCITY #[ln-dln:ln+dln]
    tr1 = D.tr1#[ln-dln:ln+dln]
    x1 = D.x1#[ln-dln:ln+dln]
    
    ntc = t/tc_min
    
    col= 'tab:green'
    
    vx1 = vx1*UNIT_VELOCITY
    
#    if cnt!=0:
#        ax[cnt,0].set_yscale('log')
#    else:
#        formatter = mticker.ScalarFormatter(useMathText=True)
#        formatter.set_powerlimits((-3,2))
#        ax[cnt,0].yaxis.set_major_formatter(formatter)
    
    ax[cnt,0].set_yscale('log')
    ax[cnt,0].plot(x1*ul,rho,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    if cnt==2:
        ax[cnt,0].set_xlabel(r'x (kpc)',fontsize=35)
        
    ax[cnt,0].set_ylabel(r'$\rho$ (amu/$cm^3$)',fontsize=35)
    ax[cnt,0].tick_params(labelsize=25)
    text = ax[cnt,0].yaxis.get_offset_text()
    text.set_size(25)
    
    
    
#    if cnt!=0:
#        ax[cnt,1].set_yscale('log')
#    else:
#        formatter = mticker.ScalarFormatter(useMathText=True)
#        formatter.set_powerlimits((-3,2))
#        ax[cnt,1].yaxis.set_major_formatter(formatter)
        
    ax[cnt,1].set_yscale('log')
    ax[cnt,1].plot(x1*ul,T,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    if cnt==2:
        ax[cnt,1].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,1].set_ylabel(r'T (K)',fontsize=35)
    ax[cnt,1].tick_params(labelsize=25)
    text = ax[cnt,1].yaxis.get_offset_text()
    text.set_size(25)
    
    
    formatter = mticker.ScalarFormatter(useMathText=True)
    formatter.set_powerlimits((-3,2))
    ax[cnt,2].yaxis.set_major_formatter(formatter)
    ax[cnt,2].plot(x1*ul,vx1,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    if cnt ==2:
        ax[cnt,2].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,2].set_ylabel(r'$V_x$ (cm/s)',fontsize=35)
    ax[cnt,2].tick_params(labelsize=25)
    text = ax[cnt,2].yaxis.get_offset_text()
    text.set_size(25)
    
    ax[cnt,3].plot(x1*ul,tr1,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    if cnt ==2:
        ax[cnt,3].set_xlabel(r'x (kpc)',fontsize=35)
    ax[cnt,3].set_ylabel(r'Z ($Z\odot$)',fontsize=35)
    ax[cnt,3].tick_params(labelsize=25)
    ax[cnt,3].legend(fontsize=35,loc='upper right')
    text = ax[cnt,3].yaxis.get_offset_text()
    text.set_size(25)
    
    cnt +=1


plt.savefig(wdir_script+'/nonlinear_ic_unstable_periodic.png')