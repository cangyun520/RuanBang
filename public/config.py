# encoding:utf-8
import os
import time
import configparser


# 获取当前项目根目录
def propath(prjname="RuanBang"):
    """
    param prjname:
    return:
    """
    v_path = os.getcwd()
    v_thepath = v_path[:v_path.find(prjname)] + prjname + "/"
    return v_thepath


class Config(object):
    """
    配置文件
    """

    @staticmethod
    def url_test():
        cf = configparser.ConfigParser()
        cf.read(propath() + 'config\config.ini')
        return cf.get('url', 'url_test')

    @staticmethod
    def url_online():
        cf = configparser.ConfigParser()
        cf.read(propath() + 'config\config.ini')
        return cf.get('url', 'url_online')


# 休眠时间
def timesl(num):
    if 0 < num < 50:
        time.sleep(num)
    else:
        print("休眠时间非 大于0，小于50，请重新设置")


"""
参考资料
https://www.cnblogs.com/feeland/p/4514771.html
Python中的self,cls参数
https://blog.csdn.net/nyist327/article/details/47679771
"""