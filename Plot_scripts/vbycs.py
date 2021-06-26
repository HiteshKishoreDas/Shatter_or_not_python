#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:13:27 2020

@author: Hitesh Kishore Das
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:16:26 2020

@author: hitesh
"""

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import workdir as wd
import lamfn as lf

wdir_script = os.getcwd()

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

gamma = 5./3.
plutodir = os.environ['PLUTO_DIR']

wdir = wd.wdir41
N = 1200

wdir = wdir + 'output/'

D = pp.pload(N,w_dir=wdir)

ul = 100 # in kpc
uv = 1.0E+8 # in cm/s
#ut = ((ul * 3.086E+21)/uv)  # in s
#ut = (ut / 3.154e+13)    # in Myr

ut = 100 # in Myr
t = 2.0 * ut  # in Myr
dt = 1.0 # in Myr


fig = plt.figure(figsize=(12,12))

cs = np.sqrt(gamma*D.prs/D.rho)

plt.yscale('log')
plt.plot(D.x1*ul,np.abs(D.vx1)/cs,linewidth = 2)
plt.plot(D.x1*ul,np.zeros(np.size(D.x1),dtype=float)+1.0)

plt.xlabel('x (in kpc)',fontsize=30)
plt.ylabel(r'$v/c_s$',fontsize=35)
plt.title(r'$v/c_s$ vs x',fontsize=40)
#plt.ylim(0,800)
#plt.xlim(2740,2780)
#plt.legend(fontsize = 25)
plt.tick_params(labelsize=25)
plt.savefig(wdir_script+'/vbycs.png')
plt.close()