from runAR import runModelFromArray
from ARfromJSON import loadData
import numpy as np

#----------------------------------------------------------------------------------------
#Inputs both actual data (post-MA) and projected data to determine risk of collapse
#Calculates (absolute value) z-score of previous 20 data points versus their projected values
#If the total z-score of these values exceeds a certain threshold, a collapse is detected
#----------------------------------------------------------------------------------------

#Returns True or False if a collapse is detected
#data is the name of a JSON file in the local directory containing sensor readings
#model is the name of the .obj file in local directory that most accurately fits the current data. 
    #This is obtained from trainAR.py
#sensorUnit and sensor are to find the data in the JSON file, ex. "ESP1" and "FlexSensor" respectively
def detectCollapse(data, model, sensorUnit, sensor):


    #Collapse threshold
    #*****************
    threshold = 10
    #*****************


    #number of previous data points loaded
    #20 datapoints considered, 2 more needed for initial predictions
    backtrack = 20 + 2

    #load dataset
    series = loadData(data, sensorUnit, sensor)
    prev = series[-backtrack:]
    
    predictions = []
    for i in range(len(prev) - 2):
        slice = prev[i:i+2]
        predictions.append(runModelFromArray(slice, model))

    comparativeSensorReadings = prev[2:]

    zscores = []
    stddev = np.std(comparativeSensorReadings)
    mean = np.mean(comparativeSensorReadings)

    for i in range(len(comparativeSensorReadings)):
        zscores.append(abs((comparativeSensorReadings[i] - mean)/stddev))

    return np.sum(zscores) > threshold


#Sample code
#print(detectCollapse("Proto3.json", "model_fit.obj", "ESP1", "FlexSensor"))
