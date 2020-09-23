import os

for root, dirs, files in os.walk('/Users/jguerrad/Downloads/'):
    for file in files:
        if file.endswith('.dmg'):
            print(os.path.join(root, file))
