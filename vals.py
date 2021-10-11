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
    ArrSens = np.zeros(sensors)
    print(ArrSens)
    ax.legend(loc='best')
    while timeT < timeTotal:
        for i in range(sensors):
            ArrSens[i] += np.random.randint(-2,3)
        print('Time:', timeAvg*timeT, ArrSens) 
        ax.plot(timeT, ArrSens[0], 'ko', label = 'Sensor 1')
        ax.plot(timeT, ArrSens[1], 'bo', label = 'Sensor 2')
        ax.plot(timeT, (ArrSens[0]+ArrSens[1])/sensors, 'yx', label = 'Averages')
        timeT += timeAvg
    return ArrSens
fig.tight_layout()
print(generate(2, .01, 10))
