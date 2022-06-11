"""
Copyright (c) 2018 hu. All rights reserved.
Personal code, only for learning and communication.
You can contact me in the following ways:
    stonebirdjx <1245863260@qq.com, g1245863260@gmail.com>
    https://www.hjxstbserver.xyz/
File: router  2022/6/11 12:08
Desc:
"""

from configs.config import response_header, \
    status_ok, \
    status_notfound
from pkg.apis.v1.ocr import Ocr
from flask import Flask

# app flask program entry.
app = Flask(__name__)


@app.route("/ping")
def ping():
    data = {
        "ping": "pong",
    }
    return data, status_ok, response_header


@app.route("/")
def root():
    content = "Welcome to visit stonebird ai"
    return content, status_ok, response_header


@app.errorhandler(404)
def no_route(e):
    data = {
        "message": "God has no route"
    }
    return data, status_notfound, response_header


# api/v1
api_v1 = "/api/v1"


@app.route(api_v1 + "/ocr")
def easy_ocr():
    v1ocr = Ocr([], "pic_path")
    data = v1ocr.read_data()
    return data, status_ok, response_header
