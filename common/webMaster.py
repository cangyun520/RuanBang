# encoding:utf-8
from config.config import *
import unittest
from selenium import webdriver


class WebLogin(object):
    """初始测试准备工作"""
    @staticmethod
    def __url(self, url):
        # 环境URL地址
        driver = self.driver
        # 浏览器最大化
        driver.maximize_window()
        # 通过yaml公共方法，获取配置文件地址。get后续get获取2级目录数据
        _url = Config().get('url').get(url)
        driver.get(_url)
        time.sleep(2)

    @staticmethod
    def __user(self, uname, password, tenantid=None):
        """用户登录"""
        driver = self.driver
        if driver.find_element_by_id('txtTenantId').is_displayed():
            driver.find_element_by_id('txtTenantId').clear()
            driver.find_element_by_id('txtTenantId').send_keys(tenantid)
        driver.find_element_by_id("txtCode").clear()
        driver.find_element_by_id("txtCode").send_keys(uname)
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)

    @staticmethod
    def __masterUser(self, user, passwd):
        """用户登录"""
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(passwd)
        elements = driver.find_elements_by_tag_name("span")
        for i in elements:
            if i.text == '登 录':
                # print(i.text)
                i.click()
                break
        time.sleep(2)

    # 主数据登录页面
    """
    @url        : 应用的登录地址
    @ucode      : 用户登录id一般为电话号码
    @upasswd    : 用户登录密码
    """

    @staticmethod
    def master_login(self, url, user, passwd):
        # self.driver = webdriver.Chrome()
        # 设置页面上隐形的智能等待时间30秒
        self.driver.implicitly_wait(20)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        # 打开浏览器
        WebLogin.__url(self, url)
        # 用户登录
        WebLogin.__masterUser(self, user, passwd)


class MenuOpen(object):
    """打开导航栏2级菜单"""
    @staticmethod
    def menu_full(self, name):
        # 全名称菜单
        if name != "":
            menus = self.driver.find_elements_by_class_name("ant-menu-item")
            for i in menus:
                print(i.text)
                print(len(menus))
                if i.text == name:
                    i.click()
                    break
            time.sleep(1)

    @staticmethod
    def menu_part(self, *name):
        # 关键字名称菜单
        if name != "":
            for i in name:
                self.driver.find_element_by_partial_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(1)

    @staticmethod
    def menu_top_full(self, name):
        # 全名称菜单
        names = self.driver.find_elements_by_class_name("ant-menu-submenu-title")
        for i in names:
            if i.text == name:
                i.click()
                break


class ObjectPc(object):
    """点击指定某一个按钮"""
    @staticmethod
    def button(self, text):
        buttons = self.driver.find_elements_by_tag_name('button')
        for i in buttons:
            if i.text == text:
                i.click()
                break
        timesl(2)