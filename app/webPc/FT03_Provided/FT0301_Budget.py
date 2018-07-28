# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *
from public.config import *
import re


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "数据填报", "预算")

    """预算-保存"""
    def test_0301_01_save(self):
        """预算-保存"""
        dr = self.driver
        SAASPc.buttons(self, "保存")
        _tip = SAASPc.get_tip(self)
        if "保存成功" in _tip:
            print(_tip)
            logger.info(_tip)
        else:
            dr.get_screenshot_as_file(REPORT_PATH + "webPc/test_0301_01_save.png")
            unittest.expectedFailure("test_0301_01_save")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
