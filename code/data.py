import numpy as np
import sys

def readFile(fileName):
	print("Loading data...")	
	data = np.loadtxt(open(fileName, "r"), delimiter=",", skiprows=1)
	training_set = data[: 3 * len(data) // 4]
	test_set = data[3 * len(data) // 4 :]
	return training_set, test_set

#readFile(sys.argv[1])
