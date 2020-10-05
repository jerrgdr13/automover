import os
import json
import shutil

#read Json file
myjsonfile=open('./information.json','r')
jsondata=myjsonfile.read()

#parse Json
obj=json.loads(jsondata)
#print(str(obj['origin_path']))

org_path=str(obj['origin_path']) 
l = os.listdir(org_path)
for e in l:
    if str(e.split('.')[0]) in (None,""):
        print('Not a File')
    else:
        file_name=str(e.split('.')[0]),
        ext_name=str(e.split('.')[1]):
        if ext_name == 'pptx':
            shutil.move(dest_path,)