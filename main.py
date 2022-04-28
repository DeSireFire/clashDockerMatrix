#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/27
# CreatTIME : 17:41 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
from util.net import *
from settings import *
import copy
def update_rss():
    """
    更新订阅
    :return:
    """
    for file_name,file_url in convert_rss.items():
        temp_parm = copy.deepcopy(unified_rss)
        # temp_parm["url"] = url_quote(file_url)
        # temp_parm["config"] = url_quote(temp_parm["config"])
        param_str = dict_to_urlParam(temp_parm)
        rss_url = f'{convert_rss_api}{param_str}'
        print(rss_url)
if __name__ == '__main__':
    update_rss()