#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:01:08 2020

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
UNIT_VELOCITY = 1e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

labelsize = 40
ticksize = 35
titlesize = 40 
offsetsize = ticksize
plotline_width = 5

col = 'tab:blue'

left   = 0.15   # the left side of the subplots of the figure
right  = 0.9   # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top    = 0.8   # the top of the subplots of the figure
wspace = 0.27   # the amount of width reserved for blank space between subplots
hspace = 0.32   # the amount of height reserved for white space between subplots


wdir_list = [wd.wdir82,wd.wdir83]   #*****************
state_list = ['unstable','stable']
periodic_tag = True

for wd_i,wdir in enumerate(wdir_list):
    
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    t_arr = [np.array([0,nlinf['nlast']-2100,nlinf['nlast']-200]),\
             np.array([0,nlinf['nlast']-600,nlinf['nlast']-100])]
    
    t_arr = t_arr[wd_i]
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    lam0 =  np.zeros(np.size(D0.x1),dtype=float)
    
    n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1,D0.tr2)*CONST_amu)
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1,D0.tr2)
    for i in range(np.size(D0.x1)):
        lam0[i] = lf.lam(T0[i],D0.tr1[i])
    q0 = n_H0*n_H0*lam0/unit_q
    tc0 = D0.prs/(q0*(gamma - 1))
    tc_min = np.min(tc0)*ut
    
    fig,ax = plt.subplots(4,3,figsize=(25,25))
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
    
    
    cnt = 0
#    t_arr = np.array([550,2700,3355])
#    t_arr = np.array([1508,1509,1510])
#    t_arr = np.array([1000,1500,3000])
#    t_arr = np.array([0,nlinf['nlast']-600,nlinf['nlast']-100])
    
    for t in t_arr:
        D = pp.pload(t,w_dir=wdir+'output/')
        
        T  = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)
        
        ln = int(np.size(D.x1)/2)
        dln = 3000
    
    
        if periodic_tag:
            rho = D.rho
            prs = D.prs* UNIT_DENSITY*UNIT_VELOCITY**2
            vx1 = D.vx1* UNIT_VELOCITY
            tr1 = D.tr1
            x1 = D.x1
        else:
            rho = D.rho[ln-dln:ln+dln]
            prs = D.prs[ln-dln:ln+dln]
            T = T[ln-dln:ln+dln]
            vx1 = D.vx1[ln-dln:ln+dln]* UNIT_VELOCITY#
            tr1 = D.tr1[ln-dln:ln+dln]
            x1 = D.x1[ln-dln:ln+dln]
        
        
        ntc = t/tc_min
        
        if cnt!=0:
            ax[0,cnt].set_yscale('log')
        else:
            formatter = mticker.ScalarFormatter(useMathText=True)
            formatter.set_powerlimits((-3,2))
            ax[0,cnt].yaxis.set_major_formatter(formatter)
        
    
        ax[0,cnt].plot(x1*ul,rho,linewidth=plotline_width,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    #    if cnt==2:
    #        ax[0,cnt].set_xlabel(r'x (kpc)',fontsize=35)
        if cnt==0:    
            ax[0,cnt].set_ylabel(r'$\rho$ (amu cm$^{-3}$)',fontsize=labelsize)
        ax[0,cnt].tick_params(labelsize=labelsize)
        ax[0,cnt].set_title('t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',fontsize=titlesize,y=1.2)
        text = ax[0,cnt].yaxis.get_offset_text()
        text.set_size(offsetsize)
        
        ax[0,cnt].tick_params(axis="x", direction="inout", length=8, width=2)
        ax[0,cnt].tick_params(axis="y", direction="inout", length=8, width=2)
    
        ax[0,cnt].tick_params(axis="x", which='minor', direction="in", length=4, width=1)
        ax[0,cnt].tick_params(axis="y", which='minor', direction="in", length=4, width=1)    
    
        
    ######################
        
        if cnt==4:
            ax[1,cnt].set_yscale('log')
        else:
            formatter = mticker.ScalarFormatter(useMathText=True)
            formatter.set_powerlimits((-3,2))
            ax[1,cnt].yaxis.set_major_formatter(formatter)
            
        ax[1,cnt].plot(x1*ul,prs,linewidth=plotline_width,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    #    if cnt==2:
    #        ax[1,cnt].set_xlabel(r'x (kpc)',fontsize=35)
        if cnt==0:
            ax[1,cnt].set_ylabel(r'p (dyne cm$^{-2}$)',fontsize=labelsize)
        ax[1,cnt].tick_params(labelsize=labelsize)
        text = ax[1,cnt].yaxis.get_offset_text()
        text.set_size(offsetsize)
        
        ax[1,cnt].tick_params(axis="x", direction="inout", length=8, width=2)
        ax[1,cnt].tick_params(axis="y", direction="inout", length=8, width=2)
    
        ax[1,cnt].tick_params(axis="x", which='minor', direction="in", length=4, width=1)
        ax[1,cnt].tick_params(axis="y", which='minor', direction="in", length=4, width=1)    
    
    #######################
        
        if cnt!=0:
            ax[2,cnt].set_yscale('log')
        else:
            formatter = mticker.ScalarFormatter(useMathText=True)
            formatter.set_powerlimits((-3,2))
            ax[2,cnt].yaxis.set_major_formatter(formatter)
            
        ax[2,cnt].plot(x1*ul,T,linewidth=plotline_width,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
    #    if cnt==2:
    #        ax[1,cnt].set_xlabel(r'x (kpc)',fontsize=35)
        if cnt==0:
            ax[2,cnt].set_ylabel(r'T (K)',fontsize=labelsize)
        ax[2,cnt].tick_params(labelsize=labelsize)
        text = ax[2,cnt].yaxis.get_offset_text()
        text.set_size(offsetsize)
        
        ax[2,cnt].tick_params(axis="x", direction="inout", length=8, width=2)
        ax[2,cnt].tick_params(axis="y", direction="inout", length=8, width=2)
        
        ax[2,cnt].tick_params(axis="x", which='minor', direction="in", length=4, width=1)
        ax[2,cnt].tick_params(axis="y", which='minor', direction="in", length=4, width=1)    
    
        
    ##########################
        
        formatter = mticker.ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-3,2))
        ax[3,cnt].yaxis.set_major_formatter(formatter)
        ax[3,cnt].plot(x1*ul,vx1,linewidth=plotline_width,label='t='+"{0:.2f}".format(ntc)+r'$t_{\rm cool}$',color=col)
        ax[3,cnt].set_xlabel(r'x (kpc)',fontsize=labelsize)
        if cnt==0:
            ax[3,cnt].set_ylabel(r'$V_x$ (cm s$^{-1}$)',fontsize=labelsize)
        ax[3,cnt].tick_params(labelsize=ticksize)
        text = ax[3,cnt].yaxis.get_offset_text()
        text.set_size(offsetsize)
            
        ax[3,cnt].tick_params(axis="x", direction="inout", length=8, width=2)
        ax[3,cnt].tick_params(axis="y", direction="inout", length=8, width=2)
    
        ax[3,cnt].tick_params(axis="x", which='minor', direction="in", length=4, width=1)
        ax[3,cnt].tick_params(axis="y", which='minor', direction="in", length=4, width=1)    
    
        ax[0,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)
        ax[1,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)
        ax[2,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)
        ax[3,cnt].set_xlim(x1[0]*ul,x1[-1]*ul)
        
        cnt +=1
    
    plt.savefig(wdir_script+'/nonlinear/nonlinear_ic_'+ str(state_list[wd_i]) +'_periodic.png')
