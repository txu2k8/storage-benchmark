#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : downloads_handler.py
@Time  : 2020/11/20 17:20
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import os
import xml.sax
import unittest


class DownloadsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.url = ""
        self.md5 = ""
        self.sha256 = ""
        self.filename = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "Package":
            print()
            print("Downloads Package:")

    # 元素结束事件处理
    def endElement(self, tag):
        if self.current_data == "URL":
            print("URL:", self.url)
        elif self.current_data == "MD5":
            print("MD5:", self.md5)
        elif self.current_data == "SHA256":
            print("SHA256:", self.sha256)
        elif self.current_data == "FileName":
            print("FileName:", self.filename)
        self.current_data = ""

    # 内容事件处理
    def characters(self, content):
        if self.current_data == "URL":
            self.url = content
        elif self.current_data == "MD5":
            self.md5 = content
        elif self.current_data == "SHA256":
            self.sha256 = content
        elif self.current_data == "FileName":
            self.filename = content


class UnitTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01(self):
        # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        # 重写 ContextHandler
        handler = DownloadsHandler()
        parser.setContentHandler(handler)
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        f_xml = os.path.join(os.path.dirname(cur_dir), 'test-profiles/sqlite/downloads.xml')
        parser.parse(f_xml)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
