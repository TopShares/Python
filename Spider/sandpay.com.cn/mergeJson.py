import json
import os
dct1 = {'reverse0': [('609L', 4.585), ('615L', 4.285), ('966L', 3.585)]}
dct2 = {'reverse1': [('619L', 3.185), ('625L', 4.655), ('936L', 1.585)]}
# print(type(dct1))
# tmp = dict(dct1, **dct2)
# print(tmp)

def mergeDict(dict1, dict2):
    if dict1 and dict2:
        return dict(dict1, **dict2)
    else:
        return dict1


oldJson, newJson = {}, {}
n = 1
for parent, dirnames, filenames in os.walk('./data/'):
    for filepath in filenames:
        
        path ='./data/'+filepath
        with open(path, 'r', encoding='utf-8') as f:
            data = f.readlines()
            if not oldJson:
                oldJson = json.loads(data[0])
            else:
                newJson = json.loads(data[0])
            print(oldJson)
            print('-'*50)
            oldJson = mergeDict(oldJson,newJson)
        if n==2:
            print(oldJson)
            exit()

        n+=1

# n = '233'
# s = n.zfill(5)
# print(s)