




import matplotlib.pyplot as mp
import matplotlib.ticker as mtick

import re
import numpy as np
import pandas as pd




DUT_name = "G3_L03"

W="10"
L="0.4"

type="CORNER"

walter_meas_path = r"C:\All_projects\C35_model_assessment\PLots_Spice_modeling\CORNER\data\\"

Device_name="c35_NMOSIMW_" + type + "_PLOT__" + DUT_name + "_TR__IDVG_LIN_T_p025_meas"
filename = Device_name + ".txt"

Device_name_simulation = "c35_NMOSIMW_" + type + "_PLOT__" + DUT_name + "_TR__IDVG_LIN_T_p025_tt_lib_25C"
filename_sim=Device_name_simulation + ".txt"



#############
with open(walter_meas_path + filename) as file:
    lines = file.readlines()
lines = [line.lstrip() for line in lines]



output_filename=Device_name + '_output.txt'

with open(walter_meas_path + output_filename, 'w') as file:
    file.writelines(lines)

with open(walter_meas_path + output_filename) as f:
    df = pd.read_csv(f, sep="\s+", header=None, engine='python')

df.columns = ["Vgs", "ID_VB0", "ID_VB1", "ID_VB2"]

# Remove leading spaces from each line

print(lines)


print(df)

#################



#############
with open(walter_meas_path + filename_sim) as file:
    lines = file.readlines()
lines = [line.lstrip() for line in lines]



output_filename=Device_name_simulation + '_output.txt'

with open(walter_meas_path + output_filename, 'w') as file:
    file.writelines(lines)

with open(walter_meas_path + output_filename) as f:
    df_s = pd.read_csv(f, sep="\s+", header=None, engine='python')

df_s.columns = ["Vgs", "ID_VB0", "ID_VB1", "ID_VB2"]

# Remove leading spaces from each line

print(lines)


print(df_s)

#################





Vgs_value =df['Vgs']
ID_VB0=df['ID_VB0']
ID_VB1=df['ID_VB1']
ID_VB2=df['ID_VB2']



Vgs_value_sim =df_s['Vgs']
ID_VB0_sim=df_s['ID_VB0']
ID_VB1_sim=df_s['ID_VB1']
ID_VB2_sim=df_s['ID_VB2']



fig, ax = mp.subplots()
ax.scatter(Vgs_value,ID_VB0, s=25, c='k', marker="x", label="VB=0" )
ax.scatter(Vgs_value,ID_VB1, s=25, c='k', marker="x", label="VB=-0.7" )
ax.scatter(Vgs_value,ID_VB2, s=25, c='k', marker="x", label="VB=-1.4" )


ax.plot(Vgs_value_sim,ID_VB0_sim, 'r-' )
ax.plot(Vgs_value_sim,ID_VB1_sim, 'r-' )
ax.plot(Vgs_value_sim,ID_VB2_sim, 'r-' )
ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
#ax.get_xaxis().get_major_formatter().set_useOffset(False)
ax.yaxis.get_major_formatter().set_scientific(False)
ax.yaxis.get_major_formatter().set_useOffset(False)

#ax.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))

#.ticklabel_format(style='sci', axis='both', scilimits=(0,0))


picname = "Id-Vgs Vds0p1" + Device_name + type + "_Waffle.png"
#mp.title(picname)

#title = ax.set_title(picname)
#title.set_y(3.05)  # Adjust the vertical position


mp.xlabel('Vgs(V)')
mp.ylabel('Id(A)')


mp.grid()
#mp.legend(["NMOSIMW-Measurement",  'NMOSIMW-Simulation'],loc="lower right")
mp.savefig(picname, bbox_inches='tight')

mp.show()
mp.close()


fig, bx = mp.subplots()
bx.scatter(Vgs_value,ID_VB0, s=25, c='k', marker="x", label="VB=0" )
bx.scatter(Vgs_value,ID_VB1, s=25, c='k', marker="x", label="VB=-0.7" )
bx.scatter(Vgs_value,ID_VB2, s=25, c='k', marker="x", label="VB=-1.4" )


bx.plot(Vgs_value_sim,ID_VB0_sim, 'r-' )
bx.plot(Vgs_value_sim,ID_VB1_sim, 'r-' )
bx.plot(Vgs_value_sim,ID_VB2_sim, 'r-' )
bx.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
bx.get_xaxis().get_major_formatter().set_useOffset(False)

picname = "Id-Vgs Vds0p1" + Device_name + type +"_Waffle_log.png"
#mp.title(picname)
mp.xlabel('Vgs(V)')
mp.ylabel('Id(A)')


