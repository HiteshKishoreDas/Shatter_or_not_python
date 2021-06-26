#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:43:23 2020

@author: Hitesh Kishore Das
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import workdir as wd
import lamfn as lf


wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5
CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

count = 0
phi_arr=['0','\dfrac{\pi}{2}','\pi']

for wdir in [wd.wdir58]:
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    #ut = ((ul * 3.086E+21)/uv)  # in s
    #ut = (ut / 3.154e+13)    # in Myr
    
    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = 1.0 # in Myr
    
    m = -0.01
    c = 0.5
    
    noch = 0.5
    
    T_cold = 10**4.1
    
#    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    z = []
    x = []
    t = []
    m = []
    
    for i in range(nlinf['nlast']+1):
        D1 = pp.pload(i,w_dir=wdir+'output/') # Loading the data into a pload object D.
        
#        ln = int(np.size(D1.x1)/2)
#        dln = 30
        
        T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
        
        dx = D1.x1[1]-D1.x1[0]
        
        xbeg = D1.x1[0]
        xend = D1.x1[np.size(D1.x1)-1]
        
        for j in range(np.size(D1.x1)):
            if (D1.x1[j]> xbeg+noch and D1.x1[j]< xend-noch):
                if (T[j] < T_cold):
                   x.append(D1.x1[j]*ul)
                   z.append(D1.tr1[j])
                   t.append(i*dt/ut*100)
                   m.append(D1.rho[j]*dx)
                   
#        plt.scatter(i*dt/ut*100,m_cold/m_tot,color='tab:blue')
#        plt.scatter(i*dt/ut,m_hot,color='tab:red')

z = np.array(z)
t = np.array(t)
x = np.array(x)
m = np.array(m)

#%%

fig, ax = plt.subplots(figsize=(15,15))

scat = ax.scatter(t,x,c=z,cmap='magma')

plt.xlabel('t (in Myr)',fontsize=35)
plt.ylabel(r'x (in kpc)',fontsize=35)
plt.title(r'x vs. t in isobaric regime',fontsize=40)
ax.tick_params(labelsize=30)

cbar = fig.colorbar(scat)
cbar.ax.tick_params(labelsize=20)
cbar.set_label(label='Metallicity',fontsize=30)
#plt.legend(fontsize=25,loc="lower right")

plt.savefig(wdir_script+'/xtz_isobaric.png')

#%%
#
#plt.figure(figsize=(15,15))
#plt.scatter(t,z,c=x,cmap='jet')
#plt.xlabel('t',fontsize=30)
#plt.ylabel(r'z',fontsize=35)
#plt.title(r'z vs. t in isobaric regime',fontsize=40)
#plt.tick_params(labelsize=25)
#plt.colorbar()
##plt.legend(fontsize=25,loc="lower right")
#
##plt.savefig(wdir_script+'/ztx_isobaric.png')
#
##%%
#
##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
##
##ax.scatter(x,m,z,c=t,cmap='jet')
##plt.xlabel('x',fontsize=30)
##plt.ylabel(r'Z',fontsize=35)
##plt.title(r'Z vs. x in isobaric regime',fontsize=40)
##plt.tick_params(labelsize=25)
##plt.colorbar()
##plt.legend(fontsize=25,loc="lower right")
#
##plt.savefig(wdir_script+'/Zxt_isobaric_3d.png')
#
#
##%%
#
#plt.figure(figsize=(15,15))
#plt.scatter(x,z,c=t,cmap='jet')
#plt.xlabel('x',fontsize=30)
#plt.ylabel(r'Z',fontsize=35)
#plt.title(r'Z vs. x in isobaric regime',fontsize=40)
#plt.tick_params(labelsize=25)
#plt.colorbar()
##plt.legend(fontsize=25,loc="lower right")
#
##plt.savefig(wdir_script+'/Zxt_isobaric.png')
#
##%%
#
#plt.figure(figsize=(15,15))
#plt.scatter(z,m,c=t,cmap='jet')
#plt.xlabel('Z',fontsize=30)
#plt.ylabel(r'm',fontsize=35)
#plt.title(r'm vs. Z in isobaric regime',fontsize=40)
#plt.tick_params(labelsize=25)
#plt.colorbar()
##plt.legend(fontsize=25,loc="lower right")
#
##plt.savefig(wdir_script+'/mZt_isobaric.png')
#
##%%
#
#plt.figure(figsize=(15,15))
#plt.scatter(x,m,c=t,cmap='jet')
#plt.xlabel('x',fontsize=30)
#plt.ylabel(r'm',fontsize=35)
#plt.title(r'm vs. x in isobaric regime',fontsize=40)
#plt.tick_params(labelsize=25)
#plt.colorbar()
##plt.legend(fontsize=25,loc="lower right")
#
##plt.savefig(wdir_script+'/mxt_isobaric.png')