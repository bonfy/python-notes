# -*- coding:utf-8 -*-

"""
文件操作
"""


def file_open():
    """
    文件打开
    """
    with open('file.txt', 'w') as f:
        f.write("something")


def file_open_codec():
    """
    文件打开 codecs
    """
    import codecs
    with codecs.open('file.txt', 'w', encoding='utf-8') as f:
        f.write("something")
