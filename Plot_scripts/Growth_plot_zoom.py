#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:38:50 2019

@author: hitesh
"""
#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import disp_soln as ds
import sympy as sm

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

#%%
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
                          label='Fiducial simulation',markerfacecolor='tab:red', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{T}$ as fiducial',markerfacecolor='tab:blue', markersize=20),
                   Line2D([0], [0], marker='o', markeredgecolor='k',
                          label=r'Same $\Lambda_{Z}$ as fiducial',markerfacecolor='tab:green', markersize=20)]


fig = plt.figure(figsize=(16,16))
#ax = fig.add_subplot(1,1,1)



ksim_kpc = ksim*0.01

n1b = 0
m1b = 4
yt1b = wi_arr[0, n1b:m1b]     # Isobaric points
ys1b = wi_arr[1, n1b:m1b] 
xt1b = np.log10(ksim_kpc[n1b:m1b])
xs1b = np.log10(ksim_kpc[n1b:m1b])

n1c = 5
m1c = 10
yt1c = wi_arr[0, n1c:m1c]    # Isochoric points
ys1c = wi_arr[1, n1c:m1c]
xt1c = np.log10(ksim_kpc[n1c:m1c])
xs1c = np.log10(ksim_kpc[n1c:m1c])

n2b = 10
m2b = 13
yt2b = wi_arr[0, n2b:m2b]   # Isobaric contour points
ys2b = wi_arr[1, n2b:m2b]
xt2b = np.log10(ksim_kpc[n2b:m2b])
xs2b = np.log10(ksim_kpc[n2b:m2b])

n2c = 13
m2c = 16
yt2c = wi_arr[0, n2c:m2c]   # Isochoric contour points
ys2c = wi_arr[1, n2c:m2c]
xt2c = np.log10(ksim_kpc[n2c:m2c])
xs2c = np.log10(ksim_kpc[n2c:m2c])

ax1 = fig.add_axes([0.15, 0.1, 0.8, 0.8])
ax2 = ax1.inset_axes([0.68, 0.05, 0.3, 0.3])
ax3 = ax1.inset_axes([0.04, 0.3, 0.3, 0.3])

width=2

ss = 1200
ss_arr = [1800,1200,1600]
ts = 400
alp = 0.7


#ax.plot(k,wi)
ax1.scatter(xs1b, ys1b, s=ss,marker='o',edgecolors='k',linewidth=width,color='tab:orange',alpha=alp)
ax1.scatter(xt1b, yt1b, s=ts,marker='X',edgecolors='k',linewidth=width,zorder=3,color='tab:orange')

ax1.scatter(xs1c, ys1c, s=ss,marker='o',edgecolors='k',linewidth=width,color='tab:purple',alpha=alp)
ax1.scatter(xt1c, yt1c, s=ts,marker='d',edgecolors='k',linewidth=width,zorder=3,color='tab:purple')

ax1.scatter(xs2b, ys2b, s=ss,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax1.scatter(xt2b, yt2b, s=ts,marker='X',edgecolors='k',linewidth=width,zorder=3,color= colorarr)
#
ax1.scatter(xs2c, ys2c, s=ss,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax1.scatter(xt2c, yt2c, s=ts,marker='d',edgecolors='k',linewidth=width,zorder=3,color= colorarr)

ax2.scatter(xs2b, ys2b, s=ss_arr,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax2.scatter(xt2b, yt2b, s=ts+200,marker='X',edgecolors='k',linewidth=width,zorder=3,color= colorarr)
#
ax3.scatter(xs2c, ys2c, s=ss+400,marker='o',edgecolors='k',linewidth=width,color=colorarr,alpha=alp)
ax3.scatter(xt2c, yt2c, s=ts+200,marker='d',edgecolors='k',linewidth=width,zorder=3,color= colorarr)


ax1.set_ylim(-0.002, 0.008)

#ax.set_xscale('log')
ax1.set_xlabel(r'Log$_{10}$k (kpc$^{-1}$)',fontsize=30)
ax1.set_ylabel(r'Growth rate (Myr$^{-1}$)',fontsize=30)
#ax1.set_title(r'Growth Rate',fontsize = 40)
ax1.legend(handles=legend_elements,fontsize = 25, loc='upper left')
ax1.tick_params(labelsize=30)

ax2.set_xlim(-0.6, -0.4)
ax2.set_ylim(0.0018, 0.0028)
ax2.tick_params(labelsize=20)
ax1.indicate_inset_zoom(ax2)
mark_inset(ax1, ax2, loc1=1, loc2=2, fc="none", ec="0.5",lw=3)

ax3.set_xlim(-2.65, -2.35)
ax3.set_ylim(-0.00065, -0.00035)
ax3.yaxis.tick_right()
ax3.tick_params(labelsize=20)
ax1.indicate_inset_zoom(ax3)
mark_inset(ax1, ax3, loc1=3, loc2=4, fc="none", ec="0.5",lw=3)

#plt.axis([-3,-2,-0.2,0])


# plt.show()
fig.savefig('linear_wi.png')
plt.close(fig)
del(fig)
del(ax1)
del(ax2)
#del(ax3)


#%%
# plt.figure(figsize=(8,8))
# ka = np.min(ksim_kpc)
# kb = np.max(ksim_kpc)

# kth_arr = np.logspace(np.log10(ka)-1,np.log10(kb),num=200)
# T = 8.76e6

# w_th = []
# tol = 1e-10

# for i,kth in enumerate(kth_arr):
#        soln_arr = ds.disp_solve(kth,T)
#        for soln in soln_arr:
#               if (np.abs(sm.re(soln)) < tol ):
#                      w_th.append(sm.im(soln))
       
#        # print(i)

# #%%
# plt.plot(np.log10(kth_arr),np.array(w_th))
# plt.show()