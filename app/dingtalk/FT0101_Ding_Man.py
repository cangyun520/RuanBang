# encoding:utf-8
from public.dingTalkClass import *
import random
from public.getData import *


class BusinessMan(unittest.TestCase):
    def setUp(self):
        # 调用钉钉初始化公共方法
        desired_caps = DingTalk.start_ding(self)
        # 引用Appium_Python_Client
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        dr = self.driver

        try:
            dr.find_element_by_name("工作").click()
        except Exception as err:
            print(err)

    """钉钉-页面检查"""
    def test_0101_01_check(self):
        """钉钉-页面检查"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_id("menu_current_company").click()
        dr.find_element_by_name("源钉云测试").click()
        timesl(1)
        try:
            dr.find_element_by_name("常用应用").is_displayed()
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_01_check.jpg")
            unittest.expectedFailure("test_0101_01_check")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

