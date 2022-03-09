#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("主界面")
#
def show():
    print(e.get())

e = tkinter.Variable()
entry = tkinter.Entry(win,textvariable=e)

button = tkinter.Button(win,text = "登录",command=show)

entry.pack()
button.pack()
win.mainloop()