#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:38:50 2019

@author: hitesh
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Solution for memory leak in savefig
import matplotlib.pyplot as plt
import begend as bg


os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

wdir = plutodir+ '/TI_uniform/metallicity/output/'

wi_arr = np.zeros((2,7),dtype = 'float')
wi_arr = np.load("wi_arr.npy")

ksim = np.array([0.1*np.pi,10.*np.pi,50.*np.pi,100.*np.pi,10.*np.pi,10.*np.pi,10.*np.pi])
msim = np.array([-0.05,-0.05,-0.05,-0.05,-0.025,-0.05,-0.05])
labelarr= ["m_-0.05","m_-0.05","m_-0.05","m_-0.05","m_-0.025","m_-0.05_lowT","m_-0.05"]
colorarr = ["g","g","g","g","r","b","g"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

#ax.plot(k,wi)
ax.scatter(ksim,wi_arr[1,:],s=30,marker='o',color=colorarr,label=labelarr )
ax.scatter(ksim,wi_arr[0,:],s=30,marker='x',color=colorarr)
ax.set_xlabel(r'k')
ax.set_ylabel(r'Growth rate')
ax.legend()
ax.grid()
ax.set_xlim([-10.0, 110.0*np.pi])
ax.set_ylim([0.0, 1.5])
#ax.set_title(st + ': ' + str(i*dt) + ' Myr')
fig.savefig(wdir+'Plots/linear_wi.png')