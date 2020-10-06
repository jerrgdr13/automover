#Importing OS to work with the directories and JSON to store paths and avoid hardcoded information.
import os
import json

#read Json file
myjsonfile=open('./information.json','r')
jsondata=myjsonfile.read()

#parse Json
obj=json.loads(jsondata)
#print(str(obj['origin_path']))

#Transform JSON data in to variables.
org_path=str(obj['origin_path'])
dst_path=str(obj['dest_path']) 
#l = os.listdir(org_path)

#This function will move the information
def move_files(source_folder, dest_folder):
    try:
        for path, dir, files in os.walk(source_folder):
            if files:
                for file in files:
                    if not os.path.isfile(dest_folder + file):
                        os.rename(path + '/' + file, dest_folder + file)
        print('All Files have been moved')
    except Exception as e:
        print(e)

#Calling the function.
move_files(org_path,dst_path)