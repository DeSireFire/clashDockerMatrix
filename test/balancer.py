#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/11
# CreatTIME : 15:20 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7,und;q=0.6,ja;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://192.168.50.122:7889',
    'Pragma': 'no-cache',
    'Referer': 'http://192.168.50.122:7889/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

json_data = {
    'name': '\uD83D\uDD2E \u8D1F\u8F7D\u5747\u8861',
}
# http://192.168.50.122:9091/proxies/🚀 节点选择

# response = requests.put('http://192.168.50.122:9091/proxies/%F0%9F%9A%80%20%E8%8A%82%E7%82%B9%E9%80%89%E6%8B%A9', headers=headers, json=json_data, verify=False)
response = requests.get('http://192.168.50.122:9091/traffic', headers=headers, verify=False)
print(response.text)