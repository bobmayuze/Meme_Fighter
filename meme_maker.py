#!/usr/bin/env python
#coding: utf-8
import PIL
from PIL import ImageFont, Image, ImageDraw
import random 
import os

def get_meme():
	font = ImageFont.truetype("/Users/user/Documents/Projects/Ultra_wechat/chinese_font.ttf", 22)
	
	# img = Image.open("p.png")
	img = Image.open("./source/anger/" + random.choice(os.listdir("./source/anger")))
	# Find out the height and width of the target pic
	width = img.size[0]
	height = img.size[1]
	msg_l = ["上车么骚年","上车吧骚年","那你很棒哦","放学后别走","编程猫听过么", "阿不就好棒棒","大佬大佬","社会社会"]
	index = random.randint(0,len(msg_l)-1)

	msg = msg_l[index]
	dummy_msg = len(msg) * "**"


	draw = ImageDraw.Draw(img)
	tw, th = draw.textsize(dummy_msg)
	draw.text(((width-tw)*0.4, height* 0.8),msg,(0,0,0),font=font)
	img.save("out.png")

def get_meme_by_emotion(emotion):
	img_dir = "./source"

	img = Image.open("./source/anger/" + random.choice(os.listdir("./source/anger")))
	return "并不想理你，并向你扔了一只旋转狗"

