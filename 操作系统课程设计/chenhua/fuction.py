import os
import shutil

# 获取目录列表
def inser_file(path):
    aaa=os.listdir(path)
    return aaa


#创建文件夹
def create_folder(path,name):
    os.mkdir(path+name)
    return name


# 创建文件
def create_file(path,name):
    with open(path+name,'w') as f:
        pass


# 删除文件夹
def delete_folder(path,name):
    shutil.rmtree(path+name)
    return name


# 删除文件
def delete_file(path,name):
    os.remove(path+name)
    return name


# 复制文件
def copy_folder(path1,name1,path2,name2):
    shutil.copy(path1+name1,path2+name2)
    return name2



# 复制文件夹
def copy_folders(path1,name1,path2,name2):
    shutil.copytree(path1+name1,path2+name2)
    return name2

# 展示文件内容
def show_file(path,name):
    with open(path+name,'r') as f:
        content=f.read()
    return content