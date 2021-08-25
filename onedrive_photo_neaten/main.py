#!/usr/bin/python
# encoding:utf-8


"""
@author yushu
@contact:yusuhanghe92@outlook.com
@file:
@Description:
@Date: 2021-08-24
@Time: 20:14
"""
import hashlib
import os
import time


def list_dir(path, separator):
    pic_dict = {}
    mkdir_set = set()
    delete_list = []
    g = os.walk(path)

    for path, dir_list, file_list in g:
        for file_name in file_list:
            file_full_name = os.path.join(path, file_name)
            file_uptime = get_file_uptime(file_full_name)
            mkdir1 = os.path.join(path, file_uptime[0:4])
            mkdir2 = os.path.join(mkdir1, file_uptime[5:7])
            mkdir_set.add(mkdir1)
            mkdir_set.add(mkdir2)
            file_md5 = get_file_md5(file_full_name)
            # line = '{file_full_name}:{file_uptime}:{file_md5}'.format(file_full_name=file_full_name,
            #                                                           file_uptime=file_uptime, file_md5=file_md5)
            # print(line)

            if file_md5 in pic_dict:
                line = pic_dict[file_md5]
                pre_file_name = line.split(separator)[0]
                pre_file_uptime = line.split(separator)[1]
                # print('{file_full_name}:{file_uptime}:{pre_file_name}:{pre_file_uptime}'.format(
                #     file_full_name=file_full_name, file_uptime=file_uptime, pre_file_name=pre_file_name,
                #     pre_file_uptime=pre_file_uptime))
                if file_uptime < pre_file_uptime:
                    line = '{file_full_name}{separator}{file_uptime}'.format(separator=separator,
                                                                             file_full_name=file_full_name,
                                                                             file_uptime=file_uptime)
                    pic_dict[file_md5] = line
                    delete_list.append(pre_file_name)
                else:
                    delete_list.append(file_full_name)
            else:
                line = '{file_full_name}{separator}{file_uptime}'.format(separator=separator,
                                                                         file_full_name=file_full_name,
                                                                         file_uptime=file_uptime)
                pic_dict[file_md5] = line

        print(pic_dict)
        print(mkdir_set)
        print(delete_list)
        return (pic_dict, mkdir_set, delete_list)


def get_file_uptime(file_full_name):
    # 文件的修改时间
    uptime = time.localtime(os.stat(file_full_name).st_mtime)
    return time.strftime("%Y-%m-%d", uptime)


def get_file_md5(file_full_name):
    hash_md5 = hashlib.md5()
    with open(file_full_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def delete_repetition_file(delete_list):
    for file_name in delete_list:
        os.remove(file_name)


def mkdirs(mkdir_set):
    for path in sorted(mkdir_set):
        if not os.path.exists(path):
            os.mkdir(path)


def move_files(pic_dict, path, separator):
    for line in pic_dict.values():
        file_full_name = line.split(separator)[0]
        file_name = os.path.basename(file_full_name)
        uptime = line.split(separator)[1]
        target_path = os.path.join(os.path.join(path, uptime[0:4]), uptime[5:7])
        print('{file_full_name}{separator}{file_name}{separator}{target_path}'.format(file_full_name=file_full_name,
                                                                                      file_name=file_name,
                                                                                      target_path=target_path,
                                                                                      separator=separator))
        os.replace(file_full_name, os.path.join(target_path, file_name))


if __name__ == '__main__':
    '''
    解析目录，剔除文件夹
    遍历，取uptime，md5
    md5排重
    剩余时间创建文件夹
    move
    '''
    path = r'C:\Users\yushu\OneDrive\图片\本机照片'
    separator = ';'
    my_tuple = list_dir(path, separator)
    mkdirs(my_tuple[1])
    move_files(my_tuple[0], path, separator)
    # delete_repetition_file(my_tuple[2])
