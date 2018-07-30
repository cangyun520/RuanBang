from appium import webdriver
import unittest
from public.config import *


class DingTalk(object):
    """钉钉公共操作代码集合"""
    @staticmethod
    def start_ding(self):
        """初始化配置钉钉应用"""
        self.desired_caps = {}
        desired_caps = self.desired_caps
        # 使用哪种移动平台。iOS, Android, orFirefoxOS
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '6.0.0'
        # 启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...
        desired_caps['deviceName'] = '127.0.0.1:6555'
        # 待测试的app的java package
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        # 待测试的app的Activity名字
        desired_caps['appActivity'] = '.biz.home.activity.HomeActivity'
        # 解决无法输入中文问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # 使用哪种自动化引擎。appium（默认）还是Selendroid。api小于17使用Selendroid
        # self.desired_caps["automationName"] = "Selendroid"
        return desired_caps

    @staticmethod
    def start_read5_ding(self):
        """初始化配置钉钉应用"""
        self.desired_caps = {}
        desired_caps = self.desired_caps
        # 使用哪种移动平台。iOS, Android, orFirefoxOS
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '6.0.0'
        # 启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...
        desired_caps['deviceName'] = '94f997b49805'
        # 真机
        # 待测试的app的java package
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        # 待测试的app的Activity名字
        desired_caps['appWaitActivity'] = '.biz.home.activity.HomeActivity'
        desired_caps['appActivity'] = '.biz.home.activity.HomeActivity'
        # 解决无法输入中文问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # 使用哪种自动化引擎。appium（默认）还是Selendroid。api小于17使用Selendroid
        # self.desired_caps["automationName"] = "Selendroid"
        return desired_caps