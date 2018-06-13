from public.config import *
from public.getData import *
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebLogin:
    """初始测试准备工作"""
    def __url(self):
        # 环境URL地址
        driver = self.driver
        v_url = UrlTest.pc()
        # driver.set_window_size(420, 700)
        driver.maximize_window()
        driver.get(v_url)
        time.sleep(2)

    def __user(self, uname):
        """用户登录"""
        log_file = open(propath() + 'data/text/LogName.txt', 'r')

        # 读取所有行数据，并匹配当前登陆用户
        for i in log_file.readlines():
            try:
                uname in i
                break
            except Exception as err:
                print(err)

        driver = self.driver
        password = 123456
        driver.find_element_by_id("user_login").clear()
        driver.find_element_by_id("user_login").send_keys(uname)
        driver.find_element_by_id("user_pass").clear()
        driver.find_element_by_id("user_pass").send_keys(password)
        driver.find_element_by_id("btn_Login").click()
        time.sleep(3)
        if driver.find_element_by_id("tab_home").is_displayed():
            driver.find_element_by_id("tab_home").click()
        else:
            driver.refresh()
            time.sleep(2)
        # 关闭读取，及时释放
        log_file.close()

    def submit(self):
        # 设置页面上隐形的智能等待时间30秒
        self.driver.implicitly_wait(20)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        time.sleep(1)
        # 打开菜单
        WebLogin.__url(self)
        # 用户登录
        WebLogin.__user(self, "admin")


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
        time.sleep(3)

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

    '''行弹出时间控件选择【今天】'''
    def line(self, uid):
        # 选择当天日期
        self.driver.find_element_by_id(uid).click()
        for i in self.driver.find_elements_by_tag_name("button"):
            if i.text == "今天":
                i.click()
                break


class WebPopupWindow:
    """表头弹出窗体数据选择"""
    def project(self):
        # 项目弹出窗体数据选择
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='ProjectCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to_frame("winAdd_IFrame")
        v_projectlist = driver.find_elements_by_class_name("x-grid3-row")
        v_projectlist[random.randint(0, (len(v_projectlist) - 1))].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
