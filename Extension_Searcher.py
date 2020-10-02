import os
import json

#read Json file
myjsonfile=open('./information.json','r')
jsondata=myjsonfile.read()

#parse Json
obj=json.load(jsondata)
print(str(obj['Origin_Path'])