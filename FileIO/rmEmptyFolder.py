#目标：删除所有空文件夹
#逐个判断某目录下所有项目
#若该项目是目录就进入该目录，完成上一步，不是下一个项目
#判断完所有后判断当前目录是否是空目录，是就删除
#需要管理员权限，否则很多目录无权限
#慎用
import os

def delete_gap_dir(dir):
    if  os.path.isdir(dir):
        for item in os.listdir(dir):
            if item!='System Volume Information':#windows下没权限删除的目录：可在此添加更多不判断的目录
                delete_gap_dir(os.path.join(dir, item))

        if not os.listdir(dir):
            os.rmdir(dir)
            print("移除空目录：" + dir)


delete_gap_dir(r'F:\3D')