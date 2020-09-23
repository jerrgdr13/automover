import os

path = '/Users/jguerrad/Downloads/'

l = os.listdir(path)
for e in l:
    print(e)

for root, dirs, files in os.walk('/Users/jguerrad/Downloads/'):
    for file in files:
        if file.endswith('.*'):
            print(os.path.join(root, file))
