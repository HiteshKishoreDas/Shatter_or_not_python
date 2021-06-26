#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:45:57 2019

@author: Hitesh Kishore Das
"""
import numpy as np
#import tkinter
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random


tau = 0.5
a = 2.0
t0 = a*tau
b = 200.0
w = b*np.pi/tau

def phi(t):
#    return 2*np.pi*np.cos((t-t0)/tau)
    return 2*np.pi*random.uniform(-1,1)*1000000

def A(t):
    return np.exp(-1*(t-t0)*(t-t0)**2/tau**2)

def E(t):
    Ex = A(t)*np.cos(w*t)
    Ey = A(t)*np.sin(w*t + phi(t))
    return Ex,Ey

sp = 0
ep = 4
n = ep*1000000

tar = np.linspace(sp,ep,n)

plt.figure(figsize=(10,10))

Exar = np.zeros((n,),dtype = float)
Eyar = np.zeros((n,),dtype = float)

cnt = 0
for t in tar:
    Ex, Ey = E(t)
    Exar[cnt] = Ex
    Eyar[cnt] = Ey
#    print(t, A(t))
    cnt = cnt +1
    
#plt.plot(A(tarr),tarr)
plt.scatter(Exar,Eyar,s=0.25,c=tar,cmap = plt.cm.jet)
    
plt.xlabel(r'$E_x$')
plt.ylabel(r'$E_y$')
plt.grid()
cbar = plt.colorbar()
cbar.set_label(r'$t/\tau$', rotation=270,y=0.45, weight = 'bold')
#plt.show()
plt.title(r'$E_y$ vs $E_x$ for large and random $\phi(t)$ : $\omega\tau='+str(b)+r'\pi$; $t_0 = $'+str(a)+r'$\tau$ ;$\tau=$'+str(tau))
plt.savefig('/home/hitesh/Desktop/HW2.png')
plt.close()