#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:19:24 2019

@author: hitesh
"""

import numpy as np

def velo(m_arr,F_arr,dt):
#    N = np.size(m_arr)
    v_arr = np.zeros(np.size(F_arr),dtype=float)
    
    v_arr[0,:] = np.divide(F_arr[0,:],m_arr) * dt
    v_arr[1,:] = np.divide(F_arr[1,:],m_arr) * dt
    
    return v_arr