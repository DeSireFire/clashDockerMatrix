#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/8/17
# CreatTIME : 18:15 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
import os
import httpx
import asyncio
from util.fileHandler import *
from main import rss_pool, convert_rss_pool, convert_rss_api, unified_rss,base_path
class rss(object):
    """
    通过订阅链接下载和保存配置文件

    修改位置文件中的特定字符串
    """
    def __init__(self):
        self.rss_pool = rss_pool
        self.convert_rss_pool = convert_rss_pool
        self.convert_rss_api = convert_rss_api
        self.unified_rss = unified_rss


    def dl_raw_rss(self):
        # 非转换 rss
        for file_name, file_url in rss_pool.items():
            print(f"更新{file_name}.yml 配置文件 by {file_url}")
            file_path = os.path.join(base_path, "configs", f"{file_name}.yml")
            asyncio.run(self.text_downloader(file_url, file_path))
            file_status = clashYmlCheck(file_path)
            if not file_status and os.path.exists(file_path):
                os.remove(file_path)

    async def text_downloader(self):
        tasks = [asyncio.create_task(self.make_request()) for _ in range(250)]
        await asyncio.gather(*tasks)

    async def make_request(self):
        async with httpx.AsyncClient() as client:
            resp = await client.get('', headers=headers, params=params)
            assert resp.status_code == 200
            html = resp.text
            print(html)