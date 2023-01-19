# -*- coding: utf-8 -*-
 
import unittest
 
class TestMulDiv(unittest.TestCase):
    def setUp(self):
        print("init the test environment>>>>>>>>")
 
    def tearDown(self):
        print("clean the test environment<<<<<<<\n")
 
    def test_multi(self):
        result = 3*2
        print(result)
        self.assertEqual(result, 6)

    def test_div(self):
        result = 3/2
        print(result)
        self.assertEqual(result, 1.5)
   

if __name__ == '__main__':
    unittest.main()
