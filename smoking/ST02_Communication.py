# -*- coding: utf-8 -*-
from utils.webClass import *

class ST02_Communication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

# #------沟通交流模块------
    def test_0201_Note(self):
        """沟通交流-消息中心-【收信】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "沟通交流", "消息中心")
        driver.switch_to_frame("frame_tab_PM000416")
        v_receive = driver.find_element_by_id("btnReceive")
        try:
            v_receive.is_displayed()
            print("消息中心-显示正常")
        except ImportError:
             print("BUG 消息中心-【收信】不显示")
             unittest.expectedFailure("test_0201_Note")

    def test_0203_Mobile_SendMessage(self):
        """沟通交流-发短信-【选择系统用户】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "沟通交流", "手机短信", "发短信")
        driver.switch_to_frame("frame_tab_PM001047")
        v_selectProfile = driver.find_element_by_link_text("选择系统用户")
        try:
            v_selectProfile.is_displayed()
        except ImportError:
            print("BUG ‘选择系统用户’不显示")
        else:
            print("发短信页面-显示正常")

    def test_0204_Mobile_MessageRecord(self):
        """沟通交流-短信发送记录-【查询】检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "沟通交流", "手机短信", "短信发送记录")
        driver.switch_to_frame("frame_tab_PM001006")
        MessageRecord_Seach = driver.find_element_by_id("btnSearch")
        try:
            MessageRecord_Seach.is_displayed()
        except ImportError:
            print("BUG 短信发送记录页面【查询】不显示")
        else:
            print("短信发送记录页面-显示正常")
        MessageRecord_Seach.click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ST02_Communication("test_0201_Note"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)