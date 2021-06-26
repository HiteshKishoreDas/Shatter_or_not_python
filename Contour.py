#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:26:57 2019

@author: Hitesh Kishore Das
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3d
from scipy import interpolate


plutodir = os.environ['PLUTO_DIR']

wdir = plutodir+ 'TI_uniform/metallicity_thd_run/Contour/'

m = 4999
n = 5000

lamT = np.zeros((m,n),dtype= float)
lamZ = np.zeros((m,n),dtype= float)

fT = open(wdir+'lam_cont_T.txt', 'r+')
for i in range (m):    
    var = fT.readline()
    var = str(var)
    var = var.split(" ")
    var = var[:-1]
    lamT[i,:] = var
fT.close()

fZ = open(wdir+'lam_cont_Z.txt', 'r+')
for j in range (m):    
    var = fZ.readline()
    var = str(var)
    var = var.split(" ")
    var = var[:-1]
    lamZ[j,:] = var
fZ.close()

x = np.zeros(n,dtype=float)
y = np.zeros(m,dtype=float)

N = n

Tbeg = 5000000.0;
Tend = 50000000.0;
Zbeg = 0.2;
Zend = 0.7;

dT = (Tend - Tbeg)/N;
dZ = (Zend - Zbeg)/N;

for k in range(n):
    x[k] = Zbeg + k*dZ
    
for l in range(m):
    y[l] = Tbeg + l*dT

X, Y = np.meshgrid(x, y)

#Xnew, Ynew = np.mgrid[Zbeg:Zend:10000j, Tbeg:Tend:10000j]
#tck = interpolate.bisplrep(X, Y, lamT, s=0)
#lamT_new = interpolate.bisplev(Xnew[:,0], Ynew[0,:], tck)

#print(np.size(X))

#f = interpolate.interp2d(x, y, lamT, kind='quintic')
#xnew = np.linspace(Zbeg, Zend, num=10000)
#ynew = np.linspace(Tbeg, Tend, num=10000)
#lamT_new = f(xnew,ynew)
#
#Xnew, Ynew = np.meshgrid(xnew, ynew)

fig,ax = plt.subplots(figsize=(20,20))
#ax = fig.gca(projection='3d')

ax.contour(X,Y,lamT,cmap="jet",vmin=-0.5, vmax=0.5)
ax.scatter(X,Y, marker = '.',color='k',s = 0.00002)
#ax.contour(X,Y,lamZ,cmap="jet",vmin=-0.5, vmax=0.5)

plt.title("lamT and lamZ",fontsize=30)
plt.xlabel("Z",fontsize = 20)
plt.ylabel("T",fontsize = 20)

wdir = plutodir+ 'TI_uniform/metallicity_thd_run/output/'

plt.savefig(wdir+'lam.png')
plt.close(fig)
del(fig)
del(ax)

