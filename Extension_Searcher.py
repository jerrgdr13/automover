#Importing OS to work with the directories and JSON to store paths and avoid hardcoded information.
import os
import json
import shutil

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
    for path, dir, files in os.walk(source_folder):
        if files:
            for file in files:
                destFolder = dest_dir(dst_path)
                shutil.move(file, destFolder)
                print('All Files have been moved')
        else:
            print(e)

    #the following will create the dest_path
    def dest_dir(dest_folder):
            for path, dir, files in os.walk.exists(dest_folder):
                    try:
                        extFile = ext_file(org_path)
                        if not os.path.exists(extFile):
                            os.makedirs(extFile)
                            return dest_folder + '/' + extFile + '%Y-%m-%d %H:%M:%S'
                        else: #os.path.exists(ext_file):
                            dest_dir = dest_folder + '/' + extFile + '%Y-%m-%d %H:%M:%S'
                            return dest_dir
       
        #The following will check the files extension
        def ext_file(source_folder):
            for e in org_path:
                if str(e.split('.')[0]) in (None,""):
                    print('No a File')
                else:
                    return (str(e.split('.')[1]))




#Calling the functions.
move_files(org_path,dest_dir)