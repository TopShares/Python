import os,shutil

path = r'.\result'
# shutil.rmtree(path)

sum = 0
for parent, dirnames, filenames in os.walk(path):
    for filepath in filenames:
        print("rmfile: "+ filepath)
        os.remove(path+ '/'+filepath)
        sum +=1

print("all: " + sum)
