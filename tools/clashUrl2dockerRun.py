#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/8/31
# CreatTIME : 15:14 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'

import copy
import pypinyin
from util.clash_yaml2docker import generateDockerComm
from util.fileHandler import clashYmlCheck

"""
设置的中的url批量转换成docker运行命令
"""
from settings import *
from util.net import text_downloader,dict_to_urlParam

def hanzi_pinyin(hanzi):
    raw_pinyins = pypinyin.pinyin(hanzi, style=pypinyin.NORMAL)
    one_pinyins = [i[0] for i in raw_pinyins]
    pinyin = one_pinyins[0].capitalize() + '-' + ''.join(one_pinyins[1:]).capitalize()
    return pinyin

def downLoader_RSS():
    for name, base_url in convert_rss_pool.items():
        params = copy.deepcopy(unified_rss)
        params["url"] = base_url
        params["filename"] = f"{name}.yml"
        params_str = dict_to_urlParam(params)
        url = f"{convert_rss_api}?{params_str}"
        file_path = os.path.join(base_path, "configs", params["filename"])
        text,save_path = text_downloader(url, file_path)

        file_status = clashYmlCheck(file_path)
        if file_status:
            # 定制化修改
            # strategy: round-robin
            # 均衡模式修改为round-robin
            text = text.replace("consistent-hashing", "round-robin")
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(text)
        else:
            if os.path.exists(file_path):
                os.remove(file_path)

def main_process():
    # 下载rss
    downLoader_RSS()

    # 生成docker run 命令
    # 获取文件夹列表
    ymlfilePath = os.path.join(base_path, "configs")
    files = os.listdir(ymlfilePath)
    # for n,f in enumerate(files,start=1):
    for n,f in enumerate(convert_rss_pool,start=1):
        if f"{f}.yml" in files:
            name = os.path.splitext(f)[0]
            hzpy = hanzi_pinyin(name)
            comm = generateDockerComm(f'/data/crawler/crawlers_project/clash/{f}.yml', f"clash-{hzpy}", 7200+n, 7100+n)
            print(f"sudo {comm}")
    print("*"*100)
    for n,f in enumerate(convert_rss_pool,start=1):
        if f"{f}.yml" in files:
            name = os.path.splitext(f)[0]
            hzpy = hanzi_pinyin(name)
            comm = generateDockerComm(f'/home/ubuntu/software/clashs/{f}.yml', f"clash-{hzpy}", 7200+n, 7100+n)
            print(f"sudo {comm}")
    print("*"*100)
    for n,f in enumerate(convert_rss_pool,start=1):
        if f"{f}.yml" in files:
            name = os.path.splitext(f)[0]
            hzpy = hanzi_pinyin(name)
            comm = f"docker restart clash-{hzpy}"
            print(f"sudo {comm}")
        if n == len(convert_rss_pool):
            print(f"sudo docker ps -a")

if __name__ == '__main__':
    main_process()