#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:11:22 2020

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
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 0.01*ut # in Myr

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

labelsize=40
ticksize=35
titlesize=45 
offsetsize=35
legendsize= 30
plotline_width = 7
plotline_width0 = 3

col = 'tab:blue'
col0 = 'tab:red'

left   = 0.1   # the left side of the subplots of the figure
right  = 0.9   # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top    = 0.8   # the top of the subplots of the figure
wspace = 0.25   # the amount of width reserved for blank space between subplots
hspace = 0.25   # the amount of height reserved for white space between subplots


wdir_list = [wd.wdir73,wd.wdir72]   #*****************
state_list = ['NIC_ST_OF','NIC_UST_OF']
periodic_tag = False

fig,ax = plt.subplots(2,2,figsize=(20,20))

for wd_i,wdir in enumerate(wdir_list):
    
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    lam0 =  np.zeros(np.size(D0.x1),dtype=float)
    
    n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1,D0.tr2)*CONST_amu)
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)
    for i in range(np.size(D0.x1)):
        lam0[i] = lf.lam(T0[i],D0.tr1[i])
    q0 = n_H0*n_H0*lam0/unit_q
    tc0 = D0.prs/(q0*(gamma - 1))
    tc_min = np.min(tc0)*ut

#    cnt = 0
    #t_arr = np.array([550,2700,3355])
    #t_arr = np.array([1508,1509,1510])
    #t_arr = np.array([1000,1500,3000])
    t = nlinf['nlast']-50
    
    D = pp.pload(t,w_dir=wdir+'output/')
    
    T  = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)
    
    ln = int(np.size(D.x1)/2)
    dln = 3000#int(np.size(T)*0.5)


    if periodic_tag:
        rho = D.rho
        rho0 = D0.rho
#        vx1 = D.vx1* UNIT_VELOCITY#
        tr1 = D.tr1
        tr10 = D0.tr1
        x1 = D.x1
    else:
        rho = D.rho[ln-dln:ln+dln]
        rho0 = D0.rho[ln-dln:ln+dln]
#        T = T[ln-dln:ln+dln]
#        vx1 = D.vx1[ln-dln:ln+dln]* UNIT_VELOCITY#
        tr1 = D.tr1[ln-dln:ln+dln]
        tr10 = D0.tr1[ln-dln:ln+dln]
        x1 = D.x1[ln-dln:ln+dln]
    
    
    ntc = t*dt/tc_min
    
#        if cnt!=0:
#            ax[0,cnt].set_yscale('log')
#        else:
    ax[0,wd_i].set_yscale('log')
    formatter = mticker.ScalarFormatter(useMathText=True)
    formatter.set_powerlimits((-3,2))
    ax[0,wd_i].yaxis.set_major_formatter(formatter)
    

    ax[0,wd_i].plot(x1*ul,rho,linewidth=plotline_width,\
      label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    ax[0,wd_i].plot(x1*ul,rho0,linewidth=plotline_width0,\
      linestyle='dashed',label='t='+"{0:.2f}".format(0.0)+r'$t_{\rm cool}$',\
      color=col0, zorder= 3)

#    if cnt==2:
#        ax[0,cnt].set_xlabel(r'x (kpc)',fontsize=35)
    if wd_i==0:    
        ax[0,wd_i].set_ylabel(r'$\rho$ (amu cm$^{-3}$)',fontsize=labelsize)
    ax[0,wd_i].tick_params(labelsize=labelsize)
    ax[0,wd_i].set_title(state_list[wd_i],fontsize=titlesize,y=1.02)
    text = ax[0,wd_i].yaxis.get_offset_text()
    text.set_size(offsetsize)
    
    
    
#        if cnt!=0:
#            ax[1,cnt].set_yscale('log')
#        else:
#            formatter = mticker.ScalarFormatter(useMathText=True)
#            formatter.set_powerlimits((-3,2))
#            ax[1,cnt].yaxis.set_major_formatter(formatter)
#            
#        ax[1,cnt].plot(x1*ul,T,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
#    #    if cnt==2:
#    #        ax[1,cnt].set_xlabel(r'x (kpc)',fontsize=35)
#        if cnt==0:
#            ax[1,cnt].set_ylabel(r'T (K)',fontsize=labelsize)
#        ax[1,cnt].tick_params(labelsize=labelsize)
#        text = ax[1,cnt].yaxis.get_offset_text()
#        text.set_size(offsetsize)
#        
#        
#        formatter = mticker.ScalarFormatter(useMathText=True)
#        formatter.set_powerlimits((-3,2))
#        ax[2,cnt].yaxis.set_major_formatter(formatter)
#        ax[2,cnt].plot(x1*ul,vx1,linewidth=3,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
#    #    if cnt ==2:
#    #        ax[2,cnt].set_xlabel(r'x (kpc)',fontsize=35)
#        if cnt==0:
#            ax[2,cnt].set_ylabel(r'$V_x$ (cm s$^{-1}$)',fontsize=labelsize)
#        ax[2,cnt].tick_params(labelsize=ticksize)
#        text = ax[2,cnt].yaxis.get_offset_text()
#        text.set_size(offsetsize)
    
    
    ax[1,wd_i].plot(x1*ul,tr1,linewidth=plotline_width,\
      label='t = '+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    ax[1,wd_i].plot(x1*ul,tr10,linewidth=plotline_width0,\
      linestyle='dashed',label='t='+"{0:.2f}".format(0.0)+r'$t_{\rm cool}$',\
      color=col0, zorder=3)
    
    ax[1,wd_i].set_xlabel(r'x (kpc)',fontsize=labelsize)
    if wd_i ==0:
        ax[1,wd_i].set_ylabel(r'Z ($Z\odot$)',fontsize=labelsize)
    ax[1,wd_i].tick_params(labelsize=ticksize)
#    ax[3,cnt].legend(fontsize=35,loc='upper right')
    text = ax[1,wd_i].yaxis.get_offset_text()
    text.set_size(offsetsize)
    ax[1,wd_i].legend(fontsize=legendsize)
    
    ax[0,wd_i].set_xlim(x1[0]*ul,x1[-1]*ul)
    ax[1,wd_i].set_xlim(x1[0]*ul,x1[-1]*ul)
#        ax[2,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)
#        ax[3,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)

plt.savefig(wdir_script+'/nonlinear/nonlinear_ic_outflow.png')
