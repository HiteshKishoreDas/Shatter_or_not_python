#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:29:37 2020

@author: hitesh
"""
import os
import numpy as np
import dcst

wdir_script = os.getcwd()

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

def fourier_bin(wdir,t):
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    ln = int(np.size(D0.x1)/2)#+ 250 + 265
    dln = 3000
    
    rho0 = D0.rho[ln-dln:ln+dln]
    x0 = D0.x1[ln-dln:ln+dln]
    
    L = x0[-1]-x0[0]
    
    rho_k0 = dcst.dct(rho0)
    rho_k0 = np.abs(rho_k0)
    
    k_arr = np.zeros(np.size(rho_k0),dtype=float)
    k_arr = np.array([k for k in range(np.size(k_arr))])
    
    k_arr = k_arr[1:]*2*np.pi/(L*ul)
    
    kmax = k_arr[np.size(k_arr)-1]
    kmin = k_arr[0]
    
    nbin = 25
    
    k_bin = [kmin*(kmax/kmin)**(i/nbin) for i in range(nbin+1)]
    k_bin_mid = [k_bin[i]+(k_bin[i+1]-k_bin[i])/2. for i in range(nbin)]
    
#    t = nlinf['nlast']
    
    D1 = pp.pload(t,w_dir=wdir+'output/')
    
    rho = D1.rho[ln-dln:ln+dln]
    
    rho_k = dcst.dct(rho)
    rho_k = np.abs(rho_k)
    
    rho_k = rho_k[1:]    
    
    E_arr = np.zeros(np.size(k_bin),dtype=float)
    i = 0
    j = 0
    E = 0
    
    delk = k_bin[1] - k_bin[0]
    while j < np.size(k_arr)-1:
#        print(i,j)
        if k_bin[i]<=k_arr[j]<k_bin[i+1]:
            E =+ rho_k[j]**2/delk
            j +=1
        else:
            E_arr[i] = E
            E = 0
            i +=1
            delk = k_bin[i+1] - k_bin[i]
#            print(delk)
    
    ind_nonzero = np.array(np.nonzero(E_arr)[0],dtype=int)
    
    E_arr = E_arr[ind_nonzero]
    k_bin = [k_bin_mid[i] for i in ind_nonzero]
    
    del(D1)
    
    return E_arr,k_bin


#def fourier_kt_imshow (wdir,t_skip,nbin):
#    nlinf = pp.nlast_info(w_dir=wdir+'output/')
#        
#    D0 = pp.pload(0,w_dir=wdir+'output/')
#        
#    ln = int(np.size(D0.x1)/2)#+ 250 + 265
#    dln = 3000
#    
#    rho0 = D0.rho[ln-dln:ln+dln]
#        
#    rho_k0 = dcst.dct(rho0)
#    rho_k0 = np.abs(rho_k0)
#    
#    kt_bin_arr = np.zeros((nbin-1,int(nlinf['nlast']/t_skip)+1),dtype=float)
##    kt_arr = np.zeros((dln*2-1,int(nlinf['nlast']/t_skip)+1),dtype=float)
#    for t in range(nlinf['nlast']):
#        if t%t_skip==0:
#            k_arr = np.zeros(np.size(rho_k0),dtype=float)
#            k_arr = np.array([k for k in range(np.size(k_arr))])
#            
#            k_arr = k_arr[1:]
#            
#            kmax = k_arr[np.size(k_arr)-1]
#            kmin = k_arr[0]
#            
#            k_bin = [kmin*(kmax/kmin)**(i/nbin) for i in range(nbin+1)]
#            
#            D1 = pp.pload(t,w_dir=wdir+'output/')
#            
#            rho = D1.rho[ln-dln:ln+dln]
#            
#            rho_k = dcst.dct(rho)
#            rho_k = np.abs(rho_k)
#            
#            rho_k = rho_k[1:]    
#            
#            E_arr = np.zeros(np.size(k_bin),dtype=float)
#            i = 0
#            j = 0
#            E = 0
#            while j < np.size(k_arr)-1:
#        #        print(i,j)
#                delk = k_bin[i+1] - k_bin[i] 
#                if k_bin[i]<=k_arr[j]<k_bin[i+1]:
#                    E =+ rho_k[j]**2/delk
#                    j +=1
#                else:
#                    E_arr[i] = E
#                    E = 0
#                    i +=1
#            
#    #        ind_nonzero = np.array(np.nonzero(E_arr)[0],dtype=int)
#    #        
#    #        E_arr = E_arr[ind_nonzero]
#    #        k_bin = [k_bin[i] for i in ind_nonzero]
#                    
#            kt_bin_arr[:,int(t/t_skip)] = np.log10(E_arr[:-2]) #E_arr#       
#            del(D1)
#            
#    return kt_bin_arr