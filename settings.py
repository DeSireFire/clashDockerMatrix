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
# 直接获取clash配置文件
rss_pool = {
    'demo': 'https://proxypoolss.fly.dev/clash/config',
}

# 需要转为统一订阅样式的rss
# 部分订阅地址返回的不是标准clash配置文件格式
# 客户端 clash for windows 自身会处理此类问题
# 本程序则通过subconverter转换工具转为标准的clash配置文件
# 文件名称:url
convert_rss_pool = {
    'convert_demo': 'https://rss.linghunyun.xyz/api/v1/client/subscribe?token=01809ef84020c94981824ec522fe6b99',
}

# 订阅转换接口
convert_rss_api = "https://subconverter.raxianch.moe/api/sub?"

# 统一订阅文件样式
unified_rss = {
    "target": "clash",
    "url": "",
    "insert": "false",
    "config": 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini',
    "filename": "AllBalancer.yml",
    "emoji": "true",
    "list": "false",
    "tfo": "false",
    "scv": "false",
    "fdn": "false",
    "sort": "false",
    "udp": "true",
    "new_name": "true"
}
