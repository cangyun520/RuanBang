from selenium import webdriver
from public.config import *
from public.getData import *
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebLogin:
    """初始测试准备工作"""
    def __url(self):
        # 环境URL地址
        driver = self.driver
        # 浏览器最大化
        driver.maximize_window()
        # 获取配置文件地址
        v_url = Config.url_test()
        driver.get(v_url)
        time.sleep(2)

    def __user(self, uname, password):
        """用户登录"""
        driver = self.driver
        driver.find_element_by_id("txtCode").clear()
        driver.find_element_by_id("txtCode").send_keys(uname)
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)

    def submit(self):
        driver = self.driver
        # 设置页面上隐形的智能等待时间30秒
        self.driver.implicitly_wait(20)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        # 打开浏览器
        WebLogin.__url(self)
        # 用户登录
        WebLogin.__user(self, "0KOF1MVY04089AD2DQLO", '0KOF1MVY04089AD2DQLO')


class WebMenu:
    """打开菜单连接"""
    def full_text(self, *v_menu):
        # 全名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(2)

    def part_text(self, *v_menu):
        # 关键字名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_partial_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(3)


class WebForm:
    """js移动到页面顶部，防止对象遮挡"""
    def top(self, number):
        # js移动到页面顶部，防止对象遮挡
        js_top = "window.scrollTo(0," + str(number) + ")"
        self.driver.execute_script(js_top)

    '''表头弹出时间控件选择【今天】'''
    def today(self, uid):
        # 选择当天日期
        self.driver.find_element_by_id(uid).click()
        for i in self.driver.find_elements_by_tag_name("button"):
            if i.text == "今天":
                i.click()
                break
        time.sleep(1)