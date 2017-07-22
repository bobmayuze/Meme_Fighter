from wxpy import *
from meme_maker import *
from emotional import *
import requests
import time
import json
import re


# Init the env, login
bot = Bot()
print("========INIT SUCCESSFULLY=====")
frs = bot.friends()
dummy = ''
yuze = bot.friends().search('Yuze Ma 鱼哲')[0]
apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
	"key": "c306b319ca4541d78a6413ccc16c8119",
	"info": "你好呀",
	"userid":"123"
}
dummy_dict = dict()

# @bot.register()
# def just_print(msg):
#     print("GET: \n",msg)



@bot.register(Group, TEXT)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        # print(msg.raw)
        # data["info"] = msg.text
        # try:
        #     time.sleep(1200)
        #     res = requests.post(apiUrl, data = data).json()
        #     return res["text"]
        # except:    
        #     return "你说什么我听不见！"
        print("==EXECUTRED==")
        get_meme()
        msg.sender.send_image("out.png")
        return
    else:
        # 回复消息内容和类型
        try:
            print("==EXECUTRED==")
            get_meme()
            msg.sender.send_image("out.png")
            return "lolol"
            # data["info"] = msg.text
            # res = requests.post(apiUrl, data = data).json()
            # return res["text"]
        except:
            return "Connection lost"

@bot.register(bot.friends(), PICTURE)
def auto_reply(msg):
    print(msg.raw)
    # print (json.dumps(msg.raw, indent=4, sort_keys=True))
    raw_content = msg.raw['Content']
    url = re.findall("cdnurl=(.*) des",raw_content, re.S)
    real_url = re.findall("\"(.*)\"",url[0], re.S)[0]
    print("=================================")
    emotional_data = get_emotion_from_img(real_url)
    print(emotional_data)
    # print(msg.raw['Content'])
    # return "我还看不懂这个图呢"
    msg.sender.send_image("new.gif")
    return emotional_data

@bot.register(bot.friends(), TEXT)
def auto_r(msg):
    print(">>>>>>>>>>>>>>>GET: \n",msg.raw)
    try:
        print("==EXECUTRED==")
        get_meme()
        msg.sender.send_image("out.png")
        return 
    except:
        print("photo cannot successfully load")
        return "23333"

