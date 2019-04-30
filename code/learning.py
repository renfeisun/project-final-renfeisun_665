import sys

import numpy as np
import pickle
import math
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

import data
import models

def getData(data):
	print("Split data...")	
	kf = KFold(10)
	index = kf.split(data)
	return index, data

def training_KFold(index, data, name):	
	_min = sys.maxsize
	_model = None	
	for train, validation in index:
		train_set = data[train]
		validation_set = data[validation]
		training_X, training_y = models.features_labels(train_set)
		validation_X, validation_y = models.features_labels(validation_set)		
		if name == 'gbr':		
			model, error = models.gbr(training_X, training_y, validation_X, validation_y)
		if name == 'svm':
			model, error = models.svm(training_X, training_y, validation_X, validation_y)
		if name == 'rfr':
			model, error = models.rfr(training_X, training_y, validation_X, validation_y)
		if name == 'mlr':
			model, error = models.mlr(training_X, training_y, validation_X, validation_y)
		if _min > error:
			_min = error
			_model = model
			print("update model")		
		print(error)
		print()
	return _model

def training(data, name, arg):
	training_set = data[: 3 * len(data) // 4]
	validation_set = data[3 * len(data) // 4 :]		
	training_X, training_y = models.features_labels(training_set)
	validation_X, validation_y = models.features_labels(validation_set)		
	if name == 'gbr':		
		model, error = models.gbr(training_X, training_y, validation_X, validation_y, n_estimators = 10, min_samples_split = arg)
	if name == 'svm':
		model, error = models.svm(training_X, training_y, validation_X, validation_y)
	if name == 'rfr':
		model, error = models.rfr(training_X, training_y, validation_X, validation_y)
	if name == 'mlr':
		model, error = models.mlr(training_X, training_y, validation_X, validation_y)
	print(error)
	print()
	return model

def testing(model, test_set):
	print("testing...")
	testing_X, testing_y = models.features_labels(test_set)
	error = models.testing_model(model, testing_X, testing_y)
	print(error)	


def main(argv):
	train_set, test_set = data.readFile(argv[1])
	index, _data = getData(train_set)
	n_estimators = np.arange(0.1, 0.5, 0.01)
	for n_estimator in n_estimators:	
		model = training(_data, argv[2], n_estimator)
	testing(model, test_set)

if __name__ == '__main__':
	main(sys.argv)

