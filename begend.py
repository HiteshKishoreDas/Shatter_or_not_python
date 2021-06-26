#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:49:15 2019

@author: hitesh
"""

import os
import sys
import numpy as np
from matplotlib.pyplot import *

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

nwdir = os.environ['PLUTO_DIR']

def begend(st,dr,step):
    data = np.loadtxt(nwdir+"TI_uniform/metallicity/"+st)
    dr = np.insert(dr,0, data[step*40][1],axis=0)
    dr = np.insert(dr,0, data[step*40][0],axis=0)
    
    dr = np.append(dr,data[step*40][2])
    dr = np.append(dr,data[step*40][3])
    
    return dr