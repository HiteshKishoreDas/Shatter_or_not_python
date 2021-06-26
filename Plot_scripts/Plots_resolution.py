#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:48:14 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd

import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

wdir_list = [wd.wdir103,wd.wdir111,wd.wdir112,wd.wdir106]

nlinf1 = pp.nlast_info(w_dir=wdir_list[0]+'output/')
nlinf2 = pp.nlast_info(w_dir=wdir_list[1]+'output/')
nlinf3 = pp.nlast_info(w_dir=wdir_list[2]+'output/')
nlinf4 = pp.nlast_info(w_dir=wdir_list[3]+'output/')

stopN = np.min([nlinf1['nlast'],nlinf2['nlast'],nlinf3['nlast'],nlinf4['nlast']])

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#    ut = 100 # in Myr
dt = 0.0001*ut # in Myr ############################

box_size=4.0

m=-0.05
c=0.5

col = ['r','g','k','b']

plt.figure(figsize=(10,10))

peak = 0.0

isperiodic = True  #*********************

res_list=["20000","30000","40000","50000"]

# ln = int(np.size(D0.x1)/2)
# dln = 510

for i in range(stopN+1):
    fig1,ax1 = plt.subplots(figsize=(10,8))
    fig2,ax2 = plt.subplots(figsize=(10,8))
    fig3,ax3 = plt.subplots(figsize=(10,8))
    fig4,ax4 = plt.subplots(figsize=(10,8))
    
    ax1.set_yscale('log')
    ax4.set_yscale('log')

    cnt = 0
    for wdir in wdir_list:
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        logT = np.log10(T)

    #        ln = int(np.size(D1.x1)/2)
    #        dln = 500    
        
        if isperiodic:
            rho = D1.rho
            prs = D1.prs
            vx1 = D1.vx1 * UNIT_VELOCITY
            tr1 = D1.tr1
            tr2 = D1.tr2
            x1 = D1.x1*ul
            sk = D1.sk
        else:
            rho = D1.rho[ln-dln:ln+dln]
            prs = D1.prs[ln-dln:ln+dln]
            T = T[ln-dln:ln+dln]
            vx1 = D1.vx1[ln-dln:ln+dln] * UNIT_VELOCITY
            tr1 = D1.tr1[ln-dln:ln+dln]
            tr2 = D1.tr2[ln-dln:ln+dln]
            x1 = D1.x1[ln-dln:ln+dln]*ul
            sk = D1.sk[ln-dln:ln+dln]

        ax1.plot(x1,rho,label=res_list[cnt],color=col[cnt])
        ax2.plot(x1,prs,label=res_list[cnt],color=col[cnt])
        ax3.plot(x1,vx1,label=res_list[cnt],color=col[cnt])
        ax4.plot(x1,T,label=res_list[cnt],color=col[cnt])

        cnt +=1
        
    ax1.set_ylabel(r"$\rho$",fontsize=15)
    ax2.set_ylabel(r"pressure",fontsize=15)
    ax3.set_ylabel(r"$v_x$ (cm s$^{-1}$)",fontsize=15)
    ax4.set_ylabel(r"T (K)",fontsize=15)

    ax1.set_xlabel(r"x (kpc)")
    ax2.set_xlabel(r"x (kpc)")
    ax3.set_xlabel(r"x (kpc)")
    ax4.set_xlabel(r"x (kpc)")

    ax1.set_title("t = "+str(np.round(i*dt,4))+" Myr",fontsize=20)    
    ax2.set_title("t = "+str(np.round(i*dt,4))+" Myr",fontsize=20)
    ax3.set_title("t = "+str(np.round(i*dt,4))+" Myr",fontsize=20)
    ax4.set_title("t = "+str(np.round(i*dt,4))+" Myr",fontsize=20)

    ax1.legend(fontsize=10)
    ax2.legend(fontsize=10)
    ax3.legend(fontsize=10)
    ax4.legend(fontsize=10)
        
    fig1.savefig("Resolution_plots/density/density_"+str(i)+".png")
    fig2.savefig("Resolution_plots/prs/prs_"+str(i)+".png")    
    fig3.savefig("Resolution_plots/vx/vx_"+str(i)+".png")
    fig4.savefig("Resolution_plots/logT/logT_"+str(i)+".png")

    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)
    plt.close(fig4)