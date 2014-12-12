import os
from PIL import Image

for letter in os.listdir('change/'):
	im = Image.open('change/%s'%letter)
	im = im.crop((1,0,9,50))
	print im.size[0]
	print im.size[1]
	print
	im.save('change/%s'%letter)