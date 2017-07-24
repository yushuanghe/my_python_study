#!/usr/bin/python
# encoding:utf-8


"""
@author:yushuanghe
@contact:yusuhanghe92@outlook.com
@file:demoException
@time:2017/07/25 00:26
"""

import demoDef as d


def fun():
    pass


class A(object):
    pass


if __name__ == '__main__':
    a = dict(name="大力", age=20, ags=22)
    print a['ags']

    a = dict(name='大力', age=20)
    # print a['ags']
    try:
        print a['ags']
    except KeyError:
        print '出错了！'

    print
    a = range(1, 10)
    try:
        a[8] = 100
    except IndexError:
        print '出错了！'
    else:
        print 'else'

    # demoDef.action('aaa')('哈哈')
    d.action('aaa')('哈哈')

    from demoClass import A

    x = A('a', 'b')
    print x

    print
    print dir(d)
    print help(d)
