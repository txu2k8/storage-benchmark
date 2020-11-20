#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : test_definition_handler.py
@Time  : 2020/11/20 17:34
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import os
import xml.sax
import unittest
from collections import defaultdict


class TestDefinitionHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.TestInformation = defaultdict(str)
        self.TestProfile = defaultdict(str)
        self.TestSettings = defaultdict(str)
        self.opt = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "TestInformation":
            print("\nTestInformation:")
        elif tag == "TestProfile":
            print("\nTestProfile")
        elif tag == "TestSettings":
            print("\nTestSettings")

    # 元素结束事件处理
    def endElement(self, tag):
        if self.current_data in self.TestInformation.keys():
            print(self.current_data+":", self.TestInformation[self.current_data])
        elif self.current_data in self.TestProfile.keys():
            print(self.current_data+":", self.TestProfile[self.current_data])
        elif self.current_data in self.TestSettings[self.opt]:
            print(self.current_data+":", self.TestSettings[self.opt])
        self.current_data = ""

    # 内容事件处理
    def characters(self, content):
        if self.current_data == "Title":
            self.TestInformation['Title'] = content
        elif self.current_data == "Description":
            self.TestInformation['Description'] = content
        elif self.current_data == "SubTitle":
            self.TestInformation['SubTitle'] = content

        elif self.current_data == "SupportedPlatforms":
            self.TestProfile['SupportedPlatforms'] = content
        elif self.current_data == "TestType":
            self.TestProfile['TestType'] = content
        elif self.current_data == "ProjectURL":
            self.TestProfile['ProjectURL'] = content

        elif self.current_data == "DisplayName":
            self.opt = content
            self.TestSettings[self.opt] = defaultdict(str)
        elif self.current_data == "Name":
            self.TestSettings[self.opt]['Name'] = content
        elif self.current_data == "Value":
            self.TestSettings[self.opt]['Value'] = content


class UnitTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01(self):
        # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        # 重写 ContextHandler
        handler = TestDefinitionHandler()
        parser.setContentHandler(handler)
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        f_xml = os.path.join(os.path.dirname(cur_dir), 'test-profiles/sqlite/test-definition.xml')
        parser.parse(f_xml)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
