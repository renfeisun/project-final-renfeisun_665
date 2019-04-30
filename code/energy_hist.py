import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, date_range, read_csv
import datetime

def energy_series():
	time = date_range(start='1/11/2016 17:00:00', end='5/27/2016 18:00:00', freq='10min')
	plt.rcParams.update({'font.size': 40})
	data = []
	f = './energydata_complete.csv'
	with open(f, 'r') as fr:
		fr.readline()
		for line in fr:
			line = line.strip().split(',')
			row = col =index = 0        
			date = datetime.datetime.strptime(line[0].replace('"', '').strip(), '%Y-%m-%d %H:%M:%S').day
			energy = int(line[1].replace('"', '').strip())
			data.append(energy)
	data = np.asarray(data)
	ts = Series(data, index=time)
	plt.figure(num=1, figsize=(80, 20), dpi=80, facecolor='w', edgecolor='k')
	ts.plot()
	plt.savefig(r"figure_1.png")


def energy_freq():
	plt.rcParams.update({'font.size': 40})
	f = './output.csv'
	df = read_csv(f)
	df = df[['Appliances']]
	hist = df.hist(bins = 60, figsize=(80,20))
	plt.savefig(r"figure_1.png")
	df.boxplot(column='Appliances', vert=False, figsize=(80,20))
	plt.savefig(r"figure_2.png")

def energy_freq_mean():
	f = './output.csv'
	df = read_csv(f)
	df = df[['Appliances']]
	df.boxplot(column='Appliances', vert=False, fontsize=10)
	plt.show()
	plt.savefig(r"figure_1.png")
energy_freq_mean()
