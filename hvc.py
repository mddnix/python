#!/usr/bin/env python3

import os, glob

extn = ('*.mp4', '*.pdf')
files = []

for file in extn:
    files.extend(glob.glob("**/*" + file, recursive = True))

#print(files)
for i in files:
    print(i)
