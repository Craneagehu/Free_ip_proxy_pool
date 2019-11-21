# -*- coding:utf-8 -*-
import time
import random
from base_spider import BaseSpider

"""
1. 实现西刺代理爬虫：https://www.xicidaili.com/nn/4	
    定义一个类，继承通用爬虫类（BaseSpider）
    提供urls，group_xpath 和 detaili_xpath
"""
class XiciSpider(BaseSpider):
    # 准备URL列表
    urls = [f"https://www.xicidaili.com/nn/{i}" for i in range(1,2)]

    # 分组XPATH，用于获取包含代理IP信息的标签列表
    group_xpath = '//*[@id="ip_list"]/tr[position()>1]'
    # 组内的XPATH，用于提取ip,port,area
    detail_xpath = {
        "ip": './td[2]/text()',
        "port": './td[3]/text()',
        "area": './td[4]/a/text()'
    }


"""
2. 实现云代理爬虫: http://www.ip3366.net/free/?stype=1&page=2
    定义一个类，继承通用爬虫类（BaseSpider）
    提供urls，group_xpath 和 detaili_xpath
"""
class Ip3366Spider(BaseSpider):
    # 准备URL列表
    urls = [f"http://www.ip3366.net/free/?stype={i}&page={j}" for i in range(1,4,2) for j in range(1,8)]    # stype=1表示国内匿名代理，stype=3表示国外匿名代理
    # 分组XPATH，用于获取包含代理IP信息的标签列表
    group_xpath = '//*[@id="list"]/table/tbody/tr'
    # 组内的XPATH，用于提取ip,port,area
    detail_xpath = {
        "ip": './td[1]/text()',
        "port": './td[2]/text()',
        "area": './td[5]/text()'
    }


"""
3. 实现proxylistplus代理爬虫: https://www.kuaidaili.com/free/inha/2/
    定义一个类，继承通用爬虫类（BaseSpider）
    提供urls，group_xpath 和 detaili_xpath
"""
class KuaiSpider(BaseSpider):
    # 准备URL列表
    urls = [f"https://www.kuaidaili.com/free/inha/{i}/" for i in range(1,2)]
    # 分组XPATH，用于获取包含代理IP信息的标签列表
    group_xpath = '//*[@id="list"]/table/tbody/tr'
    # 组内的XPATH，用于提取ip,port,area
    detail_xpath = {
        "ip": './td[1]/text()',
        "port": './td[2]/text()',
        "area": './td[5]/text()'
    }

    # 当我们两个也米娜时间间隔太短了，就报错了，这是一种反爬手段
    # 我们需要重写父类构造方法，间隔请求页面
    def get_page_from_url(self,url):
        time.sleep(random.uniform(1,3))
        return super().get_page_from_url(url)   # 先调用子类构造方法,再调用父类构造方法


"""
4. 实现快代理爬虫: https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-2
    定义一个类，继承通用爬虫类（BaseSpider）
    提供urls，group_xpath 和 detaili_xpath
"""
class ProxylistplusSpider(BaseSpider):
    # 准备URL列表
    urls = [f"https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{i}" for i in range(1,2)]
    # 分组XPATH，用于获取包含代理IP信息的标签列表
    group_xpath = '//*[@id="page"]/table[2]/tr[position()>2]' # 从第三个tr开始才有数据
    # 组内的XPATH，用于提取ip,port,area
    detail_xpath = {
        "ip": './td[2]/text()',
        "port": './td[3]/text()',
        "area": './td[5]/text()'
    }

    # 当我们两个也米娜时间间隔太短了，就报错了，这是一种反爬手段
    # 我们需要重写父类构造方法，间隔请求页面
    def get_page_from_url(self, url):
        time.sleep(random.uniform(1, 3))
        return super().get_page_from_url(url)  # 先调用子类构造方法,再调用父类构造方法


"""
5. 实现ip66代理爬虫: http://www.66ip.cn/2.html
    定义一个类，继承通用爬虫类（BaseSpider）
    提供urls，group_xpath 和 detaili_xpath
"""
class Ip66Spider(BaseSpider):
    # 准备URL列表
    urls = [f"http://www.66ip.cn/{i}.html" for i in range(1,3)]
    # 分组XPATH，用于获取包含代理IP信息的标签列表
    group_xpath = '//*[@id="main"]/div/div[1]/table/tr[position()>1]'
    # 组内的XPATH，用于提取ip,port,area
    detail_xpath = {
        "ip": './td[1]/text()',
        "port": './td[2]/text()',
        "area": './td[3]/text()'
    }


if __name__ == '__main__':
    spider = XiciSpider()
    #spider = Ip3366Spider()
    # spider = ProxylistplusSpider()
    #spider = Ip66Spider()
    for proxy in spider.get_proxies():
        print(proxy)


