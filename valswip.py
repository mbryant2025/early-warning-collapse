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
def generate(sensors, timeAvg = 1, timeTotal = 3):
    timeT = 0
    ArrSens = np.zeros(sensors, dtype = int)
    DataArr = np.array(ArrSens)
    print(ArrSens)
    ax.legend(loc='best')
    while timeT < timeTotal:
        for i in range(sensors):
            ArrSens[i] += int(np.random.randint(-5,6))
        print('Time:', timeAvg*timeT, ArrSens) 
        timeT += timeAvg
        DataArr = np.append(DataArr,ArrSens)
    DataArr = (list(DataArr))
    print('dataArr',DataArr)
    counter = 1
    for each in range(1,len(DataArr)):
        colorCode = labels[int(each % sensors)]
        lCode = 'Sensor' + str(each)
        plt.scatter(counter,DataArr[each], c = colorCode, label = lCode)
        if each % sensors == 0:
            counter += 1
    for each in range(1,sensors):
        if dataArr[each] ==
labels = {
    0 : 'k',
    1 : 'b',
    2 : 'r',
    3 : 'y',
    4 : 'k',
    5 : 'b',
    6 : 'r'
    }
    
'''
fig.tight_layout()
        ax.plot(timeT, ArrSens[0], 'ko', label = 'Sensor 1')
        ax.plot(timeT, ArrSens[1], 'bo', label = 'Sensor 2')
        ax.plot(timeT, (ArrSens[0]+ArrSens[1])/sensors, 'yx', label = 'Averages')
        

'''
print(generate(4, 1, 10))