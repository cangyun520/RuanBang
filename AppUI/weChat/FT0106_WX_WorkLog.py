# encoding:utf-8
import win32api
import win32con


class WorkLog(unittest.TestCase):
    # noinspection PyUnresolvedReferences
    def setUp(self):
        # 调用微信初始化公共方法
        desired_caps = WeChatPublic.start_weixin(self)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)

        try:
            self.driver.find_element_by_name("OnlineBox产品").click()
        except Exception as err:
            print(err)
        self.driver.find_element_by_name("工作日志").click()
        timesl(3)
        # 全局变量
        global v_time
        v_time = time.strftime("%Y-%m-%d %H:%M:%S")

    """工作日志-添加日志-日报"""

    # noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
    def test_0106_01_addDaily(self):
        """工作日志-添加日志-日报"""
        driver = self.driver

        driver.find_element_by_name("工作日志").click()
        timesl(1)
        driver.find_element_by_name("添加日志").click()
        timesl(1)
        driver.find_element_by_name("日报").click()
        timesl(5)
        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 1)
        driver.find_element_by_id("ajp").click()
        # 自由流选择审批用户
        driver.find_element_by_accessibility_id("汇报人*").click()
        timesl(3)
        driver.find_element_by_accessibility_id("Bear-技术经理（微信）").click()
        driver.find_element_by_accessibility_id("Sunny-技术总监").click()
        # 其中键盘输入，tab定位
        driver._switch_to.context("NATIVE_APP")
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        timesl(2)

        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 0)
        timesl(1)
        v_edit = driver.find_elements_by_class_name("android.widget.EditText")
        # 明日计划
        driver.find_element_by_id("ajp").click()
        v_edit[1].send_keys(data_character(10, 150))
        # 需协调工作
        # 其中键盘输入，tab定位
        win32api.keybd_event(9, 0, 0, 0)
        # 释放按键
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        v_edit[2].send_keys(data_character(100, 300))
        # 今日完成
        win32api.keybd_event(9, 0, 0, 0)
        # 释放按键
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(9, 0, 0, 0)
        # 释放按键
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        v_edit[0].send_keys('Arvin-日报-今日完成微信提交 ' + v_time)

        # 上下滑动屏幕
        driver.swipe(0, 0, 0, 1)
        timesl(1)

        driver.find_element_by_accessibility_id("添加 Link").click()
        timesl(3)
        print(driver.contexts)
        driver._switch_to.context("NATIVE_APP")

        try:
            driver.find_element_by_accessibility_id("添加成功").is_displayed()
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(propath() + "picture/WeChat/test_0106_01_addDaily.jpg")
            unittest.expectedFailure("test_0106_01_addDaily")

    """工作日志-我发出的-页面检查"""
    def test_0106_05_check(self):
        """工作日志-我发出的-页面检查"""
        driver = self.driver

        driver.find_element_by_name("工作日报").click()
        timesl(1)
        driver.find_element_by_name("我发出的").click()
        timesl(5)
        try:
            driver.find_element_by_id("android:id/text1")
        except Exception as err:
            print(err)
            driver.get_screenshot_as_file(propath() + "picture/WeChat/test_0106_05_check.jpg")
            unittest.expectedFailure("test_0106_05_check")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