mp.yscale("log")
mp.grid()
#mp.legend(["NMOSIMW-Measurement",  'NMOSIMW-Simulation'], loc="lower right")
mp.savefig(picname, bbox_inches='tight')


mp.show()


#c35_NMOSIMW_CENTER_PLOT__G1_L01_OUT_IDVD_VB0_T_p025_meas.txt

Device_output_name="c35_NMOSIMW_" + type + "_PLOT__" + DUT_name + "_OUT_IDVD_VB0_T_p025_meas"
filename_output = Device_output_name + ".txt"

#c35_NMOSIMW_CENTER_PLOT__G1_L01_OUT_IDVD_VB0_T_p025_tt_lib_25C

Device_output_name_simulation = "c35_NMOSIMW_" + type + "_PLOT__" + DUT_name + "_OUT_IDVD_VB0_T_p025_tt_lib_25C"
filename_output_sim=Device_output_name_simulation + ".txt"


#############
with open(walter_meas_path + filename_output) as file:
    lines_output = file.readlines()
lines = [line.lstrip() for line in lines_output]



output_filename=Device_output_name + '_output.txt'

with open(walter_meas_path + output_filename, 'w') as file:
    file.writelines(lines)

with open(walter_meas_path + output_filename) as f:
    df = pd.read_csv(f, sep="\s+", header=None, engine='python')

df.columns = ["Vds", "ID_VG1", "ID_VG2", "ID_VG3", "ID_VG4", "ID_VG5"]

# Remove leading spaces from each line

print(lines)


print(df)






#############
with open(walter_meas_path + filename_output_sim) as file:
    lines = file.readlines()
lines = [line.lstrip() for line in lines]



output_filename=Device_output_name_simulation + '_output.txt'

with open(walter_meas_path + output_filename, 'w') as file:
    file.writelines(lines)

with open(walter_meas_path + output_filename) as f:
    df_s = pd.read_csv(f, sep="\s+", header=None, engine='python')

df_s.columns = ["Vds", "ID_VG1", "ID_VG2", "ID_VG3", "ID_VG4", "ID_VG5"]

print(df_s)

Vds_value =df['Vds']
ID_VG1=df['ID_VG1']
ID_VG2=df['ID_VG2']
ID_VG3=df['ID_VG3']
ID_VG4=df['ID_VG4']
ID_VG5=df['ID_VG5']


Vds_value_sim =df_s['Vds']
ID_VG1_sim=df_s['ID_VG1']
ID_VG2_sim=df_s['ID_VG2']
ID_VG3_sim=df_s['ID_VG3']
ID_VG4_sim=df_s['ID_VG4']
ID_VG5_sim=df_s['ID_VG5']




fig, cx = mp.subplots()
cx.scatter(Vds_value,ID_VG1, s=25, c='k', marker="x", label="VGS=1" )
cx.scatter(Vds_value,ID_VG2, s=25, c='k', marker="x", label="VGS=2" )
cx.scatter(Vds_value,ID_VG3, s=25, c='k', marker="x", label="VGS=3" )
cx.scatter(Vds_value,ID_VG4, s=25, c='k', marker="x", label="VGS=4" )
cx.scatter(Vds_value,ID_VG5, s=25, c='k', marker="x", label="VGS=5" )


cx.plot(Vds_value_sim,ID_VG1_sim, 'r-' )
cx.plot(Vds_value_sim,ID_VG2_sim, 'r-' )
cx.plot(Vds_value_sim,ID_VG3_sim, 'r-' )
cx.plot(Vds_value_sim,ID_VG4_sim, 'r-' )
cx.plot(Vds_value_sim,ID_VG5_sim, 'r-' )


cx.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
#ax.get_xaxis().get_major_formatter().set_useOffset(False)
cx.yaxis.get_major_formatter().set_scientific(False)
cx.yaxis.get_major_formatter().set_useOffset(False)

#ax.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))

#.ticklabel_format(style='sci', axis='both', scilimits=(0,0))


picname = "Id-Vds_Output__" + Device_name +"__" + type + "_Waffle.png"
#mp.title(picname)

#title = ax.set_title(picname)
#title.set_y(3.05)  # Adjust the vertical position


mp.xlabel('Vds(V)')
mp.ylabel('Id(A)')


mp.grid()
#mp.legend(["NMOSIMW-Measurement",  'NMOSIMW-Simulation'],loc="lower right")
mp.savefig(picname, bbox_inches='tight')

mp.show()
mp.close()
