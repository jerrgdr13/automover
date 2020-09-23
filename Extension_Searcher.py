import os

path = '/Users/jguerrad/Downloads/'

l = os.listdir(path)
def check_type(l):
    for e in l:
         print(e.split('.'))
        #print(ffiles)
