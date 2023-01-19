#!/usr/bin/python
# -*- coding:utf-8 -*-

# 存储被装饰器 @register 装饰的函数
registry = []
def register(active = True):
    def decorate(func):
        if active:
            print(f"注册函数->{func}")
            #记录被装饰的函数
            registry.append(func)  #在列表末尾添加新对象
        return func
    return decorate

@register()
def f1():
    print("执行 f1()")

@register(active=False)
def f2():
    print("执行 f2()")
