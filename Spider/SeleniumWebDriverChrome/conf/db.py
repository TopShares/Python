# -*- coding: utf-8 -*-
# @Author  : XerCis
# @Time    : 2019/11/21 15:53
# @Function: pymongo库的封装


import pymongo


class MongoDB:
    def __init__(self, uri='mongodb://localhost:27017/', db='test', collection='test'):
        """初始化MongoDB数据库和表的信息并连接数据库

        :param uri: 连接名
        :param db: 数据库名
        :param collection: 表名
        """
        client = pymongo.MongoClient(uri)
        self.db = client[db]  # 数据库
        self.collection = self.db[collection]  # 表

        if db not in client.list_database_names():
            print("数据库不存在！")
        if collection not in self.db.list_collection_names():
            print("表不存在！")

    def __str__(self):
        """数据库基本信息"""
        db = self.db._Database__name
        collection = self.collection._Collection__name
        num = self.collection.count_documents({})
        return "数据库{} 表{} 共{}条数据".format(db, collection, num)

    def __len__(self):
        """表的数据条数"""
        return self.collection.find().count()

    def count(self):
        """表的数据条数"""
        return len(self)

    def insert(self, *args, **kwargs):
        """插入多条数据
        
        :param args: 多条数据，可以是dict、dict的list或dict的tuple
        :param kwargs: 单条数据，如name=XerCis, gender=male
        :return: 添加的数据在库中的_id
        """
        documents = []
        for i in args:
            if isinstance(i, dict):
                documents.append(i)
            else:
                documents += [x for x in i]
        documents.append(kwargs)
        return self.collection.insert_many(documents)

    def delete(self, *args, **kwargs):
        """删除一批数据
        
        :param args: 字典类型，如{"gender": "male"}
        :param kwargs: 直接指定，如gender="male"
        :return: 已删除条数
        """
        # TODO(XerCis) 增加正则表达式
        list(map(kwargs.update, args))
        result = self.collection.delete_many(kwargs)
        return result.deleted_count

    def drop(self):
        '''
        数据库删除
        '''
        self.collection.drop()

    def remove(self):
        '''
        表清空
        '''
        self.collection.remove();
    def update(self, *args, **kwargs):
        """更新一批数据
        
        :param args: dict类型的固定查询条件如{"author":"XerCis"}，循环查询条件一般为_id列表如[{'_id': ObjectId('1')}, {'_id': ObjectId('2')}]
        :param kwargs: 要修改的值，如country="China", age=22
        :return: 修改成功的条数
        """
        value = {"$set": kwargs}
        query = {}
        n = 0
        list(map(query.update, list(filter(lambda x: isinstance(x, dict), args))))  # 固定查询条件
        for i in args:
            if not isinstance(i, dict):
                for id in i:
                    query.update(id)
                    result = self.collection.update_one(query, value)
                    n += result.modified_count
        result = self.collection.update_many(query, value)
        return n + result.modified_count

    def find(self, *args, **kwargs):
        """保留原接口"""
        return self.collection.find(*args, **kwargs)

    def find_all(self, show_id=False):
        """所有查询结果
        
        :param show_id: 是否显示_id，默认不显示
        :return:所有查询结果
        """
        if show_id == False:
            return [i for i in self.collection.find({}, {"_id": 0})]
        else:
            return [i for i in self.collection.find({})]

    def find_col(self, *args, **kwargs):
        """查找某一列数据
        
        :param key: 某些字段，如"name","age"
        :param value: 某些字段匹配，如gender="male"
        :return:
        """
        key_dict = {"_id": 0}  # 不显示_id
        key_dict.update({i: 1 for i in args})
        return [i for i in self.collection.find(kwargs, key_dict)]


if __name__ == '__main__':
    """连接"""
    # 常量定义
    uri = "mongodb://localhost:27017/"
    db = "MyDB"
    collection = "test"
    mongodb = MongoDB(uri, db, collection)  # 连接数据库
    print(mongodb)  # 基本信息

    """增"""
    mongodb.insert(author="XerCis", gender="male")  # 插入一条数据
    mongodb.insert({"country": "China"})  # 插入一条数据，dict
    mongodb.insert([{"country": "Japan"}, {"country": "Korea"}])  # 插入一批数据，dict的list
    result = mongodb.insert(({"country": "American"}, {"country": "Australia"}))  # 插入一批数据，dict的tuple
    # mongodb.insert({"country": "China"}, [{"country": "Japan"}, {"country": "Korea"}], country="American")# 多类型传参
    print(result.inserted_ids)  # 添加的数据在库中的_id
    print(len(mongodb))  # 表的数据条数
    print(mongodb.find_all())  # 所有查询结果

    """删"""
    print(mongodb.delete(country="Japan"))  # 删除国家为日本的所有记录
    print(mongodb.delete(country={"$regex": "^A"}))  # 删除国家开头为A的所有记录
    # print(mongodb.delete({"country": {"$regex": "^A"}}))#效果同上

    """改"""
    id = mongodb.find_col("_id")  # 查询所有_id
    print(id)
    print(mongodb.update(id, {"author": "XerCis"}, country="China", age=22, height=178))
    print(mongodb.find_col(author="XerCis"))

    """查"""
    print(mongodb.find_all(show_id=True))  # 所有查询结果，包含_id
    print(mongodb.find_col("_id", "author", "gender", author="XerCis"))  # 显示author、gender，且author为XerCis

