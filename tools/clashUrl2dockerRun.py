#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/8/31
# CreatTIME : 15:14 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
"""
设置的中的url批量转换成docker运行命令
"""
from settings import *

from util.net import file_downloader


def main_process():
    for name, url in convert_rss_pool.items():
        file_downloader(url, os.path.join(base_path, "configs", f"{name}.yml"))



if __name__ == '__main__':
    print(convert_rss_pool)
