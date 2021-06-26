#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 03:56:08 2020

@author: hitesh
"""

import numpy as np
from matplotlib import pyplot as plt

lamZ = 0.2
lamT = 0.3
Z0 = 0.3
rhomp = 0.06
ni0 = 0.01
ne0 = 0.03
n0 = ni0 + ne0

a = np.logspace(-2,3,num=100)

alpha = lamZ/Z0 + rhomp*(3*(a+5)/(16*(a+1)*ni0) + 1/(2*(a+1)*ne0))

mu_p = alpha + rhomp*(3*a+23)*lamT/(16*(a+1)*n0) 

mu_p = 1/mu_p

plt.figure(figsize=(15,15))
plt.xscale('log')
plt.tick_params(labelsize=20)
plt.xlabel('a',fontsize=25)
plt.ylabel(r'$\mu^\prime$',fontsize=25)
plt.title(r'$\mu^\prime$ vs a',fontsize=30)
plt.plot(a,mu_p)
plt.savefig('muprime.png')