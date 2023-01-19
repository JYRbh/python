#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import threading
import time
import tkinter

from pynput import mouse
from pynput.mouse import Button,Controller as MouseController

#鼠标动作模板
def mouse_action_template():
    return {
        "name":"mouse",
        "event":"defailt",
        "target":"defailt",
        "location":{
            "x":"0",
            "y":"0"
    }
}

#倒计时监听，更新UI触发自定义线程对象
class UIUpdateCutDownExecute(threading.Thread):
    def __init__(self,cut_down_time,custom_thread_list):
        super().__init__()
        self.cut_down_time = cut_down_time
        self.custom_thread_list = custom_thread_list

    def run(self):
        while  self.cut_down_time > 0:
            for custom_thread in self.custom_thread_list:
                if custom_thread['obj_ui']is not None:
                    custom_thread['obj_ui']['text'] = str(self.cut_down_time)
                    custom_thread['obj_ui']['state'] = 'disabled'
                    self.cut_down_time = self.cut_down_time - 1
            time.sleep(1)
        else:
            for custom_thread in self.custom_thread_list:
                if custom_thread['obj_ui'] is None:
                    custom_thread['OBj_ui']['text'] = custom_thread['final_text']
                    custom_thread['OBj_ui']['state'] = 'disabled'
                if custom_thread['obj_thread'] is not None:
                    custom_thread['obj_thread'].start()
                    time.sleep(1)


class MouseActionListener(threading.Thread):
    esc_key = False

    def __init__(self,file_name = 'mouse.action'):
        super().__init__()
        self.file_name = file_name

    def close_listener(self,listener):
        if self.esc_key:
            listener.stop()

    def run(self):
        with open(self.file_name,'w',encoding='utf-8') as file:
            #鼠标移动事件
            def on_move(x,y):
                template = mouse_action_template()
                template['event'] = 'move'
                template['location']['x'] = x
                template['location']['y'] = y
                file.writelines(json.dumps(template)+"\n")
                file.flush() #将缓冲区中的数据立刻写入文件，同时清空缓冲区
                self.close_listener(mouseListener)

            #鼠标点击事件
            def on_click(x,y,button,pressed):
                template = mouse_action_template()
                template['event'] = 'click'
                template['target'] = button.name
                template['action'] = pressed
                template['location']['x'] = x
                template['location']['y'] = y
                file.writelines(json.dumps(template)+"\n")
                file.flush()
                self.close_listener(mouseListener)

            with mouse.Listener(on_move = on_move,on_click = on_click) as mouseListener:
                mouseListener.join()

#鼠标动作执行
class MouseActionExecute(threading.Thread):

    def __init__(self,file_name = 'mouse.action',execute_count=0):
        super().__init__()
        self.file_name = file_name
        self.execute_count = execute_count

    def run(self):
        while self.execute_count > 0:
            with open(self.file_name,'r',encoding='utf-8') as file:
                mouse_exec = MouseController()
                line = file.readline()
                while line:
                    obj = json.loads(line)
                    if obj['name'] == 'mouse':
                        if obj['event'] == 'move':
                            mouse_exec.position = (obj['location']['x'],obj['location']['y'])
                            time.sleep(0.01)
                        elif obj['event'] == 'click':
                            if obj['action']:
                                if obj['target'] == 'left':
                                    mouse_exec.press(Button.left)
                                else:
                                    mouse_exec.press(Button.right)

                            else:
                                if obj['target'] == 'left':
                                    mouse_exec.press(Button.left)
                                else:
                                    mouse_exec.press(Button.right)
                            time.sleep(0.01)
                line =file.readline()
            self.execute_count = self.execute_count-1

def command_adapter(action):
    if action == 'listener':
        if startListenerBtn['text'] == '开始录制':
            custom_thread_list = [
                {
                    'obj_thread':MouseActionListener(),
                    'obj_ui':startListenerBtn,
                    'final_text': '录制中...esc停止录制'
                }
            ]
            MouseActionListener.esc_key = False
            UIUpdateCutDownExecute(startTime.get(),custom_thread_list).start()

    if action == 'execute':
        if startExecuteBtn['text'] == '开始回放':
            custom_thread_list = [
                {
                    'obj_thread':MouseActionExecute(execute_count=playCount.get()),
                    'obj_ui':startExecuteBtn,
                    'final_text':'回放中...关闭程序停止回放'
                }
            ]
            UIUpdateCutDownExecute(endTime.get(), custom_thread_list).start()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('按键精灵-蓝士钦')
    root.geometry('200x200+400+100')

    listenerStartLabel = tkinter.Label(root, text='录制倒计时')
    listenerStartLabel.place(x=10, y=10, width=80, height=20)
    startTime = tkinter.IntVar()
    listenerStartEdit = tkinter.Entry(root, textvariable=startTime)
    listenerStartEdit.place(x=100, y=10, width=60, height=20)
    startTime.set(3)

    listenerTipLabel = tkinter.Label(root, text='秒')
    listenerTipLabel.place(x=160, y=10, width=20, height=20)

    startListenerBtn = tkinter.Button(root, text="开始录制", command=lambda: command_adapter('listener'))
    startListenerBtn.place(x=10, y=45, width=180, height=30)

    executeEndLabel = tkinter.Label(root, text='回放倒计时')
    executeEndLabel.place(x=10, y=85, width=80, height=20)
    endTime = tkinter.IntVar()
    executeEndEdit = tkinter.Entry(root, textvariable=endTime)
    executeEndEdit.place(x=100, y=85, width=60, height=20)
    endTime.set(6)

    executeTipLabel = tkinter.Label(root, text='秒')
    executeTipLabel.place(x=160, y=85, width=20, height=20)

    playCountLabel = tkinter.Label(root, text='回放次数')
    playCountLabel.place(x=10, y=115, width=80, height=20)
    playCount = tkinter.IntVar()
    playCountEdit = tkinter.Entry(root, textvariable=playCount)
    playCountEdit.place(x=100, y=115, width=60, height=20)
    playCount.set(1)

    playCountTipLabel = tkinter.Label(root, text='次')
    playCountTipLabel.place(x=160, y=115, width=20, height=20)

    startExecuteBtn = tkinter.Button(root, text="开始回放", command=lambda:command_adapter('execute'))
    startExecuteBtn.place(x=10, y=145, width=180, height=30)
    root.mainloop()



mouse = MouseController

