#!usr/bin/python
# encoding:utf-8


"""
@author:yushuanghe
@contact:yusuhanghe92@outlook.com
@file:demo
@time:2017/07/07 17:37
"""


def fun():
    pass


class A(object):
    pass


if __name__ == '__main__':
    print (100 + 200)
    print ("====")

    # print absolute value of an integer:
    a = 100
    if a >= 1000:
        print(a)
    else:
        print(-a)

    print ("====")

    # i = raw_input("输入")
    # print "你好，", i

    print ("i\'m \"ok\"")
    print ("\\\t\\")
    print ("\\\n\\")
    # r""默认里面的字符串不转意
    print (r"\\\\\\\t")
    print ('''
大力出奇迹！
    阿诗丹顿
    东方闪电
    
    ''')
    print (r'''
    大力出奇迹！
        阿诗丹顿
        东方闪电
//////\\\\\\\\t\n\\\\\
        ''')
    print (True)
    print (False)
    print (True and True)
    print (False or True)
    print (not True)
    print (None)

    a = 123
    print a
    a = "大力出奇迹！"
    print a

    x = 10
    x = x + 2
    print x

    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)

    print 10.0 / 3
    print 10 / 3
    print 10.0 // 3
    print 10 % 3

    print
    print a

    print (ord("A"))
    print (chr(122))
    print
    # unicode编码
    print u'大力出奇迹！'
    # 把unicode转换为utf-8
    print u'\u4e2d'.encode('utf-8')
    # 把utf-8转换为unicode
    print "大力出奇迹！".decode('utf-8')
    print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

    list = ['大力', '二利', '三力']
    print len(list)
    print list[0]
    print list[-1]
    # print list[3]
    list.append('四力')
    print list[-1]
    list.insert(0, '0力')
    print list[0]
    print len(list)
    list.pop(-1)
    print list[-1]

    list2=['大力出奇迹！',111,True]

