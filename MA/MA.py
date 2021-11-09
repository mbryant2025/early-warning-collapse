import numpy as np

#Returns a list representing the moving averages of the inputted data
def findMovingAverages(data, timescale = 2):
    averages = []
    for i in range(len(data)):
        if i == 0:
            averages.append(np.average(data[0]))
        elif i < timescale:
            averages.append(np.average(data[:i + 1]))
        else:
            averages.append(np.average(data[i - timescale + 1:i + 1]))

    return averages
