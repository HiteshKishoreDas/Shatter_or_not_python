#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 05:53:38 2020

@author: hitesh
"""
#%%
import sympy as sm
from sympy.solvers import solve
import numpy as np
import lamfn as lf

from matplotlib import pyplot as plt

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ut = UNIT_LENGTH/UNIT_VELOCITY
ut = ut/3.154e7
ut = ut/1e6

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.


w = sm.Symbol('w')

soln_real_list = []
soln_imag_list = []
T_list = []

asib_list = []
asic_list = []

col_list = []
mar_list = []
siz_list = []

siz_arr = [150,100,50]
col_arr = ['tab:red','tab:orange','tab:blue']
mar_arr = ['D','o','X']


Z = 0.6
X = 1.01
rho0 = 0.0620

lamb = 100

k = 2*np.pi/lamb

start_exp = 4.1
stop_exp = 7

T_arr = np.logspace(start_exp,stop_exp,num=200)

for T in T_arr:
    # T = 1.78e5

    print(T)

    p0 = rho0*T/(KELVIN*lf.MMWt_mu(Z,X))
    n_H = rho0*UNIT_DENSITY/(lf.MMWt_muH(Z,X)*CONST_amu)

    q0 = n_H*n_H*lf.lam(T,Z)/unit_q

    tcool = p0/(q0*(gamma - 1)) * ut

    LamT = lf.lamT(T,Z)

    cs = np.sqrt(p0/rho0) * UNIT_VELOCITY / 9.785e4  # in pc/Myr

    # print(tcool)
    # print(LamT)
    # print(cs)

    # LamT = 0.059  # For low T
    # LamT = -0.2   # For 10^7 K

    # name = 'LowT'   # For low T
    # name = 'HighT'  # For 10^7 K

    # tcool = 0.185   # For low T  # in Myr
    #tcool = 50.  # For 10^7 K

    # cs = 50.342    # For low T  # in pc/Myr
    #cs = 300     # For 10^7 K

    H = 0
    gamma = 5./3.

    A = sm.I*LamT/tcool
    B = -1*cs**2*k**2
    D = (-1*B/(gamma*tcool)) * (H/k + sm.I*(2-LamT))

    soln_arr = solve(w**3 + A*w**2 + B*w + D,w)

    for i,soln in enumerate(soln_arr):

        T_list.append(T)
        soln_real_list.append(sm.re(soln))
        soln_imag_list.append(sm.im(soln))

        col_list.append(col_arr[i])
        mar_list.append(mar_arr[i])
        siz_list.append(siz_arr[i])

    asib_list.append((2-LamT)/(gamma*tcool))
    asic_list.append(-LamT/tcool)

#%%

left   = 0.15   # the left side of the subplots of the figure
right  = 0.97   # the right side of the subplots of the figure
bottom = 0.09   # the bottom of the subplots of the figure
top    = 0.97   # the top of the subplots of the figure
wspace = 0.25   # the amount of width reserved for blank space between subplots
hspace = 0.15   # the amount of height reserved for white space between subplots

axissize = 25
ticksize = 20
titlesize = 20 
legendsize = 20
offsetsize = ticksize
plotline_width = 3
markline_width = 1.5

###### Real components ######

fig,ax = plt.subplots(2,1,figsize=(10,10))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

ax[0].axvspan(3.7e4, 4.8e4, alpha=0.3, color='lightgray')
ax[0].axvspan(7e4, 8e4, alpha=0.3, color='lightgray')
ax[0].axvspan(1.6e4, 1.73e4, alpha=0.3, color='lightgray')

ax[1].axvspan(3.7e4, 4.8e4, alpha=0.3, color='lightgray')
ax[1].axvspan(7e4, 8e4, alpha=0.3, color='lightgray')
ax[1].axvspan(1.6e4, 1.73e4, alpha=0.3, color='lightgray')

ax[0].set_xscale('log')
ax[0].set_yscale('symlog')

for i in range(len(T_list)):
    ax[0].scatter(T_list[i],soln_real_list[i], facecolors='none', edgecolors=col_list[i],\
                linewidth=markline_width, marker = mar_list[i],s = siz_list[i])

# ax[0].set_title('Real component: '+str(lamb)+'pc',fontsize=titlesize)
# ax[0].set_xlabel(r'T (K)',fontsize=axissize)
ax[0].set_ylabel(r'Re($\omega$) (Myr$^{-1}$)',fontsize=axissize)
ax[0].tick_params(labelsize=ticksize)

ax[0].set_xlim(10**start_exp,10**stop_exp)
ax[0].grid(True)
# plt.savefig('cubic_soln/wvT/soln_real_T_'+str(lamb)+'pc.png')
# plt.close()

###### Imaginary components ######

# plt.figure(figsize=(15,8))
ax[1].set_xscale('log')
ax[1].set_yscale('symlog')

for i in range(len(T_list)):
    ax[1].scatter(T_list[i],soln_imag_list[i],facecolors='none', edgecolors=col_list[i],\
                linewidth=markline_width, marker = mar_list[i],s = siz_list[i])

ax[1].plot(np.array(T_list), np.zeros_like(np.array(T_list)), linestyle='dashed')

ax[1].plot(T_arr,np.array(asic_list),color='k',linestyle='dashed',\
    label='Asymptotic isochoric',linewidth=plotline_width)
ax[1].plot(T_arr,np.array(asib_list),color='tab:green',linestyle='dotted',\
    label='Asymptotic isobaric',linewidth=plotline_width)

# ax[1].set_title('Imaginary component: '+str(lamb)+'pc',fontsize=titlesize)
ax[1].set_xlabel(r'T (K)',fontsize=axissize)
ax[1].set_ylabel(r'Im($\omega$) (Myr$^{-1}$)',fontsize=axissize)
ax[1].tick_params(labelsize=ticksize)
ax[1].legend(fontsize=legendsize,frameon=False)

ax[1].set_xlim(10**start_exp,10**stop_exp)
ax[1].grid(True)

plt.savefig('cubic_soln/wvT/soln_T_'+str(lamb)+'pc.png')
# plt.close()
plt.show()


# %%

# %%
