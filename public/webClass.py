# encoding:utf-8
from selenium import webdriver
from public.config import *
from public.getData import *
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from public.log import logger


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
    def __user(self, uname, password):
        """用户登录"""
        driver = self.driver
        driver.find_element_by_id("txtCode").clear()
        driver.find_element_by_id("txtCode").send_keys(uname)
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)

    @staticmethod
    def submit(self, url, uname):
        # 设置页面上隐形的智能等待时间30秒
        self.driver.implicitly_wait(20)
        # 定义空verificationErrors数组，脚本运行错误信息被记录到整个数组中
        self.verificationErrors = []
        # 是否接受下一个警告，默认为是
        self.accept_next_alert = True
        # 打开浏览器
        WebLogin.__url(self, url)
        # 用户登录
        # WebLogin.__user(self, "0KOF1MVY04089AD2DQLO", '0KOF1MVY04089AD2DQLO')
        password = uname
        WebLogin.__user(self, uname, password)



class WebMenu(object):
    """打开导航栏菜单"""
    @staticmethod
    def full_text(self, *v_menu):
        # 全名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(2)

    @staticmethod
    def part_text(self, *v_menu):
        # 关键字名称菜单
        if v_menu != "":
            for i in v_menu:
                self.driver.find_element_by_partial_link_text(i).click()
                time.sleep(1)
        else:
            pass
        time.sleep(2)


class SAASPc(object):
    """js移动到页面顶部，防止对象遮挡"""
    def top(self, number):
        # js移动到页面顶部，防止对象遮挡
        js_top = "window.scrollTo(0," + str(number) + ")"
        self.driver.execute_script(js_top)

    """获取当前页面编号wid"""
    @staticmethod
    def get_wid(self):
        """
        param self:
        param modu:页面区域
        param obj : 具体控件对象
        return:
        """
        url = self.driver.current_url
        url = url.split('=')
        if len(url) > 1:
            url = url[1]
            url = url.split('&')
            wid = url[0]
            return wid
        else:
            wid = "w0"
            return wid

    """获取当前页面编号wid,当页面出现2个wid时候"""
    @staticmethod
    def get_wid_body(self):
        wid = self.driver.find_element_by_class_name("body").get_attribute("id")
        return wid

    def set_value(self, value):
        jscode = "Rb.Pages.Page.s_pages['w0'].getControl('gridEdit')." \
                 "model.internalData[8].setValue('shortName', '" \
                 + value + "');"
        return self.driver.execute_script(jscode)




    def get_dada(self):
        jscode = "var data; Rb.Pages.Page.s_pages['w0'].getData({ id: '', mode: Rb.Data.DataModeEnum.singleTable, attachParams: {} }).done(function(result){data=result}); return data;"
        return self.driver.execute_script(jscode)

    """获取弹出框提示内容"""
    @staticmethod
    def get_tip(self):
        _tip = self.driver.find_element_by_class_name("rb-hint-popup").text
        logger.info(_tip)
        return _tip

    """获取控件下拉值区域ID"""
    @staticmethod
    def popup(self, modu, obj):
        wid = SAASPc.wid(self, modu, obj)
        return wid + "$popup"

    """点击指定某一个按钮"""
    @staticmethod
    def button(self, text, css="rb-button"):
        button = self.driver.find_elements_by_class_name(css)
        for b in button:
            if b.text == text:
                b.click()
                timesl(2)
                break

    """循环点击所有该按钮所有的"""
    @staticmethod
    def button_cycle(self, text, css="rb-row-button"):
        button = self.driver.find_elements_by_class_name(css)
        for b in button:
            if b.text == text:
                b.click()
                timesl(2)

    """检查当前列表是否有数据"""
    def checklist(self):
        pass