#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 05:53:38 2020

@author: hitesh
"""

import sympy as sm
from sympy.solvers import solve
import numpy as np
import lamfn as lf

CONST_amu = 1.66053886e-24
UNIT_DENSITY = 1.66053886e-24
UNIT_VELOCITY = 1.e8
UNIT_LENGTH = 3.0856775807e18  * 1.e5

CONST_kB = 1.3806505e-16
KELVIN = UNIT_VELOCITY*UNIT_VELOCITY*CONST_amu/CONST_kB

ut = UNIT_LENGTH/UNIT_VELOCITY
ut = ut/3.154e7
ut = ut/1e6

unit_q = UNIT_DENSITY*np.power(UNIT_VELOCITY,3.0)
unit_q = unit_q / UNIT_LENGTH
gamma = 5./3.

w = sm.Symbol('w')


Z = 0.4
X = 1.01
rho0 = 0.0620

def disp_solve(k,T):
    # print(k,T)

    p0 = rho0*T/(KELVIN*lf.MMWt_mu(Z,X))
    n_H = rho0*UNIT_DENSITY/(lf.MMWt_muH(Z,X)*CONST_amu)

    q0 = n_H*n_H*lf.lam(T,Z)/unit_q

    tcool = p0/(q0*(gamma - 1)) * ut

    LamT = lf.lamT(T,Z)

    # print((-LamT)/(tcool)

    cs = np.sqrt(p0/rho0) * UNIT_VELOCITY / 9.785e7  # in kpc/Myr

    print(tcool,cs,LamT)

    H = 0

    A = sm.I*LamT/tcool
    B = -1*cs**2*k**2
    D = (-1*B/(gamma*tcool)) * (H/k + sm.I*(2-LamT))

    soln_arr = solve(w**3 + A*w**2 + B*w + D,w)

    return soln_arr