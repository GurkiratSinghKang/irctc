from PIL import Image
import os
import ImageChops
import math, operator
first_pixel=0

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    pixels_image1 = im1.load()
    pixels_image2 = im2.load()
    pixel_match=0
    total_pixel=0
    for x in xrange(im1.size[0]):
    	for y in xrange(im1.size[1]):
    		if (pixels_image2[x,y][3]!=0):
    		              total_pixel +=1
    		              if(pixels_image1[x,y][3]!=0):
    				pixel_match+=1
    			
    # calculate rms
    if (total_pixel!=0):
    	return (math.sqrt(float(float(pixel_match)/float(total_pixel))))
    	
    #return math.sqrt(reduce(operator.add,map(lambda h: h**2, h) / (float(im1.size[0]) * im1.size[1]))

captcha = Image.open('img96.png')
pixels = captcha.load()
iconset = [('x',15)]

def calculate_next(first):
	for x in xrange(first+1,170):
		for y in xrange(50):
			if (pixels[x,y][3]>20):
				return x



max=0
final=[]

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

  		



  
  