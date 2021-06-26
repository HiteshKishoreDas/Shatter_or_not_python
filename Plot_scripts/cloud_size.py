#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:51:20 2020

@author: hitesh
"""
import os
wdir_script = os.getcwd()
import numpy as np
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

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
#ut = ((ul * 3.086E+21)/uv)  # in s
#ut = (ut / 3.154e+13)    # in Myr

ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 1.0 # in Myr


def cloud_size (wdir,t,dln,periodic_flag=False):
    """
    To calculate cloud size
    Input: Data directory, time_index, half-size
    Output: List of cloud size in kpc
    """
    D = pp.pload(t,w_dir=wdir+'output/')
    
    T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)
    
    ln = int(np.size(D.x1)/2)
    
    if periodic_flag:
        x1 = D.x1*ul
    else:
        T = T[ln-dln:ln+dln]
        x1 = D.x1[ln-dln:ln+dln]*ul
    dx = x1[1]-x1[0]
    box = np.size(x1)
    
    T_lim = 1e5  #********************
    
    cloud_ind = np.array(np.where(T<T_lim)[0])
    cloud_size = []
    
    
    if np.size(cloud_ind)==0:
        return cloud_size,dx
    cld_start = x1[cloud_ind[0]]
    N = np.size(cloud_ind)
    for i in range(N):
        if i==N-1:
            if periodic_flag:
                if cloud_ind[i]==box-1 and N!=0:
                    if len(cloud_size)!=0:
                        cloud_size[0] += x1[cloud_ind[i]]+dx-cld_start
                    else:
                        cloud_size.append(x1[cloud_ind[i]]+dx-cld_start)
                else:
                    cloud_size.append(x1[cloud_ind[i]]+dx-cld_start)
            else:
                cloud_size.append(x1[cloud_ind[i]]+dx-cld_start)
            
        elif cloud_ind[i+1]==cloud_ind[i]+1:
            continue
        
        else:
            cloud_size.append(x1[cloud_ind[i]]+dx-cld_start)
            cld_start = x1[cloud_ind[i+1]]
            
    return cloud_size,dx

if __name__=='__main__':
    label_arr = ['Unstable','Stable']
    title_arr = ['Single eigenmode','Single eigenmode (Periodic)',\
                 'Mixed eigenmode','Random noise','Isobaric']
    
    
    wdir_list = [[wd.wdir72,wd.wdir73],\
                 [wd.wdir82,wd.wdir83],\
                 [wd.wdir74,wd.wdir75],\
                 [wd.wdir76,wd.wdir77],\
                 [wd.wdir86,wd.wdir86]]
    
    plot_cnt = -1
    for wdir_set in wdir_list:
        plot_cnt +=1
        fig,ax = plt.subplots(2,2,figsize=(12,12))
        fig.suptitle(title_arr[plot_cnt],fontsize=30)#+' (After ~45 Myr)'
        cnt = -1
        for wdir in wdir_set:
            cnt +=1
            
            dln = 3000
            
            nlinf = pp.nlast_info(w_dir=wdir+'output/')
            t = nlinf['nlast']-50  #****************
            cloud_s,res = cloud_size(wdir,t,dln)
            
            D = pp.pload(t,w_dir=wdir+'output/')
                
            T = D.prs/D.rho*KELVIN*lf.MMWt_mu(D.tr1,D.tr2)
            
            ln = int(np.size(D.x1)/2)
            dln = 3000   #*****************
            
            T = T[ln-dln:ln+dln]
            x1 = D.x1[ln-dln:ln+dln]*ul
    #        res = x1[1]-x1[0]
            
            ax[0][cnt].set_title(label_arr[cnt],fontsize=25)
            
            ax[0][cnt].set_yscale('log')
            ax[0][cnt].plot(x1,T)
            ax[0][cnt].set_xlabel('x (kpc)',fontsize=20)
            ax[0][cnt].set_ylabel('T (K)',fontsize=20)
            ax[0][cnt].tick_params(labelsize=15)
    
            bnw = res/100.
            bin_list = np.arange(min(cloud_s)-5*bnw, max(cloud_s)+5*bnw, bnw)
            hist=np.histogram(cloud_s,bins=bin_list)
            ax[1][cnt].plot(hist[1][:-1]+bnw/2.,hist[0],linewidth=3)
            ax[1][cnt].scatter(hist[1][:-1]+bnw/2.,hist[0])
            
            ax[1][cnt].minorticks_on()
            ax[1][cnt].set_xlabel('Cloud size (kpc)\nSpatial resolution: '+str(np.round(res,4))+' kpc',fontsize=20)
            ax[1][cnt].set_ylabel('Count',fontsize=20)
            ax[1][cnt].tick_params(labelsize=15)
            
            fig.tight_layout()
            fig.subplots_adjust(top=0.88)
            
        plt.savefig(wdir_script+'/Cloud_size/Cloud_size_'+title_arr[plot_cnt]+'.png')