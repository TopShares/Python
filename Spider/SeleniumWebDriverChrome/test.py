
import myPyMongodb

db = myPyMongodb.myMongodb(host='127.0.0.1',port=27017,database='my_database',collection='my_collection')
db.insert_data_many([{'name': 'amy', 'id': 1798},{'name': 'bob', 'id': 1631}])

