#!/usr/bin/python
# -*- coding:utf-8 -*-

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

