#!/usr/bin/env python
#coding: utf-8
import PIL
from PIL import ImageFont, Image, ImageDraw
import random 
import os
import operator

def random_line(file_name):
	afile = open(file_name)
	line = next(afile)
	for num, aline in enumerate(afile):
		if random.randrange(num + 2): continue
		line = aline
	return line

def get_meme():
	font = ImageFont.truetype("./chinese_font.ttf", 18)
	emotion_l = ["anger","contempt","disgust","fear","happiness","neutrual","sadness","surprise"]
	major_emotion = random.choice(emotion_l)
	print("Emotion mode is on ===>", major_emotion)
	# img = Image.open("p.png")
	img = Image.open("./source_img/"+major_emotion+"/" + random.choice(os.listdir("./source_img/"+major_emotion)))
	file = "./source_text/" + major_emotion + "/text.txt"
	# Find out the height and width of the target pic
	width = img.size[0]
	height = img.size[1]
	# msg_l = ["上车么骚年","上车吧骚年","那你很棒哦","放学后别走","编程猫听过么", "阿不就好棒棒","大佬大佬","社会社会"]
	# index = random.randint(0,len(msg_l)-1)


	msg = random_line(file)
	dummy_msg = len(msg) * "**"


	draw = ImageDraw.Draw(img)
	tw, th = draw.textsize(dummy_msg)
	draw.text(((width-tw)*0.15, height* 0.8),msg,(0,0,0),font=font)
	img.save("out.png")

def get_meme_by_emotion(emotion):
	print("GET IMG BY EMOTION ")
	font = ImageFont.truetype("./chinese_font.ttf", 18)
	major_emotion = max(emotion, key=emotion.get) 
	print("Emotion mode is on ===>", major_emotion)

	img = Image.open("./source_img/"+major_emotion+"/" + random.choice(os.listdir("./source_img/"+major_emotion)))
	file = "./source_text/" + major_emotion + "/text.txt"

	width = img.size[0]
	height = img.size[1]

	msg = random_line(file)
	dummy_msg = len(msg) * "**"

	draw = ImageDraw.Draw(img)
	tw, th = draw.textsize(dummy_msg)
	draw.text(((width-tw)*0.15, height* 0.8),msg,(0,0,0),font=font)
	img.save("out.png")	
	# return "并不想理你，并向你扔了一只旋转狗"


# get_meme()