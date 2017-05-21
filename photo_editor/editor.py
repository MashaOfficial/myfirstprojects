# -*- coding: utf-8 -*-

# --- Photo editor ---

from PIL import Image
import os, sys


im = Image.open("picture.ppm")

# >>> print(im.format, im.size, im.mode) -> PNG (250, 188) RGB
# im.show()


def convert_to_jpg(im):
    f, e = os.path.splitext(im)
    outfile = f + ".jpg"
    if im != outfile:
        try:
            Image.open(infile).save(outfile)
            return Image
        except IOError:
            print("cannot convert", im)




