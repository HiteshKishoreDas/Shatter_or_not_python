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
                          label='Isobaric simulations',markerfacecolor='tab:orange', markersize=20),
                   Line2D([0], [0], marker='X', markeredgecolor='k',
                          label='Isobaric linear theory',markerfacecolor='tab:orange', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label='Isochoric simulations',markerfacecolor='tab:purple', markersize=20),
                   Line2D([0], [0], marker='d', markeredgecolor='k',
                          label='Isochoric linear theory',markerfacecolor='tab:purple', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label='Base simulation',markerfacecolor='tab:red', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{T}$',markerfacecolor='tab:blue', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{Z}$',markerfacecolor='tab:green', markersize=20)]


fig = plt.figure(figsize=(16,16))
#ax = fig.add_subplot(1,1,1)



ksim_pi = np.divide(ksim,np.pi)

n1b = 0
m1b = 4
yt1b = wi_arr[0, n1b:m1b]     # Isobaric points
ys1b = wi_arr[1, n1b:m1b] 
xt1b = np.log(ksim_pi[n1b:m1b])
xs1b = np.log(ksim_pi[n1b:m1b])

n1c = 5
m1c = 10
yt1c = wi_arr[0, n1c:m1c]    # Isochoric points
ys1c = wi_arr[1, n1c:m1c]
xt1c = np.log(ksim_pi[n1c:m1c])
xs1c = np.log(ksim_pi[n1c:m1c])

n2b = 10
m2b = 13
yt2b = wi_arr[0, n2b:m2b]   # Isobaric contour points
ys2b = wi_arr[1, n2b:m2b]
xt2b = np.log(ksim_pi[n2b:m2b])
xs2b = np.log(ksim_pi[n2b:m2b])

n2c = 13
m2c = 16
yt2c = wi_arr[0, n2c:m2c]   # Isochoric contour points
ys2c = wi_arr[1, n2c:m2c]
xt2c = np.log(ksim_pi[n2c:m2c])
xs2c = np.log(ksim_pi[n2c:m2c])

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = ax1.inset_axes([0.81, 0.2, 0.3, 0.3])
ax3 = ax1.inset_axes([0.05, 0.3, 0.3, 0.3])

width=2

ts = 1200
ls = 400
alp = 0.7

#ax.plot(k,wi)
ax1.scatter(xs1b, ys1b, s=ts,marker='o',edgecolors='k',linewidth=width,color='tab:orange',alpha=alp)
ax1.scatter(xt1b, yt1b, s=ls,marker='X',edgecolors='k',linewidth=width,zorder=3,color='tab:orange')

ax1.scatter(xs1c, ys1c, s=ts,marker='o',edgecolors='k',linewidth=width,color='tab:purple',alpha=alp)
ax1.scatter(xt1c, yt1c, s=ls,marker='d',edgecolors='k',linewidth=width,zorder=3,color='tab:purple')

ax1.scatter(xs2b, ys2b, s=ts,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax1.scatter(xt2b, yt2b, s=ls,marker='X',edgecolors='k',linewidth=width,zorder=3,color= colorarr)

ax1.scatter(xs2c, ys2c, s=ts,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax1.scatter(xt2c, yt2c, s=ls,marker='d',edgecolors='k',linewidth=width,zorder=3,color= colorarr)

ax2.scatter(xs2b, ys2b, s=ts+400,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax2.scatter(xt2b, yt2b, s=ls+200,marker='X',edgecolors='k',linewidth=width,zorder=3,color= colorarr)

ax3.scatter(xs2c, ys2c, s=ts+400,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax3.scatter(xt2c, yt2c, s=ls+200,marker='d',edgecolors='k',linewidth=width,zorder=3,color= colorarr)


#ax.set_xscale('log')
ax1.set_xlabel(r'Log$_{10}$ of k (k in x$\pi$)',fontsize=30)
ax1.set_ylabel(r'Growth rate',fontsize=30)
ax1.set_title(r'Growth Rate',fontsize = 40)
ax1.legend(handles=legend_elements,fontsize = 25, loc='upper left')
ax1.tick_params(labelsize=30)

ax2.set_xlim(2.1, 2.5)
ax2.set_ylim(0.175, 0.26)
ax2.tick_params(labelsize=20)
ax1.indicate_inset_zoom(ax2)

ax3.set_xlim(-2.6, -2.0)
ax3.set_ylim(-0.06, -0.035)
ax3.yaxis.tick_right()
ax3.tick_params(labelsize=20)
ax1.indicate_inset_zoom(ax3)

#plt.axis([-3,-2,-0.2,0])

plt.show()
fig.savefig('linear_wi.png')
plt.close(fig)
del(fig)
del(ax1)
del(ax2)
#del(ax3)