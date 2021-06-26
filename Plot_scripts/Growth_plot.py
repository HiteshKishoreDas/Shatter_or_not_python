#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:38:50 2019

@author: hitesh
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

wdir_script = os.getcwd()

filn = 16     # Number of points

wi_arr = np.zeros((3,filn),dtype = 'float')
wi_arr = np.load("wi_arr_fit.npy")

ksim = wi_arr[2,:]

#msim = np.array([-0.05,-0.05,-0.05,-0.05,-0.025,-0.05,-0.05])

#labelarr= ["m_-0.05","m_-0.05","m_-0.05","m_-0.05","m_-0.025","m_-0.05_lowT","m_-0.05"]

colorarr = ['tab:red','tab:blue','tab:green',]

legend_elements = [Line2D([0], [0], marker='o', markeredgecolor='k',
                          label='Simulations',markerfacecolor='tab:orange', markersize=20),
                   Line2D([0], [0], marker='X', markeredgecolor='k',
                          label='Linear Theory',markerfacecolor='tab:orange', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label='Base simulation',markerfacecolor='tab:red', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{T}$',markerfacecolor='tab:blue', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{Z}$',markerfacecolor='tab:green', markersize=20)]


fig = plt.figure(figsize=(12,12))
#ax = fig.add_subplot(1,1,1)

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.65, 0.3, 0.2, 0.2])
ax3 = fig.add_axes([0.2, 0.25, 0.2, 0.2])

ax2.set_xlim(2.25, 2.35)
ax2.set_ylim(0.175, 0.26)

ax3.set_xlim(-2.35, -2.25)
ax3.set_ylim(-0.06, -0.025)
ax3.yaxis.tick_right()

yt1b = wi_arr[0,0:5] #np.log(np.abs(np.power(wi_arr[0,:],1)))
ys1b = wi_arr[1,0:5] #np.log(np.abs(np.power(wi_arr[1,:],1)))
xt1b = np.log(np.divide(ksim[0:5],np.pi))
xs1b = np.log(np.divide(ksim[0:5],np.pi))

yt1c = wi_arr[0,5:10] #np.log(np.abs(np.power(wi_arr[0,:],1)))
ys1c = wi_arr[1,5:10] #np.log(np.abs(np.power(wi_arr[1,:],1)))
xt1c = np.log(np.divide(ksim[5:10],np.pi))
xs1c = np.log(np.divide(ksim[5:10],np.pi))

yt2b = wi_arr[0,10:13] #np.log(np.abs(np.power(wi_arr[0,:],1)))
ys2b = wi_arr[1,10:13] #np.log(np.abs(np.power(wi_arr[1,:],1)))
xt2b = np.log(np.divide(ksim[10:13],np.pi))
xs2b = np.log(np.divide(ksim[10:13],np.pi))

yt2c = wi_arr[0,13:16] #np.log(np.abs(np.power(wi_arr[0,:],1)))
ys2c = wi_arr[1,13:16] #np.log(np.abs(np.power(wi_arr[1,:],1)))
xt2c = np.log(np.divide(ksim[13:16],np.pi))
xs2c = np.log(np.divide(ksim[13:16],np.pi))


#ax.plot(k,wi)
ax1.scatter(xs1b, ys1b, s=300,marker='o',edgecolors='k',color='tab:orange',alpha=0.8)
ax1.scatter(xt1b, yt1b, s=400,marker='X',edgecolors='k',zorder=-1,color='tab:orange')

ax1.scatter(xs1c, ys1c, s=300,marker='o',edgecolors='k',color='tab:green',alpha=0.8)
ax1.scatter(xt1c, yt1c, s=400,marker='d',edgecolors='k',zorder=-1,color='tab:green')

ax2.scatter(xs2b, ys2b, s=300,marker='o',edgecolors='k',color=colorarr, alpha=0.8)
ax2.scatter(xt2b, yt2b, s=400,marker='X',edgecolors='k',zorder=-1,color= colorarr)

ax3.scatter(xs2c, ys2c, s=300,marker='o',edgecolors='k',color=colorarr, alpha=0.8)
ax3.scatter(xt2c, yt2c, s=400,marker='d',edgecolors='k',zorder=-1,color= colorarr)


#ax.set_xscale('log')
ax1.set_xlabel(r'Log of k (k in x$\pi$)',fontsize=30)
ax1.set_ylabel(r'Growth rate',fontsize=30)
ax1.set_title(r'Growth Rate',fontsize = 40)
ax1.legend(handles=legend_elements,fontsize = 20, loc='upper left')
ax1.tick_params(labelsize=25)

#plt.axis([-3,-2,-0.2,0])

plt.show()
fig.savefig('linear_wi.png')
plt.close(fig)
del(fig)
del(ax1)
del(ax2)
del(ax3)