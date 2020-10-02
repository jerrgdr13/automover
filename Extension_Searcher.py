import os
import json

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
        ext_name=str(e.split('.')[1])
        print(file_name)
        print(ext_name)
    #print(f"file name{e} and the extension is {e.split('.')[1]}")


#def  ext_validator():
#    for i in range(len(ext_lst)):
#        print(i)