#!/usr/bin/python
# encoding:utf-8


"""
@author yushu
@contact:yusuhanghe92@outlook.com
@file:
@Description:
@Date: 2021-10-11
@Time: 21:42
"""
import psutil

pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)

    # if p.name() == 'dllhost.exe':
    #     cmd = 'taskkill /F /IM dllhost.exe'
    #     os.system(cmd)
    if 'ython' in p.name():
        print('pid-%s,pname-%s' % (pid, p.name()))
