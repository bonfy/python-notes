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
        # 通常在这种 python版本小于3的情况下会重设encoding
        # reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
        # sys.setdefaultencoding('utf-8')
        print("py2")
    else:
        print("py3")


def is_py_version_2():
    """
    利用 sys.version_info
    """
    if sys.version_info < (3, 4):
        raise RuntimeError('At least Python 3.4 is required')


def is_py_version_3():
    """
    From werkzeug
    判断python version
    """
    PY2 = sys.version_info[0] == 2

    if PY2:
        unichr = unichr
        text_type = unicode
        string_types = (str, unicode)
        integer_types = (int, long)
    else:
        unichr = chr
        text_type = str
        string_types = (str, )
        integer_types = (int, )


if __name__ == '__main__':
    is_py_version()
    is_py_version_2()
