# coding:utf-8
"""
File Name:write
Description:

Author:yushuanghe
date:2019/03/20
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '大力出奇迹!'


if __name__ == '__main__':
    app.run()
