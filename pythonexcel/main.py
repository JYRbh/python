#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import webbrowser
from tkinter import*
import os
from tkinter import ttk


root = Tk()
root.geometry('750x400')
#root.geometry('+450+450')
root.title('title')
#root.mainloop()
#root.resizable(1,1)

# 创建一个顶级菜单

tab_main=ttk.Notebook(root)#创建分页栏
tab_main.place(relx=0, rely=0, width=630, height=774)

tab1=Frame(tab_main,width=400, height=300)#创建第一页框架


tab1.place(x=0,y=30)
tab_main.add(tab1,text='学习⚡通讯')#将第一页插入分页栏中

def QQ():
    def open_app(app_dir):
        os.startfile(app_dir)
    if __name__ == "__main__":
        app_dir = r'"D:\QQ\Bin\QQScLauncher.exe"'
        open_app(app_dir)


button=Button(tab1,text='QQ',bd=2,command=QQ)
button.place(x=2,y=0)
button.grid(row=0,column=0,padx=5,pady=5)
button.pack()

button2=Button(tab1,text='退出',bd=2,command=tab1.quit)
#button2.place(x=2,y=0)
button2.pack()

def fun():
    print("Hello World")
button3=Button(tab1,text='A',bd=2,command=fun)
button3.place(x=0,y=0)
button3.pack()

def xue_tong():
    webbrowser.open('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')

button4 = Button(tab1, text='Web', bd=2, command=xue_tong)
button4.place(x=0, y=0)
button4.pack()

entry = tkinter.Entry(tab1,show="*")
entry.pack()

#frame.

"""""
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = Menu(tab_main, tearoff=True)
filemenu.add_command(label="打开")

filemenu.add_separator()
filemenu.add_command(label="保存")
tab_main.add_cascade(label="文件",menu=filemenu)

# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = Menu(tab_main, tearoff=False)
editmenu.add_command(label="拷贝")
editmenu.add_separator()
editmenu.add_command(label="粘贴")

tab_main.add_cascade(label="编辑", menu=editmenu)

# 创建另一个下拉菜单“工具”，然后将它添加到顶级菜单中
toolmenu = Menu(tab_main, tearoff=False)
toolmenu.add_command(label="设置")
toolmenu.add_separator()
toolmenu.add_command(label="字体")

tab_main.add_cascade(label="工具", menu=toolmenu)
"""""
# 显示菜单
root.config(menu=tab_main)
root.mainloop()



