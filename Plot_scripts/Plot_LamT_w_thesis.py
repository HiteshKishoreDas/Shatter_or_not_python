#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:16:47 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 03:26:52 2020

@author: hitesh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:48:14 2020

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

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
ut = ((ul * 3.086E+21)/uv)  # in s
ut = (ut / 3.154e+13)    # in Myr
#    ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = ut*0.01 # in Myr

labelsize =30
ticksize  =25
titlesize =30 
offsetsize=25
legendsize=25
textsize  =25

left  = 0.1  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.4   # the amount of width reserved for blank space between subplots
hspace = 0.2   # the amount of height reserved for white space between subplots

box_size=4.0

def plot_lamT (ax,lamT_arr,rho,x1,t,tc_min,flag=True):
    axp = ax.twinx()
    ax.set_zorder(10)
    ax.patch.set_visible(False)
    
    ax.plot(x1,lamT_arr,label='lamT',c='tab:red',linewidth=3)
    if flag:
        axp.plot(x1,rho,label='Density',c='tab:blue',linewidth=3,zorder=2)
    else:
        axp.plot(x1,rho,label='Density',c='tab:blue',linewidth=0.5,zorder=2)
    
    ax.plot(x1,arr_0,c='k',linestyle='dashed',linewidth=3)
    ax.plot(x1,arr_2,c='k',linestyle='dashed',linewidth=3)

    if flag:
        ax.text(5300, 2.5, 'Both stable', ha='right', fontsize=textsize)
    ax.text(5300, 1.0, 'IC stable, IB unstable', ha='right', fontsize=textsize)
    ax.text(5300, -0.5, 'Both unstable', ha='right', fontsize=textsize)

    ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    axp.ticklabel_format(axis='y', style='sci', scilimits=(0,0))

    text1 = ax.yaxis.get_offset_text()
    text1.set_size(offsetsize)
    text2 = axp.yaxis.get_offset_text()
    text2.set_size(offsetsize)

    ax.tick_params(labelsize=ticksize)
    axp.tick_params(labelsize=ticksize)
    
    ax.set_xlabel(r'x (in kpc)',fontsize=labelsize)
    ax.set_ylabel(r'$\Lambda_T$',fontsize=labelsize)
    axp.set_ylabel(r'Density (amu cm$^{-3}$)',fontsize=labelsize)
    ax.legend(loc='upper left',fontsize=legendsize)
    axp.legend(loc='upper right',fontsize=legendsize)
    ax.set_title('At t = ' + str(np.round(t*dt/tc_min,2)) + r' t$_{\rm cool}$',fontsize=titlesize,y=1.05)
    
    return ax,axp
    

def lamT_rho_array(wdir,ln,dln,t):
    
    D1 = pp.pload(t,w_dir=wdir+'output/')
    T  = D1.prs/D1.rho*KELVIN*lf.MMWt_mu(D1.tr1)
    
    lamT_arr = lf.lamT(T,D1.tr1)
    
    lamT_arr = lamT_arr[ln-dln:ln+dln]
    x1 = D1.x1[ln-dln:ln+dln]*ul
    rho = D1.rho[ln-dln:ln+dln]
    
    del(D1)
    return lamT_arr,rho,x1

t_list = [6,10,30]

wdir = wd.wdir74

nlinf = pp.nlast_info(w_dir=wdir+'output/')
D0 = pp.pload(0,w_dir=wdir+'output/')

lam0 =  np.zeros(np.size(D0.x1),dtype=float)

n_H0 = D0.rho*UNIT_DENSITY/(lf.MMWt_muH(D0.tr1)*CONST_amu)
T0 = D0.prs/D0.rho*KELVIN*lf.MMWt_mu(D0.tr1)
for i in range(np.size(D0.x1)):
    lam0[i] = lf.lam(T0[i],D0.tr1[i])
q0 = n_H0*n_H0*lam0/unit_q
tc0 = D0.prs/(q0*(gamma - 1))
tc_min = np.min(tc0)*ut



ln = int(np.size(D0.x1)/2) #+ 250 + 265
dln = 3000

arr_2 = np.zeros(np.size(D0.x1[ln-dln:ln+dln]),dtype=float) + 2.
arr_0 = np.zeros(np.size(D0.x1[ln-dln:ln+dln]),dtype=float)

cnt = -1

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(25,10))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

output = lamT_rho_array(wdir,ln,dln,t_list[0])
ax1,ax4 = plot_lamT (ax1,output[0],output[1],output[2],t_list[0],tc_min,False)

output = lamT_rho_array(wdir,ln,dln,t_list[1])
ax2,ax5 = plot_lamT (ax2,output[0],output[1],output[2],t_list[1],tc_min)

#output = lamT_rho_array(wdir,ln,dln,t_list[2])
#ax3,ax6 = plot_lamT (ax3,output[0],output[1],output[2],t_list[2])

plt.savefig(wdir_script+'/cold_mass/lamT_rho.png')
plt.show()
plt.close()