#!/usr/bin/python
# encoding:utf-8


"""
@author:yushuanghe
@contact:yusuhanghe92@outlook.com
@file:demoDef
@time:2017/07/24 23:51
"""


def msg(a):
    print a
    return ('哈哈', 123, True)


def handleText(x):
    print 'text'


def handleHtml(x):
    print 'html'


def action(t):
    if t == 'html':
        return handleHtml
    else:
        return handleText


class A(object):
    pass


if __name__ == '__main__':
    a, b, c = msg("大力出奇迹！")
    print a, b, c

    x = msg("大力出奇迹！")
    print x, type(x)

    action('text')('大力出奇迹！')
