from runAR import runModelFromArray
import csv
import numpy as np

with open('testDataset.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[1:]
data = [float(x[1]) for x in data]

predictions = []
for i in range(len(data) - 2):
    slice = data[i:i+2]
    predictions.append(runModelFromArray(slice, "model_fit.obj"))

errors = []
data = data[2:]

for i in range(len(predictions)):
    errors.append(abs(predictions[i] - data[i]) / data[i])

print("Accuracy test on " + str(len(predictions)) + " data points:")
print(str(100 * np.average(errors)) + "%")