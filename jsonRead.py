# -*- coding: utf-8 -*-

import json

fileObject = open("data.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)
print(aList)