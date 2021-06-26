#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:05:42 2019

@author: hitesh
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

global T_tab, A, B, l

def InterpAB(T):
    i=0; j=l-1
    while (i != (j-1)):
        mid = int((i+j)/2)
        T_mid = T_tab[mid]
        
        if (T > T_mid):
            i = mid
        if (T < T_mid):
            j = mid

    Ai = A[i]
    Aj = A[j]
    
    Bi = B[i]
    Bj = B[j]
    
    Ti = T_tab[i]
    Tj = T_tab[j]
    
    dT = T_tab[j] - T_tab[i]
    
    A_intp = Ai*(Tj-T)/dT + Aj*(T-Ti)/dT;
    B_intp = Bi*(Tj-T)/dT + Bj*(T-Ti)/dT;
    
    return A_intp,B_intp

def lam(T,Z):
    A, B = InterpAB(T)
    lam_fn = A + B*Z
    
    return lam_fn

def lamT(T,Z):
    dT = 0.15*T
    lam0 = lam(T, Z)
    lam0p = lam(T+dT, Z)
      
    dlam0 = lam0p-lam0
    lamT_fn = (T/lam0)*(dlam0/dT)
    
    return lamT_fn

def lamZ(T,Z):
    dZ = 0.001
    lam0 = lam(T, Z)
    lam0p = lam(T, Z+dZ)
      
    dlam0 = lam0p-lam0
    lamZ_fn = (Z/lam0)*(dlam0/dZ)
    
    return lamZ_fn

def MMWt_muH(ZbyZsun):
    Xsol = 0.7065
    Ysol = 0.2806
    Zsol = 1.-Xsol-Ysol
    
    Z = Zsol*ZbyZsun;
    X = (1.-Z)*Xsol/(1.-Zsol);
    return 1./X

def MMWt_mu(ZbyZsun):
    Xsol = 0.7065
    Ysol = 0.2806
    Zsol = 1.-Xsol-Ysol
    Z = Zsol*ZbyZsun
    X = (1.-Z)*Xsol/(1.-Zsol)
    Y = (1.-Z)*Ysol/(1.-Zsol)
    
    return 1./(2.*X+0.75*Y+9.*Z/16.)

D = np.loadtxt('Data/CT_WSS09.dat')
T_tab = D[:,0];
A = D[:,1];
B = D[:,2];
l=np.size(T_tab)
