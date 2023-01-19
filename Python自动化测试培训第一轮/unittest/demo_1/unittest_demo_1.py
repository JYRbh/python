# -*- coding: utf-8 -*-
 
import unittest
 
class TestMathFunc(unittest.TestCase):
 
    def setUp(self):
        print("init the test environment>>>>>>>>")
 
    def tearDown(self):
        print("clean the test environment<<<<<<<\n")
 
    def test_add(self):
        result = 1 + 2
        print(result)
        self.assertEqual(result, 3)

    @unittest.skip("I don't want to run the case")
    def test_del(self):
        result = 3 - 1
        print(result)
        self.assertEqual(result, 2)
   

if __name__ == '__main__':
    unittest.main()
