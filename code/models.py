#!/usr/bin/env python -W ignore::DeprecationWarning
import sys
import math

import data

import numpy as np
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor

def features_labels(data):
	print("Extract data...")
	labels = np.reshape(data[:,:1],len(data[:,:1]))
	features = data[:,1:]
	return features, labels

def training_model(model, training_X,training_y):
	print('Training...')	
	model.fit(training_X,training_y)
	return model

def testing_model(model, testing_X, testing_y):
	print('Testing...')
	prediction = model.predict(testing_X)
	print('Calculating error...')
	RMSE = math.sqrt(mean_squared_error(testing_y, prediction))
	R2 = r2_score(testing_y, prediction)
	MAPE = mean_absolute_error(testing_y, prediction)
	return RMSE, R2, MAPE

def svm(training_X, training_y, testing_X, testing_y):
	print("SVM:")
	model = SVR(kernel='rbf', degree=3, coef0=0.0, tol=0.001, C=1.0, epsilon=0.1, shrinking=True, cache_size=200, verbose=False, max_iter=-1, gamma='auto')
	model = training_model(model, training_X,training_y)
	error = testing_model(model, testing_X, testing_y)
	return model, error

def gbr(training_X, training_y, testing_X, testing_y, n_estimators = 1, max_depth = 100, min_samples_split = 100, learning_rate = 0.1):
	print("Gradient Boosting Regression:")
	params = {'loss' : 'ls', 'alpha': 0.95, 'n_estimators': n_estimators, 'max_depth': max_depth, 'min_samples_split': min_samples_split, 'learning_rate': learning_rate, 'min_samples_leaf' : 100}
	model = GradientBoostingRegressor(**params)
	model = training_model(model, training_X,training_y)
	error = testing_model(model, testing_X, testing_y)
	return model, error

def rfr(training_X, training_y, testing_X, testing_y, max_features = 'auto',  min_samples_leaf = 50, n_estimators = 100):
	print("Random Forest Regression:")
	model = RandomForestRegressor(max_features = max_features,  min_samples_leaf = min_samples_leaf, n_estimators = n_estimators)
	model = training_model(model, training_X,training_y)
	error = testing_model(model, testing_X, testing_y)
	return model, error

def mlr(training_X, training_y, testing_X, testing_y):
	print("Multiple Linear Regression:")	
	model = LinearRegression()
	model = training_model(model, training_X,training_y)
	error = testing_model(model, testing_X, testing_y)
	return model, error

def nn(training_X, training_y, testing_X, testing_y):
        print("Multiple Layer Perceptron Regressor:")
        model = MLPRegressor()
        model = training_model(model, training_X,training_y)
        error = testing_model(model, testing_X, testing_y)
        return model, error

def knn(training_X, training_y, testing_X, testing_y):
        print("k-nearest neighbors Regressor:")
        model = KNeighborsRegressor(n_neighbors = 50)
        model = training_model(model, training_X,training_y)
        error = testing_model(model, testing_X, testing_y)
        return model, error

def main(argv):
	training_set, testing_set = data.readFile(argv[1])
	training_X, training_y = features_labels(training_set)
	testing_X, testing_y = features_labels(testing_set)
	model, error = svm(training_X, training_y, testing_X, testing_y)
	print(error)
	print()
	model, error = gbr(training_X, training_y, testing_X, testing_y)
	print(error)
	print()
	model, error = rfr(training_X, training_y, testing_X, testing_y)
	print(error)
	print()
	model, error = mlr(training_X, training_y, testing_X, testing_y)
	print(error)
	print()

if __name__ == '__main__':
	main(sys.argv)
