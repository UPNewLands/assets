import os

files = filter(os.path.isfile, os.listdir('.'))
for x in files:
    if x.endswith(".png"): 
        os.rename(x, x.replace("_", "-"))