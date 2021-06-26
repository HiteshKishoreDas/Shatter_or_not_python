#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:30:57 2020

@author: hitesh
"""
import numpy as np
import Growth_fit as grf
import workdir as wd
from matplotlib import pyplot as plt

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr

#    ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = ut#1.0 # in Myr ############################

wdir_arr = [wd.wdir93,wd.wdir94,wd.wdir95,wd.wdir96]
k_arr = np.array([160000,80000,40000,320000])*np.pi/ul

wdir_arr2 = [wd.wdir97,wd.wdir98]
k_arr2 = np.array([160000,320000])*np.pi/ul

n = np.size(wdir_arr)
n2 = np.size(wdir_arr2)

w_arr = np.zeros((2,n))
w_arr2 = np.zeros((2,n2))

for i in range(n):
    wdir = wdir_arr[i]
    
    wi_avg,v = grf.growth_fit(wdir,0,50)
    
    w_arr[0,i] = wi_avg
    w_arr[1,i] = v
    
for i in range(n2):
    wdir = wdir_arr2[i]
    
    wi_avg,v = grf.growth_fit(wdir,0,50)
    
    w_arr2[0,i] = wi_avg
    w_arr2[1,i] = v
    
#%%

ticklabel_size = 25.
axislabel_size = 25.
legend_size = 20.

fig = plt.figure(figsize=(10,12))

ax1 = fig.add_axes([0.2, 0.1, 0.75, 0.4])
ax2 = fig.add_axes([0.2, 0.5, 0.75, 0.4])


k0 = np.logspace(2.5,4.5,num=100)
zer = np.zeros_like(k0)
    
ax2.set_xscale('log')

ax2.scatter(k_arr,w_arr[0,:],marker='o',c='r',s=600,label='Linear theory')
#plt.scatter(k_arr2,w_arr2[0,:],marker='<',c='r',s=200,label='Theoretical')
ax2.scatter(k_arr,w_arr[1,:],marker='X',c='b',s=400,label='Original Simulations')
ax2.scatter(k_arr2,w_arr2[1,:],marker='D',c='b',s=300,label='Simulations with\ndouble resolution')
ax2.plot(k0,zer,linestyle='dashed')

#ax2.set_xlabel(r'k (kpc$^{-1}$)',fontsize=20)
ax2.set_ylabel(r'Growth rate (Myr$^{-1}$)',fontsize=axislabel_size)
#plt.title('Growth rate for high k',fontsize=25)
ax2.tick_params(labelsize=ticklabel_size)
ax2.legend(fontsize=legend_size,loc='lower left')
ax2.set_xlim(10**2.5,10**4.5)

    
ax1.set_xscale('log')
ax1.set_yscale('log')

devw = np.abs(w_arr[1,:]-w_arr[0,:])
devw2 = np.abs(w_arr2[1,:]-w_arr2[0,:])

v_fit = np.polyfit(np.log10(k_arr),np.log10(devw),1)
print(v_fit)
fit_line = k0**v_fit[0] * 10.**v_fit[1]

ax1.plot(k0,fit_line,linestyle='dashed',label=r'Linear fit in log-log:$ak^{b}$'\
         +'\n'+'b='+str("%.2f" % v_fit[0]))
ax1.scatter(k_arr,devw,marker='X',c='b',s=400)#,label='Original simulations')
ax1.scatter(k_arr2,devw2,marker='D',c='b',s=300)#,label='Simulations with\ndouble resolution')

ax1.set_xlabel(r'k (kpc$^{-1}$)',fontsize=axislabel_size)
ax1.set_ylabel(r'Growth rate deviation (Myr$^{-1}$)',fontsize=axislabel_size)
#plt.title('Deviation in growth rate for high k',fontsize=25)
ax1.tick_params(labelsize=ticklabel_size)
ax1.set_xlim(10**2.5,10**4.5)
ax1.legend(fontsize=legend_size,loc='lower right')


plt.savefig(grf.wdir_script+'/High_k_growth.png')
#plt.savefig(grf.wdir_script+'/High_k_growth_deviation.png')