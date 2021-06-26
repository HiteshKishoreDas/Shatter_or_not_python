#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 16:01:07 2019

@author: Hitesh Kishore Das
"""
## To plot contour plot for lambdaT and lambdaZ (logarithmic derivatives)


import lamfn as lf

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.colors

Tbeg = 10000000.0;
Tend = 50000000.0;
Zbeg = 0.2;
Zend = 0.7;

N = 50
M = 60

x = np.linspace(Zbeg,Zend,num = N)
y = np.linspace(Tbeg,Tend,num = M)

X, Y = np.meshgrid(x, y)

lamT_arr = np.zeros((M,N),dtype=float)
lamZ_arr = np.zeros((M,N),dtype=float)

for i in range(M):
    for j in range(N):
        lamT_arr[i,j] = lf.lamT(Y[i,j],X[i,j])
        lamZ_arr[i,j] = lf.lamZ(Y[i,j],X[i,j])
        Y[i,j] = Y[i,j]/1e7

sysx = [0.59,0.3,0.35]
sysy = [3.1,2.8,2.2] 
colorarr = ['tab:red','tab:blue','tab:green']
markerarr = ['o','^','D']

fig, ax = plt.subplots(figsize=(10,10))

contT = ax.contour(X,Y,lamT_arr,cmap="magma",linestyles = 'solid',linewidths = 3, vmin = -0.45,vmax = 0.6)
contZ = ax.contour(X,Y,lamZ_arr,cmap="magma",linestyles =  'dashed',linewidths = 3,vmin = -0.45,vmax = 0.6)

plt.clabel(contT, fontsize=19, inline=1, fmt='%1.1f')
plt.clabel(contZ, fontsize=19, inline=1, fmt='%1.1f')

custom_lines = [Line2D([0], [0], color=plt.cm.magma(0.5), lw=4),
                Line2D([0], [0], color=plt.cm.magma(0.5), linestyle='--',lw=4)]


plt.xlabel(r'Z ($Z_\odot$)', fontsize = 30) 
plt.ylabel(r'T ($10^7$ K)', fontsize = 30)
plt.title(r'$\Lambda_{T}$ and $\Lambda_{Z}$', fontsize = 40)

ax.tick_params(labelsize=25)
ax.legend(custom_lines,[r'$\Lambda_T$',r'$\Lambda_Z$'],fontsize=25)

for i in range(len(markerarr)):
    ax.scatter(sysx[i],sysy[i],marker=markerarr[i],color=colorarr[i],zorder=2, s = 200)

norm= matplotlib.colors.Normalize(vmin=contT.cvalues.min(), vmax=contT.cvalues.max())
sm = plt.cm.ScalarMappable(norm=norm, cmap = contT.cmap)
sm.set_array([])
cbar = fig.colorbar(sm, ticks=contT.levels)
cbar.ax.tick_params(labelsize=20)




#A_arr = np.zeros(M,dtype=float)
##B_arr = np.zeros(N,dtype=float)
#
#for k in range(M):
#    A_arr[k] = lamT(y[k],0.5)
#
#fig = plt.figure(figsize=(8,8))
##plt.scatter(np.log10(T_tab),np.log10(T_tab),marker='x')
##print(np.diff(np.log(T_tab)))
#plt.plot(y,A_arr)
##plt.axis([1e7,5e7,-2.2*1e-23,-1*1e-23])
##plt.axis([1e7,5e7,-2.2*1e-23,2.2*1e-23])


plt.savefig('lam.png')