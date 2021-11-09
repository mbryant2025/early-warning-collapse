import time
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(num=1, clear=True)
fig.set_size_inches(6, 6, forward=True)
ax = fig.add_subplot(1, 1, 1)
ax.set(
       xlabel="Time (secs)",
       ylabel="Displacement",
       title="Displacement over time"
       )

#Returns a numpy array of shape (sensors, timeTotal//timeAvg) representing data from each sensor over time
#Data deviates from previous entries by +/- varation
def generateData(sensors, timeAvg = 1, timeTotal = 3, movingAverage = 2, variation = 5):
    timePoints = int(timeTotal / timeAvg)
    data = np.zeros((sensors, timePoints))
    data = np.transpose(data)
    for i in range(timePoints):
        if i == 0:
            data[0] = np.random.randint(-variation, variation, sensors)
        else:
            data[i] = data[i - 1] + np.random.randint(-variation, variation, sensors)
    data = np.transpose(data)
    
    return data

#Returns a list representing the moving averages of the inputted data
#Combines the data from all sensors
def findTotalMovingAverages(data, timescale = 2):
    data = np.transpose(data)
    averages = []
    for i in range(len(data)):
        if i == 0:
            averages.append(np.average(data[0]))
        elif i < timescale:
            averages.append(np.average(data[:i + 1]))
        else:
            averages.append(np.average(data[i - timescale + 1:i + 1]))

    return averages

#Returns a numpy array of shape data.shape() representing moving averages for each sensor over time
def findIndividualMovingAverages(data, timescale = 2):
    averages = []
    for sensor in data:
        individualAverage = []
        for i in range(len(sensor)):
            if i == 0:
                individualAverage.append(sensor[i])
            elif i < timescale:
                individualAverage.append(np.average(sensor[:i + 1]))
            else:
                individualAverage.append(np.average(sensor[i - timescale + 1:i + 1]))
        averages.append(individualAverage)

    return averages


#Displays the data and averages, saves plot to local directory
def showPlot(data, totalAverages = None, individualAverages = None):
    if totalAverages is not None:
        plt.plot(totalAverages, label="Total Averages")
    if individualAverages is not None:
        for sensor in enumerate(individualAverages):
            plt.plot(sensor[1], label = "Sensor " + str(sensor[0]) + " Averages")
    for sensor in enumerate(data):
        plt.plot(sensor[1], label="Sensor " + str(sensor[0]))
    plt.legend(loc='best')
    plt.savefig("data.png")
    plt.show()



#To be implemented with notification system
def emergency(time, type, reading, sensor = None):
    if type == "Total":
        print("EMERGENCY at time " + str(time) + " for total sensor average" + ". Reading=" + str(reading))
    if type == "Individual":
        print("EMERGENCY at time " + str(time) + " for sensor " + str(sensor) + ". Reading=" + str(reading))
    

def saveToFile(data):
    file = open("data.txt", "w")
    np.savetxt(file, data)
    file.close()


#Sample runner code
data = generateData(2, 0.1, 20)
#print("Raw sensor data:")
#print(data)

totAvgs = findTotalMovingAverages(data, 20)
#print("Total averages")
#print(totAvgs)

indAvgs = findIndividualMovingAverages(data, 20)
#print("Individual averages:")
#print(indAvgs)

totalEmergencyThreashold = 50
individualEmergencyThreashold = 100

#Check averages for emergency
for datapt in enumerate(totAvgs):
    if datapt[1] > totalEmergencyThreashold or datapt[1] < -totalEmergencyThreashold:
        emergency(datapt[0], "Total", datapt[1])

for avg in enumerate(indAvgs):
    for datapt in enumerate(avg[1]):
        if datapt[1] > individualEmergencyThreashold or datapt[1] < -individualEmergencyThreashold:
            emergency(datapt[0], "Individual", datapt[1], avg[0])

saveToFile(indAvgs)

showPlot(data, totAvgs, indAvgs)


#Look for industry standard
#Look at sensor accuricies and account for those -> go to when you are about 95% certain of the readings

