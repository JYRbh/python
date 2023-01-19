#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import threading
from threading import Thread

class MyThreading(threading.Thread):
    def __init__(self,name):
        super(MyThreading, self).__init__()
        name = self.name

    def run(self):
        print(f"开始线程:{self.name},{time.ctime()}")
        time.sleep(2)
        print(f"退出线程：{self.name},{time.ctime()}")


'''' 
#join的用法
class Test:
    def __init__(self):
        pass
    def main_threading(self):
        print(f"主线程开始运行：{time.ctime()}")

        Thread1 = MyThreading("Thread1")
        Thread2 = MyThreading("Thread2")

        Thread1.start()
        Thread2.start()

        Thread1.join()
       # Thread2.join()

        print(f"主线程结束运行：{time.ctime()}")
'''''

#守护线程的使用
class Test:
    def __init__(self):
        pass

    def main_threading(self):
        print(f"主线程开始运行，{time.ctime()}")

        Thread1 = MyThreading("Thread1")
        Thread2 = MyThreading("Thread2")

        Thread1.setDaemon(True)
        Thread2.setDaemon(True)

        Thread1.start()
        Thread2.start()

        print(f"主线程结束运行，{time.ctime()}")


if __name__ == "__main__":
    test = Test()
    test.main_threading()

