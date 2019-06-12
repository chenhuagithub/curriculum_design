import tkinter
from chenhua import fuction
import os

root=tkinter.Tk() #生成root主窗口
root.geometry('450x350')
label=tkinter.Label(root,text='操作系统课程设计') #生成标签
label.pack()        #将标签添加到主窗口

# 操作文件的目录
path='/home/chenhua/文档/chenhua/'
path.capitalize()

def printkey(event):
    # 获取文域的内容
    bbb = text.get('0.0', 'end')
    print('bbb--->',bbb)
    # 对文本域的内容进行切割
    lis=bbb.split('\n')

    # 获取最后一条指令
    command=lis[-2]


    # 展现目录
    if command.strip() == 'dir':
        index = 1
        aaa = fuction.inser_file(path)
        for x in aaa:
            if index==1:
                text.insert('end','\n'+x)
                if os.path.isdir(path+x):
                    text.insert('end','--------------- 文件夹\n')
                elif os.path.isfile(path+x):
                    text.insert('end','--------------- 文件\n')
                index=index+1
            else:
                text.insert('end',x)
                if os.path.isdir(path+x):
                    text.insert('end','--------------- 文件夹\n')
                elif os.path.isfile(path+x):
                    text.insert('end','--------------- 文件\n')

    # 建立文件夹
    elif command.startswith('mkfile'):
        # 分割指令
        command_arr=command.split(' ')
        if command_arr[1] == '-f':
            # 获取文件夹名字
            folder_name=command_arr[-1]
            print(folder_name)
            # 调用创建文件夹的函数
            fuction.create_folder(path,folder_name)
            text.insert('end','\n文件夹'+folder_name+'创建成功\n')
        elif command_arr[1] == '-d':
            # 获取文件名字
            file_name=command_arr[-1]
            # 调用创建文件的函数
            fuction.create_file(path,file_name)
            text.insert('end','\n文件'+r'"'+file_name+r'"'+'创建成功\n')
        else:
            text.insert('end','\n指令错误\n')

    # 显示文件内容
    elif command.startswith('type'):
        command_arr=command.split(' ')
        # 获取文件名字
        file_name=command_arr[-1]
        # 调用展现文件内容的函数
        type_content=fuction.show_file(path,file_name)
        text.insert('end','\n\n'+type_content)

    # 复制文件或文件夹
    elif command.startswith('copy'):
        command_arr=command.split(' ')
        print(command_arr)
        if command_arr[1] == '-f':
            sourcefile_name=command_arr[-2]
            destition_name=command_arr[-1]
            # 复制文件夹
            fuction.copy_folders(path,sourcefile_name,path,destition_name)
            text.insert('end','\n文件夹复制成功\n')

        elif command_arr[1] == '-d':

            sourcefile_name=command_arr[-2]
            destition_name=command_arr[-1]
            fuction.copy_folder(path,sourcefile_name,path,destition_name)
            text.insert('end','\n文件复制成功\n')

        else:
            text.insert('end','\n指令错误\n')

    # 删除文件或文件夹
    elif command.startswith('delfile'):
        command_arr=command.split(' ')
        #删除文件夹
        if command_arr[1] == '-f':
            folder_name=command_arr[-1]
            try:
                fuction.delete_folder(path,folder_name)
                text.insert('end', '\n文件夹' + folder_name + '删除成功\n')
            except:
              text.insert('end','\n无文件夹'+folder_name+'\n')


        # 删除文件
        elif command_arr[1] == '-d':
            file_name=command_arr[-1]
            try:
                fuction.delete_file(path,file_name)
                text.insert('end', '\n文件' + file_name + '删除成功\n')
            except:
                text.insert('end','\n无文件'+file_name+'\n')
        else:
            text.insert('end','\n指令错误\n')

    elif command.strip() == 'clear':
        text.delete('1.0','end')

    else:
        text.insert('end','\n指令错误,请注意检查指令\n')


# 设置窗口的宽度
text=tkinter.Text(root,width=100,borderwidth=10)
# 把Text添加到窗口中
text.pack()
# 设置回车键绑定事件
text.bind('<Return>',printkey)
# 进入消息循环（必需组件）
root.mainloop()

