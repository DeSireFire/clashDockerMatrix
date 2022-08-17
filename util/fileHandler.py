#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/28
# CreatTIME : 16:12 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
import os
def StrOfSize(size):
    '''
    auth: wangshengke@kedacom.com ；科达柯大侠
    递归实现，精确为最大单位值 + 小数点后三位
    '''
    def strofsize(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return strofsize(integer, remainder, level)
        else:
            return integer, remainder, level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = strofsize(size, 0, 0)
    if level+1 > len(units):
        level = -1
    return ( '{}.{:>03d} {}'.format(integer, remainder, units[level]) )


def clashYmlCheck(file_path):
    if os.path.exists(file_path):
        check_text = ""
        with open(file_path, 'r', encoding="utf-8") as f:
            check_text = f.read()

        if "proxy-groups" not in check_text and "proxies:" not in check_text:
            print(f"更新失败！{file_path} 配置文件")
            return False
        else:
            return True

    else:
        print(f"更新失败！{file_path} 配置文件")
        return False
