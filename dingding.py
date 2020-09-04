# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:farmework
# File_name:dingding.py
# Author: dong xin
# Time:2020年09月04日

import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=fc60402bafba511344311f06a6983635c4caa1931f2c810dfe8071c03e272afb'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('我,测试报告已生成')
        },
        "at":{
            "atMobiles":[
                "18224563952"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False   #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()