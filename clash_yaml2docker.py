#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/4/12
# CreatTIME : 16:39 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
import os
import time

base_path = os.path.abspath(os.path.dirname(__file__))
# docker 操作函数
def generateDockerComm(yaml_file_path:str, dockerName:str, port=7890, ui_port=9090):
    '''
    clash docker 命令生成器
    :param dockerName: docker容器的名称
    :param port: clash http 代理端口
    :param ui_port: web-ui端口
    :param yaml_file_path: 配置文件名
    :return: 返回整理的docker命令
    '''
    # 去除特殊字符，只保留汉字，字母、数字
    import re
    # clear_docker_name = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", dockerName)
    # base_comm = f"sudo docker run -d --name='clash-client-7894-1' --restart always -p 7894:7890 -p 7895:7891 -p 9091:9090 -v /root/software/clash/configs/1649399972122.yml:/root/.config/clash/config.yaml -v /path/ui:/ui dreamacro/clash"
    # 添加参数
    shell_params = [
        f"docker run -d",
        f"--name '{dockerName}'",
        f"--restart always",
        f"-p {port}:7890",
        f"-p {port+1}:7891/udp",
        f"-p {ui_port}:9090",
        f"-v {yaml_file_path}:/root/.config/clash/config.yaml",
        f"dreamacro/clash"
        # f"-v /path/ui:/ui",   # 用不上
    ]
    comm = ""
    comm += " ".join(shell_params)
    return comm

def getDockerName():
    # 获取docker容器的名字
    res = cmdRuner(r"docker ps --format '{{.ID}}\t{{.Image}}\t{{.Names}}'")
    temp = {}
    if res:
        for line in res.splitlines():
            if 'dreamacro/clash' in line:
                temp[line.split()[2]] = line.split()[0]
    return temp

def resultDocker_comm(new_comm, old_comm):
    """
    整合处理各个容器需要运行的命令
    有变化的docker容器重启，
    没出现过的docker批量运行
    :param new_comm: 启动的新容器的命令
    :param old_comm: 重启更新的旧容器的命令
    :return: 整合后的需要运行的命令
    """
    result_comms = {}
    if old_comm:
        # 比对端口占用，端口相同但是文件名不同就干掉容器，使用新的
        for k, v in old_comm.items():                           # {'clash—7890-xx': 'docker restart a4e0c2bc78e4'}
            for m, n in new_comm.items():                       # {'clash—7910-xx': "docker run -d --name 'clash-7910-1649399371900' --restart always -p 7910:7890 -p 7911:7891 -p 9100:9090 -v /home/ubuntu/software/clash/configs/1649399371900.yml:/root/.config/clash/config.yaml dreamacro/clash"}
                k_temp = k.split("-")[1]
                m_temp = m.split("-")[1]
                if k_temp == m_temp:
                    if k == m:
                        print(f'{k} 容器无变化仅更新配置，直接重启')
                        result_comms[k] = [v]   # ['docker restart a4e0c2bc78e4']
                    else:
                        print(f'{k} 容器有变化且存在端口占用！')
                        result_comms[k] = [
                            f"docker stop {k}", # 关闭旧容器
                            f"docker container rm {k}",  # 删除容器实例
                            n,  # docker run 一个新容器
                        ]
                else:
                    print(f'{m} 为全新容器!')
                    result_comms[m] = [n]   # ["docker run -d --name 'clash-7910-1649399371900' ......"]
    else:
        # 如果该服务器上完全没有运行clash容器，old_comm为空字典
        for m, n in new_comm.items():
            print(f'{m} 为全新容器!')
            result_comms[m] = [n]  # ["docker run -d --name 'clash-7910-1649399371900' ......"]

    return result_comms

def cmdRuner(comm,readList=False):
    '''
    命令执行函数
    :param comm:需要运行的命令
    :param readList:返回结果控制，为真时 return 结果为列表类型，为假时为字符串类型
    :return: 执行命令后翻回的结果
    '''
    try:
        result = os.popen('sudo ' + comm)
        if readList:
            return result.readlines()
        else:
            return result.read()
    except Exception as e:
        print(e)
        return None

def get_yaml_list(file_dir='configs'):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    raw_list = os.listdir(file_dir)
    files = [i for i in raw_list
             if os.path.isfile(os.path.join(file_dir, i))
             and ".yml" == os.path.splitext(os.path.join(file_dir, i))[-1]]
    return files



if __name__ == '__main__':
    # 获取配置文件
    yaml_list = get_yaml_list(os.path.join(base_path, "configs"))

    # 批量生成clash docker启动命令
    docker_comms = {}
    for n, i in enumerate(range(7890, 7890+len(yaml_list)*2, 2)):
        file_name = os.path.splitext(yaml_list[n])[0]
        full_file_name = os.path.join(base_path, "configs", yaml_list[n])
        dc = generateDockerComm(full_file_name, f"clash-{i}-{file_name}", i, 9090+n)
        if dc:
            docker_comms[f"clash-{i}-{file_name}"] = dc

    # 获取已启动的clash docker，生成批量重启命令
    # 获取已经部署过的docker容器信息
    dockered = getDockerName()  # {'clash-7890-1649648522874': 'a4e0c2bc78e4'}
    dockered_comms = {}
    for k,v in dockered.items():
        dockered_comms[k] = f"docker restart {v}"

    print(docker_comms)
    print("*" * 50)
    print(dockered_comms)

    # 整合命令
    docker_comms_result = resultDocker_comm(docker_comms,dockered_comms)

    # 批量启动clash docker
    docker_runs = {}
    for a,b in docker_comms_result.items():
        print(f'执行容器{a},命令：{b},')
        docker_runs[a] = [cmdRuner(i) for i in b]
        print(f"等待执行结束..")
        time.sleep(5)

