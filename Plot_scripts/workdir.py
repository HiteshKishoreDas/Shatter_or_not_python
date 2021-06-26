#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:09:05 2020

@author: hitesh
"""

import os

# plutodir = os.environ['PLUTO_DIR']


#wdir0 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/'

# wdir1 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_10pi/'
# wdir2 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_50pi/'
# wdir3 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/'

# wdir4 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/'
# wdir5 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.05pi/'
# wdir6 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.01pi/'

# wdir7 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isobaric/'
# wdir8 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_1pi/Isochoric/'
# wdir9 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isobaric/'
# wdir10 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_2pi/Isochoric/'

# wdir11 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Base/'
# wdir12 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamT/'
# wdir13 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isobaric_k10pi/Same_lamZ/'

# wdir14 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Base/'
# wdir15 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamT/'
# wdir16 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/growth_rate/Isochoric_k0.1pi/Same_lamZ/'

# wdir17 = plutodir+ 'TI_uniform/metallicity/'
# wdir18 = plutodir+ 'TI_uniform/metallicity_sec_run/'
# wdir19 = plutodir+ 'TI_uniform/metallicity_thd_run/'

# wdir20 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/long_run/16384_4/'
# wdir21 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_0.1pi/Modified_boundary/Only_inner/'
# wdir22 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/k_100pi/Modified_boundary/Both_boundary/16384_10_Zg0.02/'

# wdir23 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/100pi/0/'
# wdir24 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/100pi/pi_2/'
# wdir25 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/100pi/pi/'

# wdir26 = plutodir+ 'TI_uniform/metallicity_modified_Zbg/'

# wdir27 = plutodir+ 'TI_uniform/metallicity_phase1/'
# wdir28 = plutodir+ 'TI_uniform/metallicity_phase2/'
# wdir29 = plutodir+ 'TI_uniform/metallicity_phase3/'

# wdir30 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/100pi/0/'
# wdir31 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/100pi/pi_2/'
# wdir32 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/100pi/pi/'

# wdir33 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/0.1pi/0/'
# wdir34 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/0.1pi/pi_2/'
# wdir35 = plutodir+ 'TI_uniform/Output_Archive/Linear_Theory/Phase/High_zpert/0.1pi/pi/'

# wdir36 = plutodir+ 'TI_uniform/Output_Archive/With_ceiling/With_outflow/'
# wdir37 = plutodir+ 'TI_uniform/metallicity_frt_run/'

# wdir38 = plutodir+ 'TI_uniform/metallicity_ic_one_run/'
# wdir39 = plutodir+ 'TI_uniform/metallicity_ic_sec_run/'

# wdir40 = plutodir+ '../PLUTO_test/metallicity_cons2prim/'

# wdir41 = plutodir+ '../PLUTO_test/metallicity_cons2prim_ic/'
# wdir42 = plutodir+ '../PLUTO_test/metallicity_cons2prim_ic_sec/'
# wdir43 = plutodir+ '../PLUTO_test/metallicity_cons2prim_ic_thd/'

# wdir44 = plutodir+ 'TI_uniform/Output_Archive/Non-linear/modified_cons2prim/10pi/'
# wdir45 = plutodir+ 'TI_uniform/Output_Archive/Non-linear/modified_cons2prim/0.1pi/'

# wdir46 = plutodir+ '../PLUTO_test/metallicity_lin_1_ib/'
# wdir47 = plutodir+ '../PLUTO_test/metallicity_lin_2_ib/'
# wdir48 = plutodir+ '../PLUTO_test/metallicity_lin_3_ib/'
# wdir49 = plutodir+ '../PLUTO_test/metallicity_lin_1_ic/'
# wdir50 = plutodir+ '../PLUTO_test/metallicity_lin_2_ic/'
# wdir51 = plutodir+ '../PLUTO_test/metallicity_lin_3_ic/'

# wdir52 = plutodir+ '../PLUTO_test/metallicity_X/'

wdir53 = '/home/hitesh/Desktop/saha_results/metallicity_17_nl/'
wdir54 = '/home/hitesh/Desktop/saha_results/metallicity_18_nl/'
wdir55 = '/home/hitesh/Desktop/saha_results/metallicity_19_nl/'
wdir56 = '/home/hitesh/Desktop/saha_results/metallicity_20_nl/'

wdir56 = '/home/hitesh/Desktop/saha_results/metallicity_01/'
wdir57 = '/home/hitesh/Desktop/saha_results/metallicity_02/'
wdir58 = '/home/hitesh/Desktop/saha_results/metallicity_03/'

wdir59 = '/home/hitesh/Desktop/saha_results/metallicity_04/'
wdir60 = '/home/hitesh/Desktop/saha_results/metallicity_05/'
wdir61 = '/home/hitesh/Desktop/saha_results/metallicity_06/'

wdir62 = '/home/hitesh/Desktop/saha_results/metallicity_07/'
wdir63 = '/home/hitesh/Desktop/saha_results/metallicity_08/'
wdir64 = '/home/hitesh/Desktop/saha_results/metallicity_09/'
wdir65 = '/home/hitesh/Desktop/saha_results/metallicity_10/'

wdir66 = '/home/hitesh/Desktop/saha_results/metallicity_11/'
wdir67 = '/home/hitesh/Desktop/saha_results/metallicity_12/'
wdir68 = '/home/hitesh/Desktop/saha_results/metallicity_13/'

wdir69 = '/home/hitesh/Desktop/saha_results/metallicity_14/'
wdir70 = '/home/hitesh/Desktop/saha_results/metallicity_15/'
wdir71 = '/home/hitesh/Desktop/saha_results/metallicity_16/'

wdir72 = '/home/hitesh/Desktop/saha_results/metallicity_22_nl/'
wdir73 = '/home/hitesh/Desktop/saha_results/metallicity_23_nl/'
wdir74 = '/home/hitesh/Desktop/saha_results/metallicity_24_nl/'
wdir75 = '/home/hitesh/Desktop/saha_results/metallicity_25_nl/'

wdir76 = '/home/hitesh/Desktop/saha_results/metallicity_26_nl_wnoise/'
wdir77 = '/home/hitesh/Desktop/saha_results/metallicity_27_nl_wnoise/'

wdir78 = '/home/hitesh/Desktop/saha_results/metallicity_28_nl_test/'

wdir79 = '/home/hitesh/Desktop/saha_results/metallicity_29_nl_oldsetup/'
wdir80 = '/home/hitesh/Desktop/saha_results/metallicity_30_nl_noheating/'
wdir81 = '/home/hitesh/Desktop/saha_results/metallicity_31_nl_noheating/'

wdir82 = '/home/hitesh/Desktop/saha_results/metallicity_32_nl_periodic/'
wdir83 = '/home/hitesh/Desktop/saha_results/metallicity_33_nl_periodic/'

wdir84 = '/home/hitesh/Desktop/saha_results/metallicity_34_nl_diffheat/'
wdir85 = '/home/hitesh/Desktop/saha_results/metallicity_35_nl_diffheat/'

wdir86 = '/home/hitesh/Desktop/saha_results/metallicity_36_nl_isobaric/'

wdir87 = '/home/hitesh/Desktop/saha_results/metallicity_37_nl_lessT_ST/'
wdir88 = '/home/hitesh/Desktop/saha_results/metallicity_38_nl_lessT_ST_periodic/'

wdir89 = '/home/hitesh/Desktop/saha_results/metallicity_39_nl_highres_8192/'
wdir90 = '/home/hitesh/Desktop/saha_results/metallicity_40_nl_highres_2048/'

wdir91 = '/home/hitesh/Desktop/saha_results/metallicity_41_nl_highres_high_drho/'
wdir92 = '/home/hitesh/Desktop/saha_results/metallicity_42_nl_highres_high_drho_periodic_small_box/'
wdir93 = '/home/hitesh/Desktop/saha_results/metallicity_43_nl_highres_periodic_large_highk/'
wdir94 = '/home/hitesh/Desktop/saha_results/metallicity_44_nl_highres_periodic_large_lowk/'

wdir95 = '/home/hitesh/Desktop/saha_results/metallicity_45_nl_periodic_large_lowlow_k/'
wdir96 = '/home/hitesh/Desktop/saha_results/metallicity_46_nl_periodic_large_highhigh_k/'

wdir97 = '/home/hitesh/Desktop/saha_results/metallicity_47_nl_periodic_highk_small_1024/'
wdir98 = '/home/hitesh/Desktop/saha_results/metallicity_48_nl_periodic_highhighk_small_1024/'

wdir99 = '/home/hitesh/Desktop/saha_results/metallicity_49_nl_periodic_10pc_lowk_highdrho/'

wdir100 = '/home/hitesh/Desktop/saha_results/metallicity_50_nl_lowT_512_isochoric/'

wdir101 = '/home/hitesh/Desktop/saha_results/metallicity_51_nl_isochoric_lowT_highres/'
wdir102 = '/home/hitesh/Desktop/saha_results/metallicity_52_nl_isochoric_lowT_vhighres/'


wdir107 = '/home/hitesh/Desktop/saha_results/metallicity_57_isochoric_square/'
wdir107b = '/home/hitesh/Hitesh/Project/metallicity_57b_isochoric_square_unstable/'
wdir107c = '/home/hitesh/Hitesh/Project/metallicity_57c_isochoric_square_stable/'
