# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:17:16 2021

@author: brady
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from sigmoid import *
colors = {
    0 : 'k',
    1 : 'b',
    2 : 'r',
    3 : 'y',
    4 : 'm',
    5 : 'c',
    6 : 'g'
    }

pointStyles = {
    0 : 'o-',
    1 : 'o-',
    2 : 'o-',
    3 : 'o-',
    4 : 'o-',
    5 : 'o-',
    6 : 'o-'
    }
counter = 0
arr = []
arry = []
arrx1 = []
arry1 = []
if __name__ == '__main__':
    fileObject = open("Proto3.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    flex = (aList["ESP1"]["FlexSensor"])
    tilt = (aList["ESP1"]["TiltSensor"])
    lflex = list(flex.items())
    ltilt = list(tilt.items())
    for k in range(len(lflex)):
        arr += [k]
        arry += [(lflex[k][1]-3202)]
    for k in range(len(ltilt)):
        arrx1 += [k]
        arry1 += [(ltilt[k][1]-3202)]
        
#%% MAX ARR

fig = plt.figure(num = 1, clear = True)
ax = fig.add_subplot(1,1,1)
#DEFINE COEFFICIENTS, PLOT MODEL

model = [18,5,12,14, 13, 12, 11, 11]
modely = []
for l in range(len(model)):
    modely += [model[l]*np.sin((np.pi/4)*l)]
    model[l] = model[l]*np.cos((np.pi/4)*l)
model += [model[0]]
modely += [modely[0]]
ax.plot(model, modely, 'r-' )

model23 = np.array(model)/1.66
modely23 = np.array(modely)/1.66
ax.plot(model23, modely23, '.7', linestyle='dashed' )
modelthird = np.array(model)/3
modelythird = np.array(modely)/3
ax.plot(modelthird, modelythird, '.9', linestyle = 'dashed')
ax.grid()
arrtest = []
radar = []
radarx = []
#while True:
for l in range(1,len(arr)):
    arrtest += [((arry[l]-arry[l-1])**2)**.5]
if len(arrtest) > 5:
    radar = [max(arrtest)*np.sin(90*counter)]
    radarx = [max(arrtest)*np.cos(90*counter)]
    arrtest = arrtest.pop(0)

ax.scatter(radarx,radar)

print(model[1] *np.sin(np.pi/2))



