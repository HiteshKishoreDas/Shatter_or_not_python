#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:15:34 2019

@author: Hitesh Kishore Das
"""

import os
import sys
from ctypes import *


os.chdir(os.environ['PLUTO_DIR']+'/TI_uniform/metallicity/Cooling_function/')

fun = cdll.LoadLibrary("libcool.so.1")