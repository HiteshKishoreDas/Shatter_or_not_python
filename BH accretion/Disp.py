#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:14:23 2019

@author: hitesh
"""
import numpy as np
import Velo

def disp(m_arr,F_arr,dt):
#    N = np.size(m_arr)
    d_arr = np.zeros(np.size(F_arr),dtype=float)
    
    v_arr = Velo.velo(m_arr,F_arr,dt)
    
    d_arr[0,:] = np.divide(v_arr[0,:],m_arr) * dt
    d_arr[1,:] = np.divide(v_arr[1,:],m_arr) * dt
    
    return d_arr