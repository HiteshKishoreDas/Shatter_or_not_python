import numpy as np
import fourier as fr 
from matplotlib import pyplot as plt
import dcst

wid = 0.01 #Square wave pulse width

def func1 (x):
    return np.sin(10*x)

def func2 (x):
    return np.cos(10*x)

def func3 (x,width):
    if np.abs(x-np.pi) < width:
        return 1.0
    else:
        return 0.0

def func4 (x,mean,std):
    
    return np.exp(-0.5*(x-mean)**2/std**2)

def func5 (x,width1,width2):
    if np.abs(x-np.pi) < width1:
        return 1.0
    elif np.abs(x-np.pi-width1) < width2:
        return 3.0
    elif np.abs(x-np.pi+width1) < width2:
        return 3.0
    else:
        return 0.0

x = np.linspace(0,2*np.pi,num=1000)

rho1 = func1(x)
# rho2 = func2(x)
# rho3 = np.vectorize(func3)(x,wid)

E1,k1 = fr.fourier_bin(x,rho1,150)
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

fig_rho = plt.figure(figsize=(10,10))
fig_dct = plt.figure(figsize=(10,10))
fig_psp = plt.figure(figsize=(10,10))

ax_rho = fig_rho.add_subplot(111)
ax_dct = fig_dct.add_subplot(111)
ax_psp = fig_psp.add_subplot(111)

ax_dct.set_xscale('log')
ax_dct.set_yscale('log')
ax_psp.set_xscale('log')
ax_psp.set_yscale('log')

for wid_n in wid_arr:
    rho_n = np.vectorize(func5)(x,wid_n,0.01)
    # rho_n = np.vectorize(func4)(x,np.pi,wid_n)
    # rho_n = np.vectorize(func3)(x,wid_n)
    En,kn = fr.fourier_bin(x,rho_n,150)
    rhon_k = dcst.dct(rho_n)
    rhon_k = np.abs(rhon_k)

    ax_rho.plot(x,rho_n,label=str(wid_n),linewidth=5)
    ax_dct.plot(k_arr[rhon_k>1e-8],rhon_k[rhon_k>1e-8],label=str(wid_n),linewidth=5)
    ax_psp.plot(kn[En>1e-10],En[En>1e-10],marker='x',label=str(wid_n),linewidth=5)

ax_rho.legend(fontsize=20)
ax_dct.legend(fontsize=20)
ax_psp.legend(fontsize=20)

ax_rho.set_title("density profile for triple square pulse",fontsize=30)
ax_dct.set_title("dct for triple square pulse",fontsize=30)
ax_psp.set_title("Power spectrum for triple square pulse",fontsize=30)

fig_rho.savefig("Square_plots/triple_square/rho_3square.png")
fig_dct.savefig("Square_plots/triple_square/dct_3square.png")
fig_psp.savefig("Square_plots/triple_square/psp_3square.png")

# ax_rho.set_title("density profile for gaussian pulse",fontsize=30)
# ax_dct.set_title("dct for gaussian pulse",fontsize=30)
# ax_psp.set_title("Power spectrum for gaussian pulse",fontsize=30)

# fig_rho.savefig("Square_plots/rho_gauss.png")
# fig_dct.savefig("Square_plots/dct_gauss.png")
# fig_psp.savefig("Square_plots/psp_gauss.png")

# ax_rho.set_title("density profile for square pulse",fontsize=30)
# ax_dct.set_title("dct for square pulse",fontsize=30)
# ax_psp.set_title("Power spectrum for square pulse",fontsize=30)

# fig_rho.savefig("Square_plots/rho_square.png")
# fig_dct.savefig("Square_plots/dct_square.png")
# fig_psp.savefig("Square_plots/psp_square.png")


# plt.figure()
# plt.plot(x,rho1,color='tab:red')
# plt.title('rho plot for sine')
# plt.savefig('rho_sin.png')
# # plt.show()

# plt.figure()
# plt.plot(x,rho2,color='tab:blue')
# plt.title('rho plot for cosine')
# plt.savefig('rho_cos.png')
# # plt.show()

# plt.figure()
# plt.plot(x,rho3,color='tab:green')
# plt.title('rho plot for square: Width '+str(wid))
# plt.savefig('rho_sqr_'+str(wid)+'.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k_arr[rho1_k>1e-8],rho1_k[rho1_k>1e-8],marker='x')
# plt.title('dct for sine')
# plt.savefig('dct_sin.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k_arr[rho2_k>1e-8],rho2_k[rho2_k>1e-8],marker='x')
# plt.title('dct for cosine')
# plt.savefig('dct_cos.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k_arr[rho3_k>1e-8],rho3_k[rho3_k>1e-8],marker='x')
# plt.title('dct for square: Width '+str(wid))
# plt.savefig('dct_sqr_'+str(wid)+'.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k1[E1>1e-10],E1[E1>1e-10],marker='x')
# plt.title('Power spectrum for sine')
# plt.savefig('power_sin.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k2[E2>1e-10],E2[E2>1e-10],marker='x')
# plt.title('Power spectrum for cosine')
# plt.savefig('power_cos.png')
# # plt.show()

# plt.figure()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(k3[E3>1e-10],E3[E3>1e-10],marker='x')
# plt.title('Power spectrum for square: Width '+str(wid))
# plt.savefig('power_sqr_'+str(wid)+'.png')
# # plt.show()