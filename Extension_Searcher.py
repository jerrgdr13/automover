import os

path = '/Users/jguerrad/Downloads/'

l = os.listdir(path)
def check_type():
    for e in l:
        split_ext = e.split('.')[1]
        filename = e.split('.')[0]
        print(f'the file name is {filename} with the extension {split_ext}')





check_type()
