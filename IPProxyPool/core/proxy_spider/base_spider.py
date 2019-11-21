#-*- coding:utf-8 -*-
import requests
from domain import Proxy
from utils.http import get_request_headers
from lxml import etree

class BaseSpider(object):
    # urls=[]
    # group_xpath = ''
    # datail_xpath = {}

    # 提供初始方法，传入URL列表，分组xpath,详情（组内）XPATH
    def __init__(self,urls =[],group_xpath='',detail_xpath={}):

        if urls:
            self.urls = urls

        if group_xpath:
            self.group_xpath = group_xpath

        if detail_xpath:
            self.detail_xpath = detail_xpath

    def get_page_from_url(self,url):
        response = requests.get(url,headers=get_request_headers())
        return response.content

    def get_proxies_from_page(self,page):
        element = etree.HTML(page)
        # 获取包含代理IP信息的标签列表
        trs = element.xpath(self.group_xpath)
        # 遍历trs，获取代理IP相关信息
        for tr in trs:
            ip = tr.xpath(self.detail_xpath["ip"])[0]
            port = tr.xpath(self.detail_xpath["port"])[0]
            area = tr.xpath(self.detail_xpath["area"])  # 注：有的没有区域，需要进行判断
            if area:
                area = area[0]
            else:
                area=""
            proxy = Proxy(ip,port,area=area)
            yield proxy

    def get_proxies(self):
        # 遍历URL列表，获取URL
        for url in self.urls:
            # 根据发送请求，获取页面数据
            page = self.get_page_from_url(url)
            # 解析页面，提取数据，封装为Proxy对象
            proxies = self.get_proxies_from_page(page)
            # 返回Proxy对象列表
            yield from proxies


if __name__ == '__main__':
    config = {
        "urls": [f"http://www.ip3366.net/?stype=1&page={i}" for i in range(1,4)],
        "group_xpath" : "//*[@id='list']/table/tbody/tr",
        "detail_xpath":{
            "ip": './td[1]/text()',
            "port": './td[2]/text()',
            "area": './td[6]/text()'
        }
    }

    spider = BaseSpider(**config)
    for proxy in spider.get_proxies():
        print(proxy)



