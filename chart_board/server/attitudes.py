#!/usr/bin/env python
#coding: utf-8
import urllib, sys
import ssl
import json
import urllib.request
import http.client

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=LYwDqiaVeoTBk6OlTrmwzSDs&client_secret=yjDD5jpY0kMgRDa86N9NrzyfUOqErpbv'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()

string_c = content.decode("utf-8")
json_obj = json.loads(string_c)
tokenjson = json_obj["access_token"]
#print(tokenjson + "\n")



headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json; charset=UTF-8',
}

params = urllib.parse.urlencode({
	'access_token': tokenjson
})


#body = "{ \"text\": \"我现在很生气！我很愤怒！我要砍人\" }".encode('GBK')

#0 error  1 pos 2 neg 3 neutral
def getattitudeFrom(text):
  try:
      conn = http.client.HTTPSConnection('aip.baidubce.com')
      body = "{ \"text\": \"" + text + "\" }"
      conn.request("POST", "/rpc/2.0/nlp/v1/sentiment_classify?%s" % params, body.encode('GBK'), headers)
      response = conn.getresponse()
      data = response.read()
      string_d = data.decode("GBK")
      json_obj = json.loads(string_d)

      #print(json_obj)
      #print(json_obj["items"][0]["confidence"])
      #print(json_obj["items"][0]["positive_prob"])
      conn.close()

      if json_obj["items"][0]["confidence"] < 0.4:  
        return 0
        # positive_prob  ~ ... 0.45 ... 0.55
      if json_obj["items"][0]["positive_prob"] < 0.45:
        return 2
      elif json_obj["items"][0]["positive_prob"] < 0.55:
        return 3
      else:
        return 1

  except Exception as e:
      print(e.args)
      # return 0