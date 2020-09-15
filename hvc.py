#!/usr/bin/env python3
""" Encodes video file(s) recursively to HEVC 10Bit video. """

from glob import glob

__author__ = "Madhusudhan D Desai"
__copyright__ = "Copyright 2020, mddnix"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Madhusudhan D Desai"
__email__ = "mddnix@gmail.com"
__status__ = "Production"

extn = ('*.mp4', '*.pdf')
files = []

for file in extn:
    files.extend(glob("**/*" + file, recursive = True))

#print(files)
for i in files:
    print(i)
