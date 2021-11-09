import json

def loadData(file, sensorUnit, sensor):
    fileObject = open(file, "r")
    jsonContent = fileObject.read()
    load = json.loads(jsonContent)
    logs = (load[sensorUnit][sensor])
    readings = list(logs.values())
    return readings
