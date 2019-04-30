import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv, scatter_matrix

import sys


f = sys.argv[1]
df = read_csv(f)
'''
Appliances,lights,T1,RH_1,T2,RH_2,T3,RH_3,T4,RH_4,T5,RH_5,T6,RH_6,T7,RH_7,T8,RH_8,T9,RH_9,T_out,Press_mm_hg,RH_out,Windspeed,Visibility,Tdewpoint,rv1,rv2,NSM,WeekStatus,Mon,Tue,Wed,Thrs,Fri,Sat,Sun
'''
df = df[['Appliances', 'T_out','Press_mm_hg','RH_out','Windspeed','Visibility','Tdewpoint', 'NSM', 'T6']]

#print(df.corr())
my_scatter = scatter_matrix(df, figsize=(50,50))
#y ticklabels
[plt.setp(item.yaxis.get_majorticklabels(), 'size', 20) for item in my_scatter.ravel()]
#x ticklabels
[plt.setp(item.xaxis.get_majorticklabels(), 'size', 20) for item in my_scatter.ravel()]
#y labels
[plt.setp(item.yaxis.get_label(), 'size', 50) for item in my_scatter.ravel()]
#x labels
[plt.setp(item.xaxis.get_label(), 'size', 50) for item in my_scatter.ravel()]
plt.savefig(r"figure_1.png")

