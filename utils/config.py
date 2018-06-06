import os
import time
import csv
import random
# 导入测试报告
from HTMLTestRunner import HTMLTestRunner
# 读取配置文件
import configparser


# 获取当前项目根目录
def propath(prjname="RuanBang"):
    v_path = os.getcwd()
    v_thepath = v_path[:v_path.find(prjname)] + prjname + "/"
    return v_thepath


class UrlTest:
    # 修改当前测试URL地址
    def testurl_pc(self):
        config = configparser.ConfigParser()
        config.read(config)
        self.testUrl = config['url']['testUrl']
        return self.testUrl


# 休眠时间
def timesl(num):
    if 0 < num < 50:
        time.sleep(num)
    else:
        print("休眠时间非 大于0，小于50，请重新设置")


# https://blog.csdn.net/huilan_same/article/details/76572428