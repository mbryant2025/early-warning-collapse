# create and evaluate an updated autoregressive model
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
import pickle

# load dataset
series = read_csv('SP500.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

# split dataset
X = series.values
test_split = 100
train, test = X[1:len(X)-test_split], X[len(X)-test_split:]

# train autoregression
window = 2
model = AutoReg(train, lags=2)
model_fit = model.fit()
coef = model_fit.params

#save model to file
saved_model = open('model_fit.obj', 'wb') 
pickle.dump(model_fit, saved_model)
saved_model.close()