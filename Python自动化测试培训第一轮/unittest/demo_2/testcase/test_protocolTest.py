# -*- coding: utf-8 -*-
 
import unittest

def getResultCmd():
     cmd = "55 AA 03 04 00 00 06"
     return cmd[0:5]

class TestProtocolParse(unittest.TestCase):
 
    def setUp(self):
        print("init the test environment>>>>>>>>")
 
    def tearDown(self):
        print("clean the test environment<<<<<<<\n")
 
    def test_add(self):
        resultCmd = getResultCmd()
        print(resultCmd)
        self.assertEqual(resultCmd, "55 AA")

if __name__ == '__main__':
    unittest.main()
