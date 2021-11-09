import numpy as np
import glob, os
import pickle
from runAR import runModelFromArray
from ARfromJSON import loadData

#Returns the model in modelDirectory that most accurately fits the JSON file at pathname logs
def compare(logs, sensorUnit, sensor, modelDirectory):

	#How many datapoints the model looks back to determine "fit" of model
	#PRECONDITION: timescale >= 2
	timescale = 20

	#Returns r^2 value of two datasets
	def r2(actual, predicted):
		corr_matrix = np.corrcoef(actual, predicted)
		corr = corr_matrix[0,1]
		return corr**2

	#Calculate predictions from model for previous timsecale data points
	def determinePredictions(model, data):
		predictions = []
		for i in range(len(data) - 2):
			slice = data[i:i+2]
			predictions.append(runModelFromArray(slice, model))
		return predictions

	models = []
	#Models stored locally for time being
	#Will be pulled from cloud in the future
	os.chdir(modelDirectory)
	for file in glob.glob("*.obj"):
		models.append(file)

	readings = loadData(logs, sensorUnit, sensor)

	if len(readings) > timescale:
		readings = readings[-timescale:]

	if len(readings) < 2:
		raise ValueError("timescale must be >= 2")

	modelScores = {}

	for model in models:
		modelScores[model] = r2(readings[2:], determinePredictions(model, readings))

	return max(modelScores, key=modelScores.get)
