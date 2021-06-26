#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:54:16 2020

@author: hitesh
"""
import os
wdir_script = os.getcwd()
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf
import fourier as fr
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as mticker

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir = wd.wdir83

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = ut*0.01 # in Myr

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

c_arr = ['tab:red','tab:blue','tab:red','tab:blue']
ls_arr = ['solid','solid','dashed','dashed']
mark_arr = ['o','^','o','^']
label_arr = ['Unstable','Stable','Unstable (periodic)','Stable (periodic)']
title_arr = ['NIC_ST_OF/NIC_UST_OF','NIC_ST_P/NIC_UST_P',\
             'NIC_ST_ME/NIC_UST_ME','NIC_ST_RN/NIC_UST_RN']

wdir_list = [[wd.wdir72,wd.wdir73],\
             [wd.wdir82,wd.wdir83],\
             [wd.wdir74,wd.wdir75],\
             [wd.wdir76,wd.wdir77],]

fig,ax = plt.subplots(4,4,figsize=(50,40))

labelsize =40
ticksize  =35
titlesize =45 
offsetsize=35
legendsize=30

#t_arr = np.array([550,2700,3355])

col_cnt = -1

for wdir_set in wdir_list:
    col_cnt +=1
    set_cnt = -1
    for wdir in wdir_set:
        cnt=-1
        set_cnt+=1
        
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
        
        if set_cnt==1:
            t_arr = np.array([[0,2500,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,2500,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,1800,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,1580,nlinf['nlast']-50,nlinf['nlast']-50]])
#            t_arr = np.array([[0,2500,nlinf['nlast']-50,0],\
#                             [0,2500,nlinf['nlast']-50,0],\
#                             [0,1800,nlinf['nlast']-50,0],\
#                             [0,1580,nlinf['nlast']-50,0]])
            ls = 'solid'
            ms = 'o'
            c = 'tab:orange'
            lw = 10
            lwf = 4
            zo = -2
        else:
            t_arr = np.array([[0,200,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,200,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,200,nlinf['nlast']-50,nlinf['nlast']-50],\
                             [0,200,nlinf['nlast']-50,nlinf['nlast']-50]])
#            t_arr = np.array([[0,200,nlinf['nlast']-50,0],\
#                             [0,200,nlinf['nlast']-50,0],\
#                             [0,200,nlinf['nlast']-50,0],\
#                             [0,200,nlinf['nlast']-50,0]])
            ls = 'dashed'
            ms = '^'
            c = 'tab:blue'
            lw = 5
            lwf = 4
            zo = 0
            
        ax[0,col_cnt].set_title(title_arr[col_cnt],fontsize=titlesize,y=1.125)
        
        for t in t_arr[col_cnt]:
            cnt +=1
            
            D = pp.pload(t,w_dir=wdir+'output/')
            
            ln = int(np.size(D.x1)/2)
            dln = 3000
            
            rho = D.rho[ln-dln:ln+dln]
            x1 = D.x1[ln-dln:ln+dln]
            
            L = x1[-1]-x1[0]
            
            ntc = t/tc_min
            
            col = 'tab:green'
            
            if cnt<3:
                if cnt!=0:
                    ax[cnt,col_cnt].set_yscale('log')
                    formatter = mticker.ScalarFormatter(useMathText=True)
                    formatter.set_powerlimits((-3,2))
                    ax[0,cnt].yaxis.set_major_formatter(formatter)
                else:
                    formatter = mticker.ScalarFormatter(useMathText=True)
                    formatter.set_powerlimits((-3,2))
                    ax[0,cnt].yaxis.set_major_formatter(formatter)
                if cnt!=0:
                    ax[cnt,col_cnt].set_yscale('log')
                ax[cnt,col_cnt].plot(x1*ul,rho,linewidth=lw,color=c,linestyle=ls,zorder=zo,label="{0:.2f}".format(ntc)+r'$t_{\rm cool}$')
                if cnt==2:
                    ax[cnt,col_cnt].set_xlabel(r'x (kpc)',fontsize=labelsize)
                if col_cnt==0:
                    ax[cnt,col_cnt].set_ylabel(r'$\rho$ (amu $cm^{-3}$)',fontsize=labelsize)
                ax[cnt,col_cnt].tick_params(labelsize=ticksize)
                ax[cnt,col_cnt].legend(fontsize=legendsize,loc='upper right')
                text = ax[cnt,col_cnt].yaxis.get_offset_text()
                text.set_size(offsetsize)
            
            else:
                E_arr,k_bin = fr.fourier_bin(wdir,t)
                ax[cnt,col_cnt].plot(k_bin,E_arr,linewidth=lwf,color=c,linestyle=ls,label=label_arr[set_cnt])
                ax[cnt,col_cnt].scatter(k_bin,E_arr,marker=ms,color=c,s=100)
                
                ax[cnt,col_cnt].set_xscale('log')
                ax[cnt,col_cnt].set_yscale('log')
                
                ax[cnt,col_cnt].tick_params(labelsize=ticksize)
                
                ax[cnt,col_cnt].set_xlabel(r'k (kpc$^{-1}$)',fontsize=labelsize)
                if col_cnt==0:
                    ax[cnt,col_cnt].set_ylabel(r'$E_\rho$',fontsize=labelsize)
                ax[cnt,col_cnt].legend(fontsize=legendsize,loc='upper right')

plt.savefig(wdir_script+'/Fourier/Fourier_rho.png')