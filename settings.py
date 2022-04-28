#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/27
# CreatTIME : 16:56 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
import os
import time

# 项目目录
base_path = os.path.abspath(os.path.dirname(__file__))

# 订阅地址
# 需要转为统一订阅样式的rss
# 文件名称:url
convert_rss = {
    'demo': 'https://proxypoolss.fly.dev/clash/config',
}

# 订阅转换接口
convert_rss_api = "https://subconverter.raxianch.moe/api/sub?"

# 统一订阅文件样式
unified_rss = {
    "target": "clash",
    "url": "https://proxypoolss.fly.dev/clash/config",
    "insert": "false",
    "config": 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini',
    "emoji": "true",
    "list": "false",
    "tfo": "false",
    "scv": "false",
    "fdn": "false",
    "sort": "false",
    "new_name": "true"
}