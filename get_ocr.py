# coding:utf-8
import urllib, urllib2, base64
import ssl
import json


access_token = '24.9b879e0aca90b2d002e5c1ca5e2940d1.2592000.1503298306.282335-9919943'
ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token


def pic2words(file_content):
  img = base64.b64encode(file_content)

  print img

  params = {"image": img}
  params = urllib.urlencode(params)
  request = urllib2.Request(ocr_url, params)
  request.add_header('Content-Type', 'application/x-www-form-urlencoded')
  response = urllib2.urlopen(request)
  content = response.read()
  if (content):
      print(content)
  json.loads(content)['words_result'][0]['words']


#image = open(r'/home/xing/Pictures/ocr3.jpg', 'rb').read()
#pic2words(image)
