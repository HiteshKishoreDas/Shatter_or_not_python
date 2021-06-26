#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
import lamfn as lf
import workdir as wd

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


for wdir in [wd.wdir40]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr

    box_size=4.0
    
    m=-0.05
    c=0.5
    
    def boxplot(dr,dr0,drx,i,st,shock,flag):
            
        drx = np.multiply(ul,drx)
        
        if (flag):
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot(1,1,1)
            ax.plot(drx,dr,label=str(i),c='tab:red',linewidth=0.3)
            ax.plot(drx,dr0,label='0',c='tab:blue',linewidth=0.3)
            ax.scatter(drx[np.nonzero(shock)],dr[np.nonzero(shock)],s=30,label='shock',marker='o',color='g')
            ax.set_xlabel(r'x (in kpc)')
            ax.set_ylabel(st)
#            ax.set_yaxis("log")
#            ax.set_xlim(195.,205.)
            ax.legend()
#            ax.grid()
            ax.set_title(st + ': ' + str(i*dt) + ' Myr')
            fig.savefig(wdir+'Plots_full_log/' + st + '/' +st+ '_' + str(i) +'.png')
            ax.cla()
            fig.clf()
            plt.close(fig)
            del(fig)
            del(ax)
    #        gc.collect(2)
        else:
            plt.figure(figsize=(10,10))
            plt.plot(range(np.size(dr)),dr,label=str(i))
            plt.plot(range(np.size(dr0)),dr0,label='0')
            plt.xlabel(r'index')
            plt.ylabel(st)
            plt.legend()
            plt.grid()
            plt.title(st + ': ' + str(i*dt) + ' Myr')
            plt.savefig(wdir+'Plots/' + st + '/' +st+ '_' + str(i) +'.png')
            plt.close()
    #        gc.collect(2)    
        return 0
    
            
    
    #col = ['r','g','k','b']
    #cnt = 0
    
    plt.figure(figsize=(10,10))
    
    peak = 0.0
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
    logT0 = np.log10(T0)
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
        ln = int(np.size(D1.x1)/2)
        dln = 600
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        logT = np.log10(T)
        
        boxplot(np.log10(D1.prs),np.log10(D0.prs),D1.x1,i,'prs_log',D1.sk,1)
        
        boxplot(np.log10(np.abs(D1.vx1)),np.log10(np.abs(D0.vx1)),D1.x1,i,'vx_abs_log',D1.sk,1)
        boxplot(D1.vx1,D0.vx1,D1.x1,i,'vx',D1.sk,1)
        
        boxplot(np.log10(D1.rho),np.log10(D0.rho),D1.x1,i,'density_log',D1.sk,1)
        
        boxplot(D1.tr1,D0.tr1,D1.x1,i,'z',D1.sk,1)
        
        boxplot(logT,logT0,D1.x1,i,'logT',D1.sk,1)
        
        del(D1)
