#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/27
# CreatTIME : 17:02 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'

import requests
from settings import *
from urllib.parse import quote
from urllib.parse import unquote

def url_unquote(text:str):
    """
    url解码
    :param text: str
    :return:
    """
    text = unquote(text, 'utf-8')
    return text

def url_quote(text:str):
    """
    url编码
    :param text: str
    :return:
    """
    text = quote(text, 'utf-8')
    return text


def dict_to_urlParam(temp_dict: dict) -> str:
    """
    将字典转为url的get参数
    :param temp_dict: dict, 需要转换的字典
    :return:
    """
    import urllib.parse
    params = urllib.parse.urlencode(temp_dict)
    return params

def file_downloader(file_url, save_path):
    """
    文件下载
    :param save_path: str, 文件保存路径
    :param file_url: str, 文件下载的url
    :return: byte, 文件流
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(save_path, "wb",) as f:
            f.write(response.content)

    else:
        print(f'{file_url} 下载失败！')

    return save_path

# 只允许导出 redis_client 实例化对象
__all__ = [
    "file_downloader",
    "dict_to_urlParam",
    "url_unquote",
    "url_quote",
    ]

if __name__ == '__main__':
    url = "https://subconverter.raxianch.moe/api/sub?target=clash&url=https%3A%2F%2Frss.linghunyun.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D01809ef84020c94981824ec522fe6b99&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online_Mini_MultiMode.ini&emoji=true&list=false&tfo=false&scv=false&fdn=false&sort=false&new_name=true"
    file_downloader(url, os.path.join(base_path, "configs", "demo.yml"))
