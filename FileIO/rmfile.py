# coding: utf-8
import os
import shutil
CUR_PATH = r'C:\Users\Administrator.DESKTOP-EFGKLOP\Desktop\2'
shutil.rmtree(CUR_PATH)
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

# del_file(CUR_PATH)