import numpy as np
import glob, os
import pickle

#How many datapoints the model looks back to determine "fit" of model
timescale = 20

#Temp random data
data = np.random.randint(800, 900, size = 20)

#Returns r^2 value of two datasets
def r2(actual, predicted):
    corr_matrix = np.corrcoef(actual, predicted)
    corr = corr_matrix[0,1]
    return corr**2
 
models = []
#Models stored locally for time being,
#Will be pulled from cloud in the future
os.chdir("/Users/michaelbryant/Desktop/ar")
for file in glob.glob("*.obj"):
    models.append(file)


window = 2

#load model
file_to_read = open("model_fit.obj", "rb")
model_fit = pickle.load(file_to_read)
file_to_read.close()
coef = model_fit.params

# walk forward over time steps in test
history = data[len(data)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(data)):
	length = len(history)
	lag = [history[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	obs = data[t]
	predictions.append(yhat)
	history.append(obs)


max = (None, 0)
for model in models:
    r2 = r2(data, predictions)
    if r2 > max[1]:
        max = (model, r2)

print(model)
print(max[1])