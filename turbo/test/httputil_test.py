#-*- coding:utf-8 -*-

import sys

import unittest
import logging
import urllib

from bson.objectid import ObjectId

import turbo.httputil  as hu


class HttpUtilTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_encode_http_params(self):
        keyword = '美女'
        paras = hu.encode_http_params(k=10, h=2, key='ass', keyword=keyword)
        self.assertEqual(sorted(paras.split('&')),['h=2', 'k=10', 'key=ass', 'keyword=%s'%urllib.quote(keyword)])

if __name__ == '__main__':
    unittest.main()
