# -*- coding: utf-8 -*-
from PubliCode.webClass import *


class DB02_Sales(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    # 业务设置-销售合同条款-合同条款添加
    def test_DB02_Sales_ContractAdd(self):
        """业务设置-销售合同条款-合同条款添加检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "采购设置", "销售设置", "销售合同条款")

        driver.switch_to.frame("frame_tab_PM000728")
        v_save = driver.find_element_by_id("btnSave")
        v_tim = time.strftime("%Y%m%d%H%M")
        if v_save.is_displayed():
            v_write_file = open(propath() + 'PubliData/character5K.txt', 'r')
            v_lines = v_write_file.read()
            driver.find_element_by_id("descrption").clear()
            driver.find_element_by_id("descrption").send_keys(v_tim + v_lines[500:2000])
            time.sleep(2)
            v_save.click()
            time.sleep(3)
            print("业务设置-销售设置-销售合同条款添加数据OK")
        else:
            print("BUG 业务设置-销售设置-销售合同条款添加数据错误")
            unittest.expectedFailure("test_DB02_Sales_ContractAdd")

    # 业务设置-销售设置-收款阶段设置
    def test_DB02_Sales_PhaseAdd(self):
        """业务设置-销售设置-收款阶段设置报警天数添加检查"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "采购设置", "销售设置", "收款阶段设置")

        driver.switch_to.frame("frame_tab_PM000726")
        v_add = driver.find_element_by_id("btnAdd")
        v_tim = time.strftime("%y%m%d%H%M")
        if v_add.is_displayed():
            v_add.click()
            time.sleep(2)
            driver.find_element_by_id("txtName").send_keys("付款名称Auto" + v_tim)
            driver.find_element_by_id("txtWarningDays").send_keys(random.randint(1, 100))
            driver.find_element_by_id("BtnSaveForm").click()
            time.sleep(3)
            print("业务设置-销售设置-收款阶段设置添加报警天数OK")
        else:
            print("BUG 业务设置-销售设置-收款阶段设置添加报警天数错误")
            unittest.expectedFailure("test_DB02_Sales_PhaseAdd")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
