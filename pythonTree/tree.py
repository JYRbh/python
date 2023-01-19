#!/usr/bin/python
# -*- coding: UTF-8 -*-

#声明树的高度
height = 5
#树的雪花数，初始值为1
stars = 1

for i in range(height):
    print((' '*(height-i))+('*'*(2*i+1)))

print((' '*height)+'|')
