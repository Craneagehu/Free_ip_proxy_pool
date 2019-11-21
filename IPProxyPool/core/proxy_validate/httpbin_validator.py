#-*- coding:utf-8 -*-
import time
import requests
from utils.http import get_request_headers
from settings import TEST_TIMEOUT
from domain import Proxy
from utils.log import logger

def check_proxy(proxy):
    """
    用于检查指定 代理IP 响应速度，匿名程度，支持协议类型
    :param proxy:
    :return: 检查后的代理IP模型对象
    """
    #准备代理IP字典
    proxies = {
        "http":f"http://{proxy.ip}:{proxy.port}",
        "https":f"https://{proxy.ip}:{proxy.port}"
    }
    try:
        # 测试该代理IP
        http,http_nick_type,http_speed = __check_http_proxies(proxies)
        https,https_nick_type,https_speed = __check_http_proxies(proxies,False)

        if http and https:
            proxy.protocol = 2      #包含http和https
            proxy.nick_type = http_nick_type
            proxy.speed = http_speed
        elif http:
            proxy.protocol=0        #包含http
            proxy.nick_type = http_nick_type
            proxy.speed = http_speed
        elif https:
            proxy.protocol = 1      #包含https
            proxy.nick_type = https_nick_type
            proxy.speed = https_speed

        else:
            proxy.protocol = -1
            proxy.nick_type = -1
            proxy.speed = -1
        return proxy
    except Exception as e:
        logger.exception(e)

def __check_http_proxies(proxies,is_http=True):
    #匿名类型
    nick_type = -1
    #响应速度
    speed = -1
    if is_http:
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    try:
        #获取开始时间
        start = time.time()
        #发送请求，获取响应数据
        response = requests.get(test_url,headers = get_request_headers(),proxies=proxies,timeout = TEST_TIMEOUT)
        if response.ok:
            #计算响应速度
            speed = round(time.time()-start,2)
            #转换成python字典
            dic = response.json()
            #获取来源IP:origin
            origin = dic["origin"]
            proxy_connection = dic["headers"].get("Proxy-Connection")
            if ',' in origin:
                # 1.如果响应的origin中有 ',' 分割的两个ip就是透明代理
                nick_type = 2
            elif proxy_connection:
                # 2.如果响应的的headers中包含 Proxy_Connection说明是匿名代理
                nick_type = 1
            else:
                # 3.否则就是高匿代理ip
                nick_type = 0
            return True,nick_type,speed
        return False,nick_type,speed

    except Exception as e:
        print(f'请求失败: {e}')
        # logger.exception(e)
        return False,nick_type,speed


if __name__ == '__main__':
    proxy = Proxy('14.207.175.80',port = '8213')
    print(proxy)
    print(check_proxy(proxy))