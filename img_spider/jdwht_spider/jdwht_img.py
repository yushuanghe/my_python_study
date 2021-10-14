#!/usr/bin/python
# encoding:utf-8


"""
@author yushu
@contact:yusuhanghe92@outlook.com
@file:
@Description:
@Date: 2021-10-10
@Time: 19:51
"""
import os
import sys
import time
from urllib import request

import requests
from lxml import etree

# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


def get_html_tree(req_url):
    response = requests.get(url=req_url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    time.sleep(5)
    return tree


def get_img_from_detail(base_url, page_id, img_path, img_name_prefix):
    img_name = img_name_prefix + str(page_id) + '.jpg'
    img_full_path = img_path + '\\' + img_name

    if not os.path.exists(img_full_path):
        req_url = base_url.format(page_id=page_id)
        tree = get_html_tree(req_url)
        img_src = tree.xpath('//div[@id=\'picg\']//img/@src')[0]
        request.urlretrieve(img_src, img_full_path)
        print('%s下载完成' % img_name)


def execute_spider(req_url, base_url):
    tree = get_html_tree(req_url)

    dir_name = tree.xpath('//meta[@name="keywords"]/@content')[0]
    base_path = 'D:\data\自定义'
    img_path = base_path + '\\' + dir_name
    print(img_path)

    if not os.path.exists(img_path):
        os.mkdir(img_path)

    get_img_from_detail(base_url, '', img_path, dir_name)

    page_list = tree.xpath('//div[@class="pagelist"]//a/@href')
    page_list = set(page_list)
    print(page_list)
    print('一共%d张图片' % (len(page_list) + 1))

    for page in page_list:
        page_id = '_' + page.split('_')[1].split('.')[0]
        get_img_from_detail(base_url, page_id, img_path, dir_name)

    print('spider detail done!')


if __name__ == '__main__':
    input_url = sys.argv[1]
    # 通用的url模板(不能修改)
    base_url = input_url.split('.html')[0] + '{page_id}.html'
    req_url = base_url.format(page_id='')
    execute_spider(req_url, base_url)
