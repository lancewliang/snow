import logging 
import time
from snow.config.fsdata_config import fs_config


def getLog(moduel, name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # 输出到屏幕
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 输出到文件
    fh = logging.FileHandler(fs_config['root'] + '/logs/' + moduel + '/' + name + '.' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.log')
    fh.setLevel(logging.DEBUG)
    # 设置日志格式
    fomatter = logging.Formatter('%(asctime)s-%(levelname)s-%(module)s:%(message)s')
    ch.setFormatter(fomatter)
    fh.setFormatter(fomatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
