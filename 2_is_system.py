# -*- coding: utf-8 -*-


"""
判断操作系统
"""

# 运行:
# python3 2_is_system.py

import platform


def isPlatForm():
    """
    kennethreitz 
    https://github.com/kennethreitz/legit/tree/develop/legit helpers
    """
    # import platform
    # 后面就是 if is_osx ...
    
    _platform = platform.system().lower()
    
    is_osx = (_platform == 'darwin')
    is_win = (_platform == 'windows')
    is_lin = (_platform == 'linux')


def TestPlatform():
    print("----------Operation System--------------------------")

    # Windows will be : Windows
    # Linux will be : Linux
    print(platform.system())

    # Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())

    # 获取操作系统可执行程序的结构，，(’32bit’, ‘WindowsPE’)
    print(platform.architecture())

    # 计算机的网络名称，’acer-PC’
    print(platform.node())

    # 获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
    print(platform.platform())

    # 计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
    print(platform.processor())

    # 获取操作系统中Python的构建日期
    print(platform.python_build())

    # 获取系统中python解释器的信息
    print(platform.python_compiler())

    if platform.python_branch() == "":
        print(platform.python_implementation())
        print(platform.python_revision())
    print(platform.release())

    # print(platform.system_alias()
    # 获取操作系统的版本
    print(platform.version())

    # 包含上面所有的信息汇总
    print(platform.uname())


def UsePlatform():
    sysstr = platform.system()
    if(sysstr == "Windows"):
        print("Call Windows tasks")
    elif(sysstr == "Linux"):
        print("Call Linux tasks")
    else:
        print("Other System tasks")


if __name__ == '__main__':
    TestPlatform()
    UsePlatform()
