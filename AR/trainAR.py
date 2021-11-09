from statsmodels.tsa.ar_model import AutoReg
import pickle
from ARfromJSON import loadData

# load dataset
train = loadData("ESP1", "FlexSensor")

# train autoregression
model = AutoReg(train, lags=2)
model_fit = model.fit()
coef = model_fit.params

#save model to file
saved_model = open('model_fit.obj', 'wb') 
pickle.dump(model_fit, saved_model)
saved_model.close()

print("Finished")
