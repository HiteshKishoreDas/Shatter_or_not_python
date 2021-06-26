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

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']


CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB


for wdir in [wd.wdir107]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    ut = ((ul * 3.086E+21)/uv)  # in s
    ut = (ut / 3.154e+13)    # in Myr
    
#    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 0.01*ut#1.0 # in Myr ############################

    box_size=4.0
    
    m=-0.05
    c=0.5
    
    def boxplot(dr,dr0,drx,i,st,shock,flag,logflag):
            
        drx = np.multiply(ul,drx)
        
        if (flag):
            t = np.round(i*dt,4)
#            t = np.round(541*dt + (i-541)*0.01*dt,4)
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot(1,1,1)
#            ax.set_ylim(np.max(dr)-0.01,np.max(dr)+0.005)
            if logflag:
                ax.set_yscale('log')
            ax.plot(drx,dr,label=str(i),c='tab:red',linewidth=0.3)
#            ax.plot(drx,dr0,label='0',c='tab:blue',linewidth=0.1)
            ax.scatter(drx[np.nonzero(shock)],dr[np.nonzero(shock)],s=30,label='shock',marker='o',color='g')
            ax.set_xlabel(r'x (in kpc)')
            ax.set_ylabel(st)
#            ax.set_yaxis("log")
#            ax.set_xlim(195.,205.)
            ax.legend()
#            ax.grid()
            ax.set_title(st + ': ' + str(t) + ' Myr')
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
    
    isperiodic = True  #*********************
    
    D0 = pp.pload(0,w_dir=wdir+'output/')
    T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
    logT0 = np.log10(T0)
    
    ln = int(np.size(D0.x1)/2)
    dln = 510
    
    if isperiodic:
        rho0 = D0.rho
        prs0 = D0.prs
        vx10 = D0.vx1 * UNIT_VELOCITY
        tr10 = D0.tr1
        tr20 = D0.tr2
        x10 = D0.x1
    else:
        rho0 = D0.rho[ln-dln:ln+dln]
        prs0 = D0.prs[ln-dln:ln+dln]
        T0 = T0[ln-dln:ln+dln]
        vx10 = D0.vx1[ln-dln:ln+dln] * UNIT_VELOCITY
        tr10 = D0.tr1[ln-dln:ln+dln]
        tr20 = D0.tr2[ln-dln:ln+dln]
        x10 = D0.x1[ln-dln:ln+dln]
        
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
#        ln = int(np.size(D1.x1)/2)
#        dln = 500
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        logT = np.log10(T)
        
        if isperiodic:
            rho = D1.rho
            prs = D1.prs
            vx1 = D1.vx1 * UNIT_VELOCITY
            tr1 = D1.tr1
            tr2 = D1.tr2
            x1 = D1.x1
            sk = D1.sk
        else:
            rho = D1.rho[ln-dln:ln+dln]
            prs = D1.prs[ln-dln:ln+dln]
            T = T[ln-dln:ln+dln]
            vx1 = D1.vx1[ln-dln:ln+dln] * UNIT_VELOCITY
            tr1 = D1.tr1[ln-dln:ln+dln]
            tr2 = D1.tr2[ln-dln:ln+dln]
            x1 = D1.x1[ln-dln:ln+dln]
            sk = D1.sk[ln-dln:ln+dln]
        
        
        boxplot(prs,prs0,x1,i,'prs',sk,1,0)
        
#        boxplot(np.log10(np.abs(vx1)),np.log10(np.abs(vx10)),x1,i,'vx_abs_log',sk,1)
        boxplot(vx1,vx10,x1,i,'vx',sk,1,0)
        
        boxplot(rho,rho0,x1,i,'density',sk,1,False)
        
        boxplot(tr1,tr10,x1,i,'z',sk,1,0)
        boxplot(tr2,tr20,x1,i,'x',sk,1,0)
        
        boxplot(T,T0,x1,i,'logT',sk,1,1)
        
        del(D1)
