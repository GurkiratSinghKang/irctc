import shutil
import requests

for i in xrange(500):
	url = 'https://www.irctc.co.in/eticketing/captchaImage'
	response = requests.get(url, stream=True)
	with open('captcha_jpg/img'+str(i)+'.jpg', 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response