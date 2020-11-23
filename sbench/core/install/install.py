#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : install.py
@Time  : 2020/11/23 14:49
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import os

from sbench.libs import utils

POSIX = os.name == "posix"
WINDOWS = os.name == "nt"


class Install(object):
    """Install benchmark tools by sbench/test-profiles"""
    def __init__(self, name):
        self.name = name
        self.command = name

    def is_installed(self):
        if POSIX:
            try:
                utils.run_cmd("which {}".format(self.command), expected_rc=0)
            except Exception as e:
                print(e)
                return False
            else:
                return True
        elif WINDOWS:
            # TODO
            return True

    def run(self):
        if self.is_installed():
            return True
        return True


if __name__ == '__main__':
    pass
