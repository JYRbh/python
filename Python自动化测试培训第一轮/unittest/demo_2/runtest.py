# -*- coding: utf-8 -*-

import os
import unittest

# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")

def mainTest():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    runner = unittest.TextTestRunner()
    runner.run(discover)

if __name__=='__main__':
    #执行测试
    mainTest()
