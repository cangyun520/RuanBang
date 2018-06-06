from utils.webClass import *


class SalesAnalysis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.submit(self)
        driver = self.driver
        # 打开菜单
        WebMenu.full_text(self, "客户关系", "售前管理", "销售机会分析")
        # 移动到页面底部，防止对象遮挡
        WebForm.top(self, 0)
        driver.switch_to.frame("frame_tab_PM001074")

    '''客户关系-销售管理-销售机会分析查询所有'''
    def test_1204_01_query(self):
        """客户关系-竞争对手维护--销售机会分析查询所有"""
        driver = self.driver
        # 清空
        driver.find_element_by_id("Button2").click()
        time.sleep(1)
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        v_list = driver.find_elements_by_link_text("详细")
        v_list[0].click()
        time.sleep(4)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000316")
        v_goto = driver.find_element_by_id("btnGoOCRD")
        if v_goto.is_displayed():
            print("点击‘详细’可穿透查看源单据")
        else:
            print("BUG, 点击‘详细’查看源单据异常")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    """# 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Competitor("test_1201_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)
    """