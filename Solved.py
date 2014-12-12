from PIL import Image
import os
import ImageChops
import math, operator
first_pixel=0

def similar(im1, im2):
    "Calculate the root-mean-square difference between two images"
    pixels_image1 = im1.load()
    pixels_image2 = im2.load()
    pixel_match=0
    total_pixel=0
    for x in xrange(im1.size[0]):
    	for y in xrange(im1.size[1]):
            if (pixels_image2[x,y][3]>220):
                if(pixels_image1[x,y][3]>220):
                    pixel_match+=1
                total_pixel +=1
            if (pixels_image1[x,y][3]>220):
                if(pixels_image2[x,y][3]>220):
                    pixel_match+=1
                total_pixel +=1
    '''print 'pixels:',pixel_match,total_pixel'''	
    # calculate rms
    if (total_pixel!=0):
    	return ((float(pixel_match)/float(total_pixel)))
    	
    #return math.sqrt(reduce(operator.add,map(lambda h: h**2, h) / (float(im1.size[0]) * im1.size[1]))

captcha = Image.open('img82.png')
pixels = captcha.load()
iconset = ['3','4','6','8','A','B','C','D','E','F','G','H','K','M','P','Q','R','S','T','U','X','Y','Z']
max=0
def calculate_next(first):
	for x in xrange(first+1,170):
		for y in xrange(50):
			if (pixels[x,y][3]>220):
				return x
first = calculate_next(0)
for i in xrange(first,170):
    captcha_letter = captcha.crop((i,0,i+10,50))
    for img in os.listdir('cleaned/Database.png'):
                    check_letter = Image.open('cleaned/Database.png/%s'%(img))
                    similarity = similar(captcha_letter,check_letter)
                    if(max>similarity):
                                    max=similarity
                                    maxletter=letter
                    if(similarity>0.95):
                        captcha_letter1 = captcha.crop((i,0,i+10,50))
                        captcha_letter1.save('captcha_letter%s.png'%i)
                        print similarity
                        print img ,i, i+10




'''
first_pixel = calculate_next(first_pixel)
for letter,width in iconset:
            for img in os.listdir('database/'):
                            check_letter = Image.open('database/%s.png'%(letter))
                            check_letter.save('letter.png')
                            captcha_letter = captcha.crop((first_pixel,0,first_pixel+width,50))
                            captcha_letter.save('captcha_letter.png')
                            rms = rmsdiff(captcha_letter,check_letter)
                            if(max>rms):
                                            max=rms
                                            maxletter=letter
                            print rms
                            print letter
'''
  		



  
  