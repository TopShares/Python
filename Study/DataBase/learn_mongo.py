from pymongo import MongoClient

client = MongoClient()
db = client.test # 连接test数据库，没有则自动创建
my_set = db.set  # 使用set集合，没有则自动创建
my_set.insert({
    "nmae":"yyyy",
    "age":18
})