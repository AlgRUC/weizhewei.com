import os, sys
from PIL import Image 

size = 400, 400

file_paths = os.listdir(".")

for infile in file_paths:
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(infile, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)
