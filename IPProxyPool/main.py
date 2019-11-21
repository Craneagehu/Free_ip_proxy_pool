#-*- coding:utf-8 -*-
from multiprocessing import Process

from core.proxy_api import ProxyApi
from core.proxy_spider.run_spiders import RunSpider
from core.proxy_test import ProxyTester

"""
开启三个进程，分别用于启动爬虫，检测代理IP，WEB服务
步骤：
    1.定义一个run方法用于启动代理池
        1.1 定义一个列表，用于存储要启动的进程
        1.2 创建 启动爬虫 的进程，添加到列表中
        1.3 创建 启动检测 的进程，添加到列表中
        1.4 创建 启动提供API服务 的进程， 添加到列表中
        1.5 遍历进程列表，启动所有进程
        1.6 遍历进程列表，让主进程等待子进程的完成
    2. 在 if__name__== "__main__" : 中调用run方法
"""



def run():
    # 1.1 定义一个列表，用于存储要启动的进程
    process_list = []
    # 1.2 创建启动爬虫 的进程，添加到列表中
    process_list.append(Process(target=RunSpider.start))
    # 1.3 创建 启动检测 的进程，添加到列表中
    process_list.append(Process(target=ProxyTester.start))
    # 1.4 创建 启动提供API服务的进程， 添加到列表中
    process_list.append(Process(target=ProxyApi.start))

    # 1.5 遍历进程列表，启动所有进程
    for process in process_list:
        process.daemon= True
        process.start()

    # 1.6 遍历进程列表，让主进程等待子进程的完成
    for process in process_list:
        process.join()


if __name__ == '__main__':
    run()







