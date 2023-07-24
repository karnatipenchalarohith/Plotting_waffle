

import pandas as pd
import matplotlib.pyplot as mp

#from scipy.stats import linregress
#from sklearn import linear_model







path_point_meas= r"C:\All_projects\C35_model_assessment\Data\CV_modified\\"

Device_name="NMOSWTM2"

filename= Device_name + '.txt'

site=1

with open(path_point_meas + filename) as file:
    lines = file.readlines()


# Remove leading spaces from each line
lines = [line.lstrip() for line in lines]


#remove first 6 lines
num_lines=7
remaining_lines = lines[num_lines:]


output_filename=Device_name + '_output.txt'

with open(path_point_meas + output_filename, 'w') as file:
    file.writelines(remaining_lines)

with open(path_point_meas + output_filename) as f:
    df = pd.read_csv(f, sep="\s+", header=None, engine='python')

#df.columns=["MeasID"]

df.columns = ["Vgateval", "Cpval", "Gval", "Dval", "Rpval", "Csval", "Xval","Rsval", "Zval", "Thetaval"]

print(df)
file_csv= path_point_meas + Device_name + '.csv'
df[['Vgateval', 'Cpval']].to_csv(file_csv, index=False)

Vgate =df['Vgateval']
Cgg_parallel=df['Cpval']
Cgg_series=df['Csval']

mp.scatter(Vgate,Cgg_parallel )
mp.show()


mp.scatter(Vgate,Cgg_series )
mp.show()