#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
#import begend as bg


os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']
wdir1 = plutodir+ 'TI_uniform/metallicity/output/'#Output_Archive/No_perturbation/wocool_nopert_wogradz_t20/output/'
wdir2 = plutodir+ 'TI_uniform/metallicity_sec_run/output/'
wdir3 = plutodir+ 'TI_uniform/metallicity_thd_run/output/'

for wdir in [wdir1,wdir2,wdir3]:
    nlinf = pp.nlast_info(w_dir=wdir)
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.05
    c = 0.5
    
    def boxplot(dr,dr0,drx,i,st,shock,flag):
        
    #    D0 = pp.pload(0,w_dir=wdir)
    #    
    #    data_dict['prs0'] = D0.prs
    #    data_dict['rho0'] = D0.rho
    #    data_dict['vx10'] = D0.vx1
    #    data_dict['z0'] = D0.tr1
    #    data_dict['zfluc0'] = D0.tr1 - (c - m*D0.x1)
    #    
    #    for i in range(100):#nlinf['nlast']+1):
    #        D1 = pp.pload(i,w_dir=wdir) # Loading the data into a pload object D.
    #        
    #        data_dict['x'] = D1.x1
    #        data_dict['prs'] = D1.prs
    #        data_dict['rho'] = D1.rho
    #        data_dict['vx1'] = D1.vx1
    #        data_dict['z'] = D1.tr1
    #        data_dict['zfluc'] = D1.tr1 - (c - m*D1.x1)
    #        
    #    for st in ['prs','rho','vx1','z','zfluc']:
    #        
    #        dr = data_dict[st]
    #        dr0 = data_dict[st+'0']
    #        drx = data_dict[x]
            
        drx = np.multiply(ul,drx)
        
        if (flag):
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot(1,1,1)
            ax.plot(drx,dr,label=str(i))
            ax.plot(drx,dr0,label='0')
            ax.scatter(drx[np.nonzero(shock)],dr[np.nonzero(shock)],s=30,label='shock',marker='o',color='g')
            ax.set_xlabel(r'x (in kpc)')
            ax.set_ylabel(st)
            ax.legend()
            ax.grid()
            ax.set_title(st + ': ' + str(i*dt) + ' Myr')
            fig.savefig(wdir+'Plots/' + st + '/' +st+ '_' + str(i) +'.png')
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
    
    D0 = pp.pload(0,w_dir=wdir)
    for i in range(300):#nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir) # Loading the data into a pload object D.
        
        boxplot(D1.prs,D0.prs,D1.x1,i,'prs',D1.sk,1)
        boxplot(D1.vx1,D0.vx1,D1.x1,i,'vx',D1.sk,1)
        boxplot(D1.rho,D0.rho,D1.x1,i,'density',D1.sk,1)
        boxplot(D1.tr1,D0.tr1,D1.x1,i,'z',D1.sk,1)
        boxplot(D1.tr1 - (m*D1.x1+c),D0.tr1 - (m*D0.x1 + c),D1.x1,i,'zfluc',D1.sk,1)   
        
        boxplot(D1.wr,D0.wr,D1.x1,i,'wr',D1.sk,1)
        boxplot(D1.wi,D0.wi,D1.x1,i,'wi',D1.sk,1)
        
        boxplot(D1.lamT,D0.lamT,D1.x1,i,'lamT',D1.sk,1)
        boxplot(D1.lamZ,D0.lamZ,D1.x1,i,'lamZ',D1.sk,1)
        del(D1)
    
        
        
    #    diff = np.max(D1.prs) - np.max(D0.prs)
    ##    if (i!=0):
    #    #plt.scatter(np.log10(i*dt),np.log10(diff))
    #    plt.scatter(i*dt,np.log10(diff))
    #    print(np.log10(diff),diff)    
    #
    ##plt.axis([0,2001,-10,10])
    #    
    #nm = "prs"
    #plt.xlabel('(time in Myr)')
    #plt.ylabel('log(max-min) of '+nm)
    #plt.title("log(max-min) of "+nm+" vs. time for no perturbation")
    #plt.grid()
    #plt.savefig(wdir+'Plots/'+nm+'_diff.png')
    ##plt.show()