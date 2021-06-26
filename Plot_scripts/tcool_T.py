#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import lamfn as lf

rho0 = 0.13
T = 3e7
X = 1.01
Z = 0.6

print(np.array(lf.cs_tcool(rho0,T,X,Z)), 'kpc')