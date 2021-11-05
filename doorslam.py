# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 13:52:06 2021

@author: brady
"""
import numpy as np 
import matplotlib.pyplot as plt
def builddisp(avg, peak):
    array = []
    while len(array) < 150:
        z = np.random.randint(1,11)
        if z == 5:
            array += [int(np.random.randint(-1,2)*peak)]
        else:
            array += [int(np.random.uniform(-1,2)*avg)]
    return array


arrx = list(range(150))

fig = plt.figure(num = 1, clear = True)
ax = fig.add_subplot(1,1,1)

ax.plot(arrx, builddisp(20,60))
