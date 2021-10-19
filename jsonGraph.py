# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
import numpy as np

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
    a = (aList["ESP1"]["FlexSensor"])
    b = (aList["ESP1"]["TiltSensor"])
    l1 = list(a.items())
    l2 = list(b.items())
    print(l1)
    print(a)
    print(aList)
    for k in range(len(l1)):
        arr += [k]
        arry += [l1[k][1]]
    for k in range(len(l2)):
        arrx1 += [k]
        arry1 += [l2[k][1]]
    plt.plot(arr,arry, colors[counter] + pointStyles[counter])
    counter += 1
    plt.plot(arrx1,arry1, colors[counter] + pointStyles[counter])

