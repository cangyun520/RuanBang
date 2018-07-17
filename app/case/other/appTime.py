# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-12.
点金 时间筛选
"""

from public.webClass import *
from selenium.webdriver.chrome.options import Options


class ProjectChange(unittest.TestCase):
    def setUp(self):
        mobile_emulation = {"deviceName": "iPhone 5"}
        option = Options()
        option.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options = option)

        dr = self.driver
        dr.maximize_window()
        url = "https://app2.shuibeidianjin.com"
        dr.get(url)
        time.sleep(2)
        dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/div[5]").click()
        timesl(2)
        dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div").click()
        timesl(1)
        mobile = dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div/input")
        mobile.click()
        mobile.send_keys("13345678900")
        timesl(1)
        pwd = dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/div[2]/div/input")
        pwd.click()
        pwd.send_keys("asdfghjkl123")
        timesl(1)

        buttons = dr.find_elements_by_class_name("name")
        for i in buttons:
            if i.text == "登录":
                i.click()
                break
        timesl(1)

    # 交易订单
    def test_timesearch(self):
        """时间查询"""
        dr = self.driver
        spans = dr.find_elements_by_class_name("title")
        for i in spans:
            if i.text == "交易订单":
                i.click()
                break
        timesl(1)
        dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[1]/div/div[2]/div[1]").click()
        timesl(1)
        # 循环点击
        n = 0
        startdates = dr.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]")
        while n < 1000:
            startdates.click()
            timesl(1)

            t1 = dr.find_elements_by_class_name("name")
            t1 = len(t1)

            dr.find_element_by_xpath("//*[@id='app']/div[2]/div[2]").click()
            timesl(1)

            t2 = dr.find_elements_by_class_name("name")
            t2 = len(t2)

            if t1-t2:
                pass
            else:
                dr.get_screenshot_as_file(propath() + "picture/webPc/test_timesearch.png")
                print(dr.current_url)
                unittest.expectedFailure("test_timesearch")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()