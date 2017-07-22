from pymongo import *


# Init the db config
client = MongoClient("localhost",27017)
db = client.ultra_wechat
collection = db.chat_history

