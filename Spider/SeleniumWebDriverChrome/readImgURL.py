from conf.config import config

c = config()


mongodb = c.mongodb

a = mongodb.find_col("ImageUrl")
with open('data.txt', 'a', encoding="utf-8") as f:
    for i in a:
        for ii in i['ImageUrl']:
            print(ii)
            f.write(ii + '\n')
