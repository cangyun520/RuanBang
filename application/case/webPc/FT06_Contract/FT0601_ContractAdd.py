
from public.webClass import *


class ContractAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", "合同")
        timesl(10)

    """合同-新增合同"""
    def test_0601_Add(self):
        """合同-新增合同"""
        driver = self.driver
        v_spans = driver.find_elements_by_tag_name("span")
        for i in v_spans:
            if i.text == "新增":
                i.click()
                break
        timesl(2)

        v_inputs = driver.find_elements_by_tag_name("input")
        for i in v_inputs:
            print(i.get_attribute("placeholder"))
            if i.get_attribute("placeholder") == "请选择合同类别":
                i.click()






    """
    请选择合同类别
    请选择合同小类
    请选择主合同
    请选择签约单位
    选择[签约单位]后显示
    选择[签约单位]后显示
    请选择签约人
    请选择签约部门
    请选择签约日期
    请选择签约公司
    请选择实施人员
    请输入签约金额
    金额大写
    
    请选择产品
    请输入分摊金额
    请输入备注
    请选择款项类型
    请选择付款时间
    请输入付款金额
    请选择负责人
    请输入付款说明
    请输入
    请输入
    请输入
    请选择
    请输入
    请输入
    """


        #         driver.get_screenshot_as_file(propath() + "picture/oa/test_0103_01_check.jpg")
        #         unittest.expectedFailure("test_0103_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()