#!/usr/bin/python
# encoding:utf-8


"""
@author yushu
@contact:yusuhanghe92@outlook.com
@file:
@Description:
@Date: 2021-10-14
@Time: 17:42
"""

# 添加请求头
import os
import sys
import time
from urllib import request

import requests
from lxml import etree

from img_spider.jdwht_spider.jdwht_img import get_html_tree, execute_spider

start_url = sys.argv[1]
base_url = start_url.split('1.html')[0]
detail_base_url = 'http://' + start_url.split('/')[2]
# 通用的url模板(不能修改)
tree = get_html_tree(start_url)

last_page = tree.xpath('//div[@class="pagelist"]//a[@title="尾页"]/@href')[0]
print(last_page)

for list_id in range(1, int(last_page.split('.html')[0]) + 1):
    # for list_id in range(1, 2):
    list_req_url = base_url + str(list_id) + '.html'
    print(list_req_url)

    # http://www.jdwht.com/zg/taotu/20220410/125496.html
    tree = get_html_tree(list_req_url)
    url_list = tree.xpath('//div[@id="list"]//li/a/@href')
    print(url_list)
    for url in url_list:
        detail_req_url = detail_base_url + url
        detail_base_url = detail_req_url.split('.html')[0] + '{page_id}.html'
        execute_spider(detail_req_url, detail_base_url)

        time.sleep(60)

    time.sleep(120)

print('list done!')
