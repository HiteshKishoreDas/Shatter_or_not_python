#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:48:14 2020

@author: hitesh
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd

# os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

# plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

dt_arr = [0.01,0.1]
t_arr = [[0,300,1000],[0,100,400]]
fname_arr = ['NIC_UST_SQ','NIC_ST_SQ']


fig,ax = plt.subplots(2,1,figsize=(20,30))

labelsize =40
ticksize  =35
titlesize =45 
offsetsize=35
legendsize=40

for i_wd, wdir in enumerate([wd.wdir107b,wd.wdir107c]):
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    ut = ((ul * 3.086E+21)/uv)  # in s
    ut = (ut / 3.154e+13)    # in Myr
    
#    ut = 100 # in Myr
    # t = 2.0 * ut  # in Myr
    dt = dt_arr[i_wd]*ut#1.0 # in Myr ###########################
    
    # isperiodic = True  #*********************
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    # T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
    # logT0 = np.log10(T0)

    tc_i = np.min(lf.tcool(D0))

    ax[i_wd].set_yscale('log')   

    for i in t_arr[i_wd]:
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
        # T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)

        ax[i_wd].plot(D1.x1*ul,D1.rho,linewidth=10,label=str(np.round(i*dt/tc_i,2))+r' $t_{\rm cool,0}$')

        print(tc_i," ")

    ax[i_wd].legend(fontsize=legendsize)
    ax[i_wd].set_xlabel("x (kpc)",fontsize=labelsize)
    ax[i_wd].set_ylabel(r'$\rho$ (amu cm$^{-3}$)',fontsize=labelsize)
    ax[i_wd].tick_params(labelsize=ticksize)
    ax[i_wd].set_title(fname_arr[i_wd],fontsize=titlesize)


    # fig_tc=plt.figure()
    # ax_tc = fig_tc.add_subplot(111)
    # ax_tc.plot(D0.x1,lf.tcool(D0))
    # fig_tc.savefig("nonlinear_initial_condition/initial_tcool"+str(i_wd)+".png")

fig.savefig("nonlinear_initial_condition/nonlin_initial.png")
        
        
        