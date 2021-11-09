from MA import findMovingAverages
from ARfromJSON import loadData
from matplotlib import pyplot as plt

def graph(file, sensorUnit, sensor):
    data = loadData(file, sensorUnit, sensor)
    ma = findMovingAverages(data)
    plt.plot(ma)
    plt.show()

