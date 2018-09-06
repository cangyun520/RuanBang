# encoding:utf-8
from public.dingTalkClass import *
import random
from public.getData import *
import uiautomator2 as u2
from public.log import logger


class BusinessMan(unittest.TestCase):
    def setUp(self):
        # 调用钉钉初始化公共方法
        desired_caps = DingTalk.start_read5_ding(self)
        # 引用Appium_Python_Client
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        if self.driver.find_element_by_name("工作").is_displayed():
            self.driver.find_element_by_name("工作").click()
        elif self.driver.find_element_by_name("软邦科技").is_displayed():
            self.driver.find_element_by_name("软邦科技").click()

        _com = self.driver.find_element_by_id("menu_current_company").text
        if _com == "深圳市软邦科技有限公司":
            pass
        else:
            self.driver.find_element_by_id("menu_current_company").click()
            self.driver.find_element_by_name("深圳市软邦科技有限公司").click()
        timesl(2)

    """主页-签到"""
    def test_0101_01_sign(self):
        """主页-签到"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("扶贫签到扶贫签到").click()
        timesl(2)
        try:
            dr.find_element_by_name("拜访对象").is_displayed()
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_01_sign.jpg")
            unittest.expectedFailure("test_0101_01_sign")

    """主页-扶贫日志"""
    def test_0101_02_log(self):
        """主页-日志"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("扶贫日志扶贫日志").click()
        timesl(2)
        try:
            dr.find_element_by_name("写日志").is_displayed()
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_02_log.jpg")
            unittest.expectedFailure("test_0101_02_log")

    """主页-钉盘"""
    def test_0101_03_disk(self):
        """主页-日志"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("钉盘钉盘").click()
        timesl(2)
        try:
            dr.find_element_by_name("我的文件").is_displayed()
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_03_disk.jpg")
            unittest.expectedFailure("test_0101_03_disk")

    """主页-日志"""
    def test_0101_04_approve(self):
        """主页-日志"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("审批审批").click()
        timesl(2)
        try:
            dr.find_element_by_name("我审批的").is_displayed()
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_04_approve.jpg")
            unittest.expectedFailure("test_0101_04_approve")

    """主页-广告"""
    def test_0101_05_banner(self):
        """主页-日志"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("贵州红渡").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_05_banner.jpg")
            unittest.expectedFailure("test_0101_05_banner")

    """主页-攻坚风采"""
    def test_0101_06_show(self):
        """主页-攻坚风采"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("攻坚风采").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "脱贫攻坚" in _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_06_show.jpg")
            unittest.expectedFailure("test_0101_06_show")

    """主页-公告"""
    def test_0101_07_note(self):
        """主页-公告"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("公告").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "公告" in _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_07_note.jpg")
            unittest.expectedFailure("test_0101_07_note")

    """主页-政策"""
    def test_0101_08_policy(self):
        """主页-公告"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("政策").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "脱贫攻坚" in _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_08_policy.jpg")
            unittest.expectedFailure("test_0101_08_policy")

    """主页-电话会议"""
    def test_0101_09_mobileMet(self):
        """主页-电话会议"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("电话会议").click()
        timesl(2)
        try:
            dr.find_element_by_name("钉钉电话会议").is_displayed()
            print(dr.find_element_by_name("钉钉电话会议").text)
            logger.info(dr.find_element_by_name("钉钉电话会议").text)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_09_mobileMet.jpg")
            unittest.expectedFailure("test_0101_09_mobileMet")

    """主页-视频会议"""
    def test_0101_10_videoMet(self):
        """主页-视频会议"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("视频会议").click()
        timesl(2)
        _name = dr.find_element_by_id("tv_empty_title").text
        try:
            "视频会议" in _name
            print(_name)
            logger.info(_name)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_10_videoMet.jpg")
            unittest.expectedFailure("test_0101_10_videoMet")

    """主页-基本情况"""
    def test_0101_11_basic(self):
        """主页-基本情况"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("基本情况").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "基本情况" in _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_11_basic.jpg")
            unittest.expectedFailure("test_0101_11_basic")

    """主页-政策"""
    def test_0101_12_power(self):
        """主页-帮扶力量"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("帮扶力量").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "帮扶力量" in _title
            print(_title)
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_05_banner.jpg")
            unittest.expectedFailure("test_0101_05_banner")

    """主页-帮扶计划"""
    def test_0101_13_plan(self):
        """主页-帮扶计划"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("帮扶计划").click()
        timesl(2)
        _title = dr.find_element_by_id("title").text
        try:
            "帮扶计划" in _title
            logger.info(_title)
        except Exception as err:
            print(err)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_05_banner.jpg")
            unittest.expectedFailure("test_0101_05_banner")

    """主页-百度一下"""
    def test_0101_14_baidu(self):
        """主页-百度一下"""
        dr = self.driver
        # 进入到页面
        dr.find_element_by_name("百度一下百度一下").click()
        timesl(2)
        try:
            dr.find_element_by_name("百度一下").is_displayed()
        except Exception as e:
            logger.info(e)
            dr.get_screenshot_as_file(PICTURE_PATH + "/dingtalk/test_0101_01_sign.jpg")
            unittest.expectedFailure("test_0101_01_sign")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

