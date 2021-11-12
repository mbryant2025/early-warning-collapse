from statsmodels.tsa.ar_model import AutoReg
import pickle
from ARfromJSON import loadData

#Returns next projected value from data
#data is the pathname for a JSON file containing sensor readings
#model is the name of a .obj file in local directory. This is obtained from trainAR.py
#sensorUnit and sensor are to find the data in the JSON file, ex. "ESP1" and "FlexSensor" respectively
def runModel(data, model, sensorUnit, sensor):
	#number of previous data points loaded
	backtrack = 150

	#load dataset
	series = loadData(data, sensorUnit, sensor)
	prev = series[-backtrack:]

	#load model
	file_to_read = open(model, "rb")
	model_fit = pickle.load(file_to_read)
	file_to_read.close()
	coef = model_fit.params

	#run through model
	window = 2
	predictions = list()
	length = len(prev)
	lag = [prev[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	prediction = yhat

	return prediction

def runModelFromArray(data, model):
	#number of previous data points loaded
	backtrack = 150

	#load dataset
	prev = data[-backtrack:]

	#load model
	file_to_read = open(model, "rb")
	model_fit = pickle.load(file_to_read)
	file_to_read.close()
	coef = model_fit.params

	#run through model
	window = 2
	predictions = list()
	length = len(prev)
	lag = [prev[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	prediction = yhat

	return prediction

