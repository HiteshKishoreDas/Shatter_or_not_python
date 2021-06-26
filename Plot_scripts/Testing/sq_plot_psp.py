import numpy as np
import fourier as fr 
from matplotlib import pyplot as plt
import dcst

wid = 0.01 #Square wave pulse width
ul =100
nbin=1000

x_a = 0.0
x_b = 4.0

def func1 (x):
    return np.sin(10*x)

def func3 (x,width):
    if np.abs(x-(x_b+x_a)*3./6.) < width:
        return 1.0
    # elif np.abs(x-(x_b+x_a)*2./6.) < width:
    #     return 1.0
    # elif np.abs(x-(x_b+x_a)*3./6.) < width:
    #     return 1.0
    # elif np.abs(x-(x_b+x_a)*4./6.) < width:
    #     return 1.0
    # elif np.abs(x-(x_b+x_a)*5./6.) < width:
    #     return 1.0
    # elif np.abs(x-(x_b+x_a)*6./6.) < width:
    #     return 1.0
    # elif np.abs(x-(x_b+x_a)*0./6.) < width:
    #     return 1.0
    else:
        return 0.0

labelsize =40
ticksize  =35
titlesize =45 
offsetsize=35
legendsize=40

x = np.linspace(x_a,x_b,num=5000)

rho1 = func1(x)
# rho2 = func2(x)
# rho3 = np.vectorize(func3)(x,wid)

# E1,k1 = fr.fourier_bin(x*ul,rho1,nbin)
# E2,k2 = fr.fourier_bin(x,rho2,150)
# E3,k3 = fr.fourier_bin(x,rho3,150)

rho1_k = dcst.dct(rho1)
rho1_k = np.abs(rho1_k)
# rho2_k = dcst.dct(rho2)
# rho2_k = np.abs(rho2_k)
# rho3_k = dcst.dct(rho3)
# rho3_k = np.abs(rho3_k)

k_arr = np.array([k for k in range(np.size(rho1_k))])

wid_arr=np.array([1.0,0.1,0.01])

fig, (ax_rho, ax_psp) = plt.subplots(1, 2, figsize=(30,10))

# fig_rho = plt.figure(figsize=(10,10))
# fig_dct = plt.figure(figsize=(10,10))
# fig_psp = plt.figure(figsize=(10,10))

# ax_rho = fig_rho.add_subplot(111)
# ax_dct = fig_dct.add_subplot(111)
# ax_psp = fig_psp.add_subplot(111)

# ax_dct.set_xscale('log')
# ax_dct.set_yscale('log')
ax_psp.set_xscale('log')
ax_psp.set_yscale('log')

ls_arr = ['-.','solid','--']
col_arr = ['tab:blue','tab:orange','tab:red']

for i_wd,wid_n in enumerate(wid_arr):
    # rho_n = np.vectorize(func5)(x,wid_n,0.01)
    # rho_n = np.vectorize(func4)(x,np.pi,wid_n)
    rho_n = np.vectorize(func3)(x,wid_n)
    En,kn = fr.fourier_bin(x,rho_n,nbin)
    rhon_k = dcst.dct(rho_n)
    rhon_k = np.abs(rhon_k)

    ax_rho.plot(x,rho_n,label=str(wid_n*2),linewidth=7,linestyle=ls_arr[i_wd],color=col_arr[i_wd])
    # ax_dct.plot(k_arr[rhon_k>1e-8],rhon_k[rhon_k>1e-8],label=str(wid_n),linewidth=5)
    ax_psp.plot(kn[En>1e-10],En[En>1e-10],label=str(wid_n*2),linewidth=7,linestyle=ls_arr[i_wd],color=col_arr[i_wd])

ax_rho.legend(fontsize=legendsize)
# ax_dct.legend(fontsize=legendsize)
ax_psp.legend(fontsize=legendsize)

ax_rho.tick_params(labelsize=ticksize)
# ax_dct.tick_params(labelsize=ticksize)
ax_psp.tick_params(labelsize=ticksize)

ax_rho.set_xlabel('x',fontsize=labelsize)
ax_rho.set_ylabel(r'$\rho$',fontsize=labelsize)

ax_psp.set_xlabel('k',fontsize=labelsize)
ax_psp.set_ylabel(r'$E_{\rho}$',fontsize=labelsize)


ax_rho.set_title("Density profile",fontsize=titlesize)
# ax_dct.set_title("dct for triple square pulse",fontsize=titlesize)
ax_psp.set_title("Power spectrum",fontsize=titlesize)

fig.savefig("Square_plots/plot_square.png")