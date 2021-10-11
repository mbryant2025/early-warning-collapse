from random import randrange
import matplotlib.pyplot as plt 
import numpy as np

def walk(total):
    pos = 0
    iteration = 0
    poslist = []
    xlist = []
    while iteration < total:
        pos += randrange(-1,2,1)
        poslist += [pos]
        xlist += [iteration]
        iteration += 1
    return [xlist], [poslist]
    
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.linspace(0,101,100), walk(100)[1], "ko")

    



    

