import logging

#在配置文件:settings.py中丁一MAX_SCORE=50,表示代理IP的默认最高分数
MAX_SCORE=50
TEST_TIMEOUT=10

#默认日志的配置
LOG_LEVEL = logging.DEBUG  # 默认等级
LOG_FMT = '%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s' # 自定义日志的输出格式，这个格式可以被文件输出流和控制台输出流调用；
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'    # 默认时间格式
LOG_FILENAME = 'log.log'    # 默认日志文件名称

# MongoDB数据库的URL
MONGO_URL = 'mongodb://127.0.0.1:27017'

PROXIES_SPIDERS = [
    # 爬虫的全类名，路径：模块.类名
    'core.proxy_spider.proxy_spiders.XiciSpider',
    'core.proxy_spider.proxy_spiders.Ip3366Spider',
    'core.proxy_spider.proxy_spiders.KuaiSpider',
    'core.proxy_spider.proxy_spiders.ProxylistplusSpider',
    'core.proxy_spider.proxy_spiders.Ip66Spider'
]
# 配置爬虫间隔时间
RUN_SPIDERS_INTERVAL = 12

# 配置检测代理IP的异步数量
TEST_PROXIES_ASYNC_COUNT = 10

# 配置检测代理IP的时间间隔
TEST_PROXIES_INTERVAL = 3

# 配置获取的代理IP最大数量，这个值越小，可用性越高；但是随机性越差
PROXIES_MAX_COUNT = 50