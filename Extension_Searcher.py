import os
import json

#read Json file
myjsonfile=open('./information.json','r')
jsondata=myjsonfile.read()

#parse Json
obj=json.loads(jsondata)
#print(str(obj['Origin_Path']))

org_path=str(obj['Origin_Path']) 
l = os.listdir(org_path)
for e in l:
    print(e)