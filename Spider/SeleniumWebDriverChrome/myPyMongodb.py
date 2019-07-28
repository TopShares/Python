import pymongo

class myMongodb:
    def __init__(self, host, port, database, collection):
        # 生成pymongo对象,传入连接服务器相关参数 ip 端口
        # 如果使用指定的账户登录，设置要登录的账户和密码
        self.mongo_client = pymongo.MongoClient(
            host='127.0.0.1',
            port=27017,
            # username="admin",
            # password="123456"
        )

        # 选择连接的数据库  创建数据库，类似字典引用
        self.mongo_db = self.mongo_client[database]

        # 创建collection
        self.collection = self.mongo_db[collection]

    def insert_data_many(self, oList):
        self.collection.insert_many(oList)
# dic = {'name':'serena',"id":1532}
# collection.insert_one(dic)


# #插入多条文档，可以传入list of dict, 即一个字典的列表，每个元素是一条记录，然后用insert_many()

# list_of_records = [{'name': 'amy', 'id': 1798},{'name': 'bob', 'id': 1631}]
# collection.insert_many(list_of_records)



# collection.delete_many({'id':1631})


# for record in collection.find():
#     print(record)
if __name__ == "__main__":
    pass