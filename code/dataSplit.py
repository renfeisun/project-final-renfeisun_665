import numpy as np
import sys
import datetime

def readFile(input_f, output1_f, output2_f):
	data_active = []
	data_nonactive = []
	with open(input_f, 'r') as fr:
		fr.readline()
		head = ["Appliances","lights","T1","RH_1","T2","RH_2","T3","RH_3","T4","RH_4","T5","RH_5","T6","RH_6","T7","RH_7","T8","RH_8","T9","RH_9","T_out","Press_mm_hg","RH_out","Windspeed","Visibility","Tdewpoint","rv1","rv2", "WeekStatus", "Mon", "Tue", "Wed", "Thrs", "Fri", "Sat", "Sun"]		
		data_active.append(head)
		data_nonactive.append(head)
		for line in fr:
			line = line.strip()
			fileds = line.split(",")
			row = []
			temp = []
			NSM = 0
			for i, item in enumerate(fileds):
				item = item.replace('"', '').strip()				
				if i != 0:
					item = float(item)
					row.append(str(item))
				else:				
					item = datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
					weekStatus = 1 if item.weekday() < 5 else 0
					weekDay = ["1" if item.weekday() == i else "0" for i in range(7)]				
					NSM = (item - item.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
					#temp.append(str(NSM))
					temp.append(str(weekStatus))
					temp += weekDay		
			row += temp
			if NSM >= 25200 and NSM <= 75600:
				data_active.append(row)
			else:
				data_nonactive.append(row)
	with open(output1_f, 'w') as fw:
		for rwo in data_active:
			fw.write(",".join(rwo) + "\n")
	with open(output2_f, 'w') as fw:
		for rwo in data_nonactive:
			fw.write(",".join(rwo) + "\n")

readFile(sys.argv[1], sys.argv[2], sys.argv[3])
