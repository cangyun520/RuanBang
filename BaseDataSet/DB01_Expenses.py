
from PubliCode.webClass import *


class Expenses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)

    '''业务设置-费用设置-类型添加'''
    def test_DB01_01_ApplyAdd(self):
        """业务设置-费用设置-类型添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", u"系统管理", "业务设置", "销售设置", "费用设置", "报销类型设置")
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000762")
        driver.find_element_by_id("btnAdd").click()
        time.sleep(2)
        v_tim = time.strftime("%m%d%H%M")
        driver.find_element_by_id("Type").send_keys("费用类型" + v_tim)
        driver.find_element_by_id("Digest").send_keys("全选菜单Auto" + v_tim)
        # 关联菜单
        driver.find_element_by_xpath("//*[@id='x-form-el-MenuLink']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        v_check = driver.find_elements_by_class_name("x-grid3-row-checker")
        for i in v_check:
            i.click()
        time.sleep(1)
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 科目代码
        driver.find_element_by_xpath("//*[@id='x-form-el-AcctCode']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winTypeAdd_IFrame")
        driver.find_element_by_id("txtBPartners").send_keys("100201")
        driver.find_element_by_id("btnBPartners").click()
        time.sleep(1)
        for i in driver.find_elements_by_class_name("x-grid3-cell-inner"):
            i.click()
            break
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.find_element_by_id("BtnSaveForm").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            if "已存在" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_DB01_01_ApplyAdd")

    '''费用设置-财务设置-报销金额添加'''
    def test_DB01_02_FinanceAdd(self):
        """费用设置-财务设置-报销金额添加"""
        driver = self.driver
        ClasMenu.menu_full_text(self, "订货管理", "系统管理", "业务设置", "销售设置", "费用设置", "财务设置")
        # 移动到页面顶部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000763")
        driver.find_element_by_link_text("费用管理财务参数").click()

        # 检查费用报销是否勾选
        v_fybx = driver.find_element_by_id("ChkExpenseReimbursement")
        if v_fybx.is_selected():
            pass
        else:
            v_fybx.click()
        # 检查差旅费报销单是否勾选
        v_fybx = driver.find_element_by_id("ChkTravelExpense")
        if v_fybx.is_selected():
            pass
        else:
            v_fybx.click()
        # 检查费用申请单是否勾选
        v_fybx = driver.find_element_by_id("ChkCostApply")
        if v_fybx.is_selected():
            pass
        else:
            v_fybx.click()
        # 检查付款单是否勾选
        v_fybx = driver.find_element_by_id("ChkPayment")
        if v_fybx.is_selected():
            pass
        else:
            v_fybx.click()
        # 检查还款单是否勾选
        v_fybx = driver.find_element_by_id("ChkRepayment")
        if v_fybx.is_selected():
            pass
        else:
            v_fybx.click()
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功！" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_DB01_02_FinanceAdd")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
