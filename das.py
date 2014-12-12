import ImageChops
import math, operator
from PIL import Image

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2)
    h.save('lel.png')

   

im1 = Image.open('im.png')
im2 = Image.open('img1.png')

rmsdiff(im1,im2)