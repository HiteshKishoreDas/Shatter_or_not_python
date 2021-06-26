#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:21:36 2019

@author: Hitesh Kishore Das
"""
import os
wdir_script = os.getcwd()
import sys
import numpy as np
import matplotlib.pyplot as plt
import workdir as wd
import matplotlib.ticker as mticker

os.chdir(os.environ['PYPLUTO'])
import pyPLUTO as pp

plutodir = os.environ['PLUTO_DIR']

ticklabel_size = 35.
axislabel_size = 35.
legend_size = 30.

col_bg = 'tab:red'
col = 'tab:blue'

def same(X,Y):
    
    Y_arr = np.zeros(np.size(X),dtype=float)
    
    for i in range(np.size(X)):
        Y_arr[i] = Y
    return Y_arr

for wdir in [wd.wdir65]:
    
    nlinf = pp.nlast_info(w_dir=wdir+'output/')
    
    ul = 100 # in kpc
    uv = 1.0E+8 # in cm/s
    ut = ((ul * 3.086E+21)/uv)  # in s
    ut = (ut / 3.154e+13)    # in Myr
    
#    ut = 100 # in Myr
    t = 2.0 * ut  # in Myr
    dt = ut*0.01 # in Myr
    
    m_z = -0.05
    c_z = 0.5
    m_x = 0.0025
    c_x = 1.01

    N = 300
    M = 0
    D0 = pp.pload(0,w_dir=wdir+'output/')
    
    fig = plt.figure(figsize=(20,22))
    
#    text1 = ax3.yaxis.get_offset_text()
#    offset3 = text1._text
#    text1.set_size(ticklabel_size)
#    ax3.yaxis.set_offset_position("bottom")
#    text1.set_position((0.1,0.1))
   
    rho0 = (np.max(D0.rho)+np.min(D0.rho))/2.0
    p0 = (np.max(D0.prs)+np.min(D0.prs))/2.0
    
    ax1 = fig.add_axes([0.2, 0.1-0.05, 0.75, 0.2])
    ax2 = fig.add_axes([0.2, 0.325-0.05, 0.75, 0.2])#,sharex='True')
    ax5 = fig.add_axes([0.2, 0.55-0.05, 0.75, 0.05+0.02])#,sharex='True')
    ax6 = fig.add_axes([0.2, 0.6-0.05+0.02, 0.75, 0.15])#,sharex='True')
    ax3 = fig.add_axes([0.2, 0.775-0.05+0.02, 0.75, 0.05+0.02])#,sharex='True')
    ax4 = fig.add_axes([0.2, 0.825-0.05+0.02+0.02, 0.75, 0.15])#,sharex='True')
#    ax.set_yscale('log')

    
    width = 6
    offset_n = 50
    
    n = int(np.size(D0.x1)/2) + offset_n
    
    ax1.plot(D0.x1*ul, same(D0.x1,1),linewidth=width,c=col_bg)
    ax1.plot(D0.x1*ul,D0.rho/rho0,linestyle='--',linewidth=width,c=col)
    ax1.scatter(D0.x1[n]*ul, D0.rho[n]/rho0,marker='o',zorder=3,s=300,c='tab:green')
    
    ax2.plot(D0.x1*ul, same(D0.x1,1),linewidth=width,c=col_bg)
    ax2.plot(D0.x1*ul,D0.prs/p0,linestyle='--',linewidth=width,c=col)
    ax2.scatter(D0.x1[n]*ul, D0.prs[n]/p0,marker='o',zorder=3,s=300,c='tab:green')

    ax3.plot(D0.x1*ul, same(D0.x1,0.0),linewidth=width,c=col_bg)
    ax3.plot(D0.x1*ul, D0.tr1 - (m_z*D0.x1+c_z),linestyle='--',linewidth=width,c=col)    
    ax3.scatter(D0.x1[n]*ul, D0.tr1[n] - (m_z*D0.x1[n]+c_z),marker='o',zorder=3,s=300,c='tab:green')
    
    ax4.plot(D0.x1*ul, D0.tr1,label = 'Background',linewidth=width,c=col_bg)
    ax4.plot(D0.x1*ul, m_z*D0.x1+c_z,linestyle='--',label = 'With perturbation',linewidth=width+2,c=col)
    ax4.scatter(D0.x1[n]*ul, D0.tr1[n],marker='o',zorder=3,s=300,c='tab:green')
    
    ax5.plot(D0.x1*ul, same(D0.x1,0.0),linewidth=width,c=col_bg)
    ax5.plot(D0.x1*ul, D0.tr2 - (m_x*D0.x1+c_x),linestyle='--',linewidth=width,c=col)    
    ax5.scatter(D0.x1[n]*ul, D0.tr2[n] - (m_x*D0.x1[n]+c_x),marker='o',zorder=3,s=300,c='tab:green')
    
    ax6.plot(D0.x1*ul, D0.tr2,label = 'Background',linewidth=width,c=col_bg)
    ax6.plot(D0.x1*ul, m_x*D0.x1+c_x,linestyle='--',label = 'With perturbation',linewidth=width+2,c=col)
    ax6.scatter(D0.x1[n]*ul, D0.tr2[n],marker='o',zorder=3,s=300,c='tab:green')
    
    ax1.set_xlabel(r'x (kpc)',fontsize=axislabel_size)
    
    ax1.set_ylabel(r'$\rho/\rho_0$',fontsize=axislabel_size)
    ax2.set_ylabel(r'$p/p_0$',fontsize=axislabel_size)
    ax3.set_ylabel(r'$\delta Z$',fontsize=axislabel_size)
    ax4.set_ylabel(r'$Z$ ($Z_\odot$)',fontsize=axislabel_size)
    ax5.set_ylabel(r'$\delta X$',fontsize=axislabel_size)
    ax6.set_ylabel(r'$X$ ($X_\odot$)',fontsize=axislabel_size)
    
    ax4.axes.get_xaxis().set_ticks([])
    ax6.axes.get_xaxis().set_ticks([])
    
    ax1.tick_params(labelsize=ticklabel_size)
    ax2.tick_params(labelsize=ticklabel_size)
    ax3.tick_params(labelsize=ticklabel_size-5)
    ax4.tick_params(labelsize=ticklabel_size)
    ax5.tick_params(labelsize=ticklabel_size-5)
    ax6.tick_params(labelsize=ticklabel_size)
    
    ax1.set_xlim(0.,400.)
    ax2.set_xlim(0.,400.)
    ax3.set_xlim(0.,400.)
    ax4.set_xlim(0.,400.)
    ax5.set_xlim(0.,400.)
    ax6.set_xlim(0.,400.)
    
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
#    ax3.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
#    ax5.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    
    ax4.legend(fontsize=legend_size)

#    text1 = ax3.yaxis.get_offset_text()
#    offset3 = text1._text

#    ax3.yaxis.offsetText.set_visible(False)
#    ax3.text(150.,-0.0005,offset3,fontsize=20)

#    ax.set_title(st + ': ' + str(i*dt) + ' Myr')
    plt.savefig(wdir_script+'/initial.png')
    plt.show()
    plt.close()