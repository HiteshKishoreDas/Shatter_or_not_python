#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 05:53:38 2020

@author: hitesh
"""
#%%
import sympy as sm
from sympy.solvers import solve
import numpy as np

from matplotlib import pyplot as plt

w = sm.Symbol('w')

soln_list_ent = []
k_list_ent = []

soln_real_list = []
soln_imag_list = []

k_list_full = []

col_list = []
mar_list = []
siz_list = []

col_arr = ['tab:red','tab:orange','tab:blue']
mar_arr = ['D','o','X']

# LamT = 0.059  # For low T
LamT = 0.2670765527009427   # For 10^7 K

# name = 'LowT'   # For low T
name = 'HighT'  # For 10^7 K

# tcool = 0.185   # For low T  # in Myr
tcool = 252.14  # For 10^7 K

# cs = 50.342    # For low T  # in pc/Myr
cs = 0.0003468     # For 10^7 K

H = 0
gamma = 5./3.

#%%

k = 2*np.pi/750000

A = sm.I*LamT/tcool
B = -1*cs**2*k**2
D = (-1*B/(gamma*tcool)) * (H/k + sm.I*(2-LamT))

soln0 = solve(w**3 + A*w**2 + B*w + D,w)

print (soln0)

#%%

tol = 1e-10

ki = 2*np.pi/1e0   # in pc^-1

while (ki > 2*np.pi/1e12):
    
    A = sm.I*LamT/tcool
    B = -1*cs**2*ki**2
    D = (-1*B/(gamma*tcool)) * (H/ki + sm.I*(2-LamT))
    
    soln = solve(w**3 + A*w**2 + B*w + D,w)
    
#    print(soln)
    
    siz = 175
    
    for i in range(len(soln)):
        if ( np.abs(sm.re(soln[i])) < tol  ):
            soln_list_ent.append(float(sm.im(soln[i])))
            
        soln_real_list.append(float(sm.re(soln[i])))
        soln_imag_list.append(float(sm.im(soln[i])))
        
        col_list.append(col_arr[i])
        mar_list.append(mar_arr[i])
        siz_list.append(siz)
        
        siz -= 50
        
        k_list_full.append(float(ki))
        
            
    k_list_ent.append(float(ki))
    
    
    ki = ki/2.
    

k_list_ent = np.array(k_list_ent)
k_list_full = np.array(k_list_full)
soln_real_list = np.array(soln_real_list)
soln_imag_list = np.array(soln_imag_list)

thic_arr = np.zeros_like(k_list_ent) - LamT/tcool
thib_arr = np.zeros_like(k_list_ent) + (2-LamT)/(gamma*tcool)



###### For entropy mode growth rate ######
## Doesn't work for LowT #####

# plt.figure(figsize=(8,8))
# plt.xscale('log')
# plt.plot(k_list_ent,soln_list_ent)


#%%
############ Real component #################
    
plt.figure(figsize=(12,8))
plt.xscale('log')

for i in range(len(k_list_full)):
    plt.scatter(k_list_full[i],soln_real_list[i],color = col_list[i],\
                marker = mar_list[i],s = siz_list[i])
    
plt.plot(np.array(k_list_full),np.array(k_list_full)*cs)
plt.plot(np.array(k_list_full),-1*np.array(k_list_full)*cs)

plt.title('Real component: '+name,fontsize=20)
plt.xlabel(r'k (pc$^{-1}$)',fontsize=15)
plt.tick_params(labelsize=15)
#plt.xlim(1e-12,1e2)
plt.grid(True)
plt.savefig('cubic_soln/soln_real_'+name+'.png')
plt.close()

############# Imaginary component #############

plt.figure(figsize=(12,8))
plt.xscale('log')

for i in range(len(k_list_full)):
    plt.scatter(k_list_full[i],soln_imag_list[i],color = col_list[i],\
                marker = mar_list[i],s = siz_list[i])
plt.plot(k_list_ent,thic_arr,linewidth=4)
plt.plot(k_list_ent,thib_arr,linewidth=4)


plt.title('Imaginary component: '+name,fontsize=20)
plt.xlabel(r'k (pc$^{-1}$)',fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(1e-12,1e2)
plt.grid(True)
plt.savefig('cubic_soln/soln_imag_'+name+'.png')
plt.close()


########### Both components in sign_log-log #############3


plt.figure(figsize=(12,8))
plt.xscale('log')
plt.yscale('log')

for i in range(len(k_list_full)):
    plt.scatter(k_list_full[i],\
                (np.abs(soln_real_list[i])),\
                color = col_list[i], marker = mar_list[i],s = siz_list[i])
    
for i in range(len(k_list_full)):
    plt.scatter(k_list_full[i],\
                (np.abs(soln_imag_list[i])),\
                facecolors='none', edgecolors = col_list[i],\
                marker = mar_list[i],s = siz_list[i])

plt.plot(k_list_ent,np.abs(thic_arr),linewidth=2,color='tab:blue')
plt.plot(k_list_ent,np.abs(thib_arr),linewidth=2,color='tab:orange')
plt.plot(np.array(k_list_full),np.array(k_list_full)*cs,\
         linewidth=2,linestyle='dashed',color='tab:red')
#plt.plot(np.array(k_list_full),-1*np.array(k_list_full)*cs)

plt.title('Filled: Real; Unfilled: Imaginary',fontsize=20)
plt.xlabel(r'k (pc$^{-1}$)',fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(1e-12,1e2)
plt.grid(True)
plt.savefig('cubic_soln/soln_loglog_'+name+'.png')
plt.close()