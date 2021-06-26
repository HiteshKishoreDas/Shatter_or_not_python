#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:29:13 2020

@author: hitesh
"""
import numpy as np
from matplotlib import pyplot as plt

h_20000 = np.loadtxt("heating_values/heatfunc_20000.txt")
h_30000 = np.loadtxt("heating_values/heatfunc_30000.txt")
h_40000 = np.loadtxt("heating_values/heatfunc_40000.txt")
h_50000 = np.loadtxt("heating_values/heatfunc_50000.txt")

plt.figure(figsize=(10,10))

plt.plot(h_20000[:,1]*0.001/20000,h_20000[:,2],linewidth=15,color='tab:blue',label="20000")
plt.plot(h_30000[:,1]*0.001/30000,h_30000[:,2],linewidth=8,color='tab:red',label="30000")
plt.plot(h_40000[:,1]*0.001/40000,h_40000[:,2],linewidth=3,linestyle='dashed',color='tab:orange',label="40000")
plt.plot(h_50000[:,1]*0.001/50000,h_50000[:,2],linewidth=5,linestyle='dotted',color='tab:green',label="50000")

plt.xlabel("x (code units)",fontsize=15)
plt.ylabel("Heating rate (code units)",fontsize=15)
plt.legend(fontsize=20)

plt.savefig("heat_rate_comparison.png")