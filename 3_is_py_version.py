# -*- coding:utf-8 -*-

"""
判断当前的Python Version
"""

import sys


def is_py_version():
    """
    利用 sys.version
    """
    if sys.version < '3':
        print("py2")
    else:
        print("py3")


def is_py_version_2():
    """
    利用 sys.version_info
    """
    if sys.version_info < (3, 4):
        raise RuntimeError('At least Python 3.4 is required')


if __name__ == '__main__':
    is_py_version()
    is_py_version_2()
