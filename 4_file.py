# -*- coding:utf-8 -*-

"""
文件操作
"""


def file_open(filename):
    """
    文件打开
    """
    with open(filename, 'w') as f:
        f.write("something")


def file_open_codec(filename):
    """
    文件打开 codecs
    """
    import codecs
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        f.write("something")
