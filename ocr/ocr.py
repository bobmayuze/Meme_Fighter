# coding:utf-8
import urllib, urllib2, base64
import ssl
import json


access_token = '24.9b879e0aca90b2d002e5c1ca5e2940d1.2592000.1503298306.282335-9919943'
ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token


# Return the first group of words recognized out
def pic2words(file_content):
  img = base64.b64encode(file_content)

  params = {"image": img}
  params = urllib.urlencode(params)

  try:
    request = urllib2.Request(ocr_url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
      print(content)
      return json.loads(content)['words_result'][0]['words']
    return ''
  except Exception as err:
    print('Runtime error: ', err)
    return ''


# First group of words from picture URI
def picurl2words(pic_url):
  content = urllib.urlopen(pic_url).read()
  return pic2words(content)

# First group of words from local picture name
def picpath2words(pic_path):
  content = open(pic_path, 'rb').read()
  return pic2words(content)

