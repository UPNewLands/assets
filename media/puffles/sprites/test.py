import os

files = filter(os.path.isfile, os.listdir('.'))
for x in files:
    os.rename(x, x.replace("-", "_"))