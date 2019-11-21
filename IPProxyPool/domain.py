#-*- coding:utf-8 -*-
import requests
from settings import MAX_SCORE

class Proxy(object):

    def __init__(self,ip=None,port=None,protocol=-1,nick_type=-1,speed=-1,area=None,score = MAX_SCORE,disable_domains=[]):
        self.ip = ip    #代理ip
        self.port = port    #端口号
        self.protocol = protocol    #协议类型，http是0，https是1，两个都支持为2
        self.nick_type = nick_type  #匿名程度，高匿:0，匿名：1，透明：2
        self.speed = speed          #响应速度，单位s
        self.area = area            #代理ip所在区域
        self.score = score          #代理ip评分，衡量代理的可用性。没遇到一次请求失败就减1分，减到0的时候从池中删除，如果检查代理可用，就恢复默认分数
        self.disable_domains = disable_domains  #不可用域名列表

    # 提供__str__方法，返回字符串
    def __str__(self):
        return str(self.__dict__)



