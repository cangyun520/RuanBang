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

        try:
            self.driver.find_element_by_name("工作").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("业务管理首页").click()
        timesl(5)

    """钉钉-页面检查"""
    def test_0101_01_check(self):
        """钉钉-页面检查"""
        driver = self.driver

        v_an = driver.find_elements_by_class_name("android.view.View")
        # for i in v_an:
        #     print(i.id)
        v_an[3].click()
        timesl(3)

        # 进入到页面
        try:
            driver.find_element_by_name("客户管理").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_01_check.jpg")
            unittest.expectedFailure("test_0101_01_check")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

