#!/usr/bin/python
# encoding:utf-8


"""
@author:yushuanghe
@contact:yusuhanghe92@outlook.com
@file:demoClass
@time:2017/07/25 00:20
"""


def fun():
    pass


# 经典类
class A():
    # 构造函数
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # toString
    def __str__(self):
        return self._x + " " + self._y

    pass


# 新式类
class B(object):
    pass


if __name__ == '__main__':
    a = A('大力', '出奇迹！')
    # 执行__str__
    print a

    b = B
