#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from MyDict import Dict

class TestMyDict(unittest.TestCase):
    def test___init__(self, **kw):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AssertionError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()