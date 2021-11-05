from pandas import read_csv
from statsmodels.tsa.ar_model import AutoReg
import pickle

# load dataset
series = read_csv('SP5001.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

# retrieve values
train = series.values

# train autoregression
model = AutoReg(train, lags=2)
model_fit = model.fit()
coef = model_fit.params

#save model to file
saved_model = open('model_fit.obj', 'wb') 
pickle.dump(model_fit, saved_model)
saved_model.close()

print("Finished")