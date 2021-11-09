# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:17:16 2021

@author: brady
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from sigmoid import *

#%% Dictionaries for plotting
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
#%% READ JSON
counter = 0
arrflex = []
arrflexy = []
arrtilt = []
arrtilty = []

fileObject = open("Proto3.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)
flex = (aList["ESP1"]["FlexSensor"])
tilt = (aList["ESP1"]["TiltSensor"])
lflex = list(flex.items())
ltilt = list(tilt.items())
for k in range(len(lflex)):
    arrflex += [k]
    arrflexy += [(lflex[k][1])-3202]
for k in range(len(ltilt)):
    arrtilt += [k]
    arrtilty += [(ltilt[k][1])-3202]
        
#%% MAX ARR

fig = plt.figure(num = 1, clear = True)
ax = fig.add_subplot(1,1,1)
#DEFINE COEFFICIENTS, PLOT MODEL

model = [18,12,9,10,13,12]

simodel = max(model) #used to squeeze variables later

am = len(model) #NUMBER OF VARIABLES

am = (2*np.pi)/am

#%%PLOTTING THE MODEL THRESHOLDS
modely = []

for l in range(len(model)):
    modely += [model[l]*np.sin((am)*l)/simodel]
    model[l] = model[l]*np.cos((am)*l)/simodel
model += [model[0]]
modely += [modely[0]]

ax.plot(model, modely, 'r-' , label = 'threshold')

model23 = np.array(model)/1.66
modely23 = np.array(modely)/1.66
ax.plot(model23, modely23, '.7', linestyle='dashed' )
modelthird = np.array(model)/3
modelythird = np.array(modely)/3
ax.plot(modelthird, modelythird, '.9', linestyle = 'dashed')
ax.grid()

#%%PLOTTING TEST
arrtestflex = arrflexy[0:20]
arrtesttilt = arrtilty[0:20]
radarflex = []
radarflexx = []
#PLOTTING THE FLEX VALUE^
radartilt = []
radartilty = []
rate = 2 #rate of updating chart
#ADD TO COUNTER EACH TIME YOU HAVE A NEW SENSOR METRIC. OTHERWISE JUST COPY AND 
#PASTE THE CODE, CREATING THE NEW TWO LISTS FOR VARIABLES ABOVE.

#while True:
for l in range(1,len(arrflex)):
    arrtestflex += [((arrflexy[l]-arrflexy[l-1])**2)**.5]
    arrtesttilt += [((arrtilty[l]-arrtilty[l-1])**2)**.5]
    

if len(arrtestflex) > rate:
    if max(arrtestflex) > (arrflexy[-1*rate-1] - arrflexy[-1]):
        radarflex = [max(arrtestflex)*np.sin((2*np.pi/am)*counter)/simodel]
        radarflexx = [max(arrtestflex)*np.cos((2*np.pi/am)*counter)/simodel]
        
    else:
        radarflex = [(arrflexy[-rate] - arrflexy[-1]) * np.sin(am*counter)/simodel]
        radarflexx = [(arrflexy[-rate] - arrflexy[-1])*np.cos(am*counter)/simodel]
    arrtestflex = arrtestflex.pop(0)
counter = 1
if len(arrtesttilt) > rate:
    if max(arrtesttilt) > (arrtilty[-1*rate-1] - arrtilty[-1]):
        radartilt = [max(arrtesttilt)*np.sin((am)*counter)/simodel]
        radartiltx = [max(arrtesttilt)*np.cos((am)*counter)/simodel]
        
    else:
        radartilt = [(arrtilty[-rate] - arrtilty[-1]) * np.sin((am)*counter)/simodel]
        radartiltx = [(arrtilty[-rate] - arrtilty[-1])*np.cos((am)*counter)/simodel]
    arrtesttilt = arrtesttilt.pop(0)

ax.scatter(radarflexx,radarflex, label = 'flex')
ax.scatter(radartiltx,radartilt,label = 'tilt')

ax.legend(loc = 'best')

#%%INTEGRATION
temp = model.copy()
temp.extend(model)
tempy = modely.copy()
tempy.extend(modely)
a = 0

#FOR BOUNDARY
for k in range(len(model)):
    a += 1/2*(temp[k]*(tempy[k+1] - tempy[k+2]) + temp[k+1]*(tempy[k+2] - tempy[k]) + temp[k+2]*(tempy[k] - tempy[k+1]))






