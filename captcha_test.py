from PIL import Image
i=432
lett = 'r'
start = 13
window = 8
im = Image.open("captchas/img"+str(i)+".png") #Can be many different formats.

z = (0,0,0,0)
noz = (255,255,255,0)

'''pix = im.load()
for x in xrange(170):
	for y in xrange(50):
		if (pix[x,y][3]>20):
			startx = x
			starty = y
			break
	else:
		continue
	break'''
im = im.crop((start,0,start+window,50))

im.save("database/%s.png"%lett)
#pix[x,y] = value # Set the RGBA Value of the image (tuple)