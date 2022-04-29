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
    # 非转换 rss
    for file_name, file_url in rss_pool.items():
        print(f"更新{file_name}.yml 配置文件 by {file_url}")
        file_path = os.path.join(base_path,"configs", f"{file_name}.yml")
        text_downloader(file_url, file_path)
        # todo 文件检查
        if os.path.exists(file_path):
            check_text = ""
            with open(file_path, 'r', encoding="utf-8") as f:
                check_text = f.read()

            if "proxy-groups" not in check_text and "proxies:" not in check_text:
                print(f"更新失败！{file_name}.yml 配置文件 by {file_url}")

        else:
            print(f"更新失败！{file_name}.yml 配置文件 by {file_url}")

    # 统一转换rss
    for file_name,file_url in convert_rss_pool.items():
        print(f"统一转换更新{file_name}.yml 配置文件 by {file_url}")
        file_path = os.path.join(base_path, "configs", f"{file_name}.yml")
        temp_parm = copy.deepcopy(unified_rss)
        temp_parm["url"] = file_url
        param_str = dict_to_urlParam(temp_parm)
        rss_url = f'{convert_rss_api}{param_str}'
        text,save_path = text_downloader(rss_url, file_path)

        # 定制化修改
        # strategy: round-robin
        # 均衡模式修改为round-robin
        text = text.replace("consistent-hashing", "round-robin")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)

if __name__ == '__main__':
    update_rss()