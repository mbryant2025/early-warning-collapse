from pandas import read_csv
from matplotlib import pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
import pickle

#Number of previous data points loaded
backtrack = 150


# load dataset
series = read_csv('SP5002.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
prev = series.values[-backtrack:]

#load model
file_to_read = open("model_fit.obj", "rb")
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

# output
print(prediction)