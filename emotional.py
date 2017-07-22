#!/usr/bin/env python
#coding: utf-8
import http.client 
import urllib.request 
import urllib.parse
import urllib.error
import base64
import sys
import json
headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '7f66b586c9d949f1b1994adb5e37d5eb',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://1.bp.blogspot.com/-FAjLTRtXwI8/VtljUoDMOuI/AAAAAAAAAb4/LvkuZYV-WqA/s1600/smile1.jpg' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    string_d = data.decode("utf-8")
    json_obj = json.loads(string_d)
    print(data)
    conn.close()
except Exception as e:
    print(e.args)


def get_emotion_from_img(img_url):
    body = "{ 'url': '"+img_url+"' }"
    print(body)
    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
        #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        string_d = data.decode("utf-8")
        json_obj = json.loads(string_d)
        conn.close()
        return json_obj[0]['scores']
    except Exception as e:
        print(e.args)
        return "网络貌似不太好，等下再试试吧"