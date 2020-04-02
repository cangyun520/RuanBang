# encoding:utf-8
import os
import time
from common.fileReader import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。
# 支持linux和windows等不同的平台，用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
# 这是是全局变量
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
PUBLIC_PATH = os.path.join(BASE_PATH, 'public')
APPUI_PATH = os.path.join(BASE_PATH, 'AppUI')
EXTEND_PATH = os.path.join(BASE_PATH, 'extend')
APPINTERFACE_PATH = os.path.join(BASE_PATH, 'AppInterface')
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
IMG_PATH = os.path.join(PUBLIC_PATH, 'img\\')
DOWN_PATH = os.path.join(PUBLIC_PATH, 'down\\')
DATA_PATH = os.path.join(PUBLIC_PATH, 'data\\')
DRIVER_PATH = os.path.join(PUBLIC_PATH, 'drivers')
EXCEL_PATH = os.path.join(PUBLIC_PATH, 'excel\\')
COOKIE_PATH = os.path.join(PUBLIC_PATH, 'cookie\\')
SCREENSHOT_PATH = os.path.join(PUBLIC_PATH, 'screenshot\\')
JS_PATH = os.path.join(PUBLIC_PATH, 'js\\')


class Config(object):
    """
    配置文件
    """
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=1):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)


# 获取应用日志路径
def log_path_app(appname):
    return LOG_PATH + appname

# 获取屏幕截图应用路径
def screenshot_path_app(app):
    return SCREENSHOT_PATH + app

# 后去UI测试应用路径
def appui_path_app(app):
    return APPUI_PATH + app

# 休眠时间
def timesl(num):
    if 0 < num < 100:
        time.sleep(num)
    else:
        print("休眠时间非 大于0，小于100，请重新设置")



if __name__ == "__main__":
    print(BASE_PATH)
    print(log_path_app('wwww'))


"""
参考资料
https://www.cnblogs.com/feeland/p/4514771.html
Python中的self,cls参数
https://blog.csdn.net/nyist327/article/details/47679771
"""