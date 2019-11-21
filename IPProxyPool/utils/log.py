#_*_coding:utf-8_*_
import logging
import sys
from settings import LOG_FMT,LOG_DATEFMT,LOG_FILENAME,LOG_LEVEL
'''
 Python使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
     1>.logger提供了应用程序可以直接使用的接口；
     2>.handler将(logger创建的)日志记录发送到合适的目的输出；
     3>.filter提供了细度设备来决定输出哪条日志记录；
     4>.formatter决定日志记录的最终输出格式。
 '''


class Logger(object):

    def __init__(self):
        # 1. 创建一个logger对象，它提供了应用程序可以直接使用的接口，其类型为“<class 'logging.RootLogger'>”；
        self._logger = logging.getLogger()
        # 2. 设置format对象
        self.formatter = logging.Formatter(fmt=LOG_FMT,datefmt=LOG_DATEFMT)
        # 3. 设置日志输出
        # 3.1 设置文件日志模式
        self._logger.addHandler(self._get_file_handler(LOG_FILENAME))
        # 3.2 设置终端日志模式
        self._logger.addHandler(self._get_console_handler())
        # 4. 设置日志等级
        self._logger.setLevel(LOG_LEVEL)

    def _get_file_handler(self,filename):
        # 1. 获取一个文件日志handler
        filehandler = logging.FileHandler(filename=filename,encoding="utf-8")
        # 2. 设置日志格式
        filehandler.setFormatter(self.formatter)
        # 3. 返回
        return filehandler


    def _get_console_handler(self):
        '''
        :return: 返回一个输出到终端日志handler
        '''
        # 1. 获取一个输出到终端日志handler
        console_handler = logging.StreamHandler(sys.stdout)
        # 2. 设置日志格式
        console_handler.setFormatter(self.formatter)
        # 3. 返回handler
        return console_handler

    @property
    def logger(self):
        return self._logger

# 初始化并配一个logger对象，到达单例的
# 使用时，直接导入logger就可以使用
logger = Logger().logger

if __name__ == '__main__':
    logger.debug("调试信息")
    logger.info("状态信息")
    logger.warning("警告信息")
    logger.error("错误信息")
    logger.critical("严重错误信息")














