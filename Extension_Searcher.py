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
    if e.split('.')[1] == True:
        print(str(e.split('.')[1]))
        print(str(e.split('.')[0]))
        #print(file_name)
        #print(ext_file)
    #print(f"file name{e} and the extension is {e.split('.')[1]}")


#def  ext_validator():
#    for i in range(len(ext_lst)):
#        print(i)