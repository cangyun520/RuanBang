# encoding:utf-8
from public.webClass import *


class ContractAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", "签约明细")

    """合同-新增合同"""
    def test_0601_01_Add(self):
        """合同-新增合同"""
        dr = self.driver
        v_spans = dr.find_elements_by_tag_name("span")
        for i in v_spans:
            if i.text == "新增":
                i.click()
                break
        timesl(2)
        wid = SAASPc.wid(self, "baseForm")
        # 合同类别
        wid_htlb = wid + "contractClassId"
        dr.find_element_by_id(wid_htlb).click()
        v_htlb = SAASPc.popup(self, wid_htlb)

        v_htlb = "#v_htlb"
        print(v_htlb)
        lis = dr.find_elements_by_css_selector(v_htlb+">ul>li")
        for i in lis:
            print(i.text)
        # 合同小类
        dr.find_element_by_id(wid + "contractSubClassId").click()

        # 签约单位
        dr.find_element_by_id(wid + "customId").click()

        # 签约部分
        dr.find_element_by_id(wid + "deptId").click()

        # 签约公司
        dr.find_element_by_id(wid + "signingCompanyId").click()

        # 实施人员
        dr.find_element_by_id(wid + "implementerId").click()

        # 签约金额
        dr.find_element_by_id(wid + "money").click()

        #         driver.get_screenshot_as_file(propath() + "picture/oa/test_0103_01_check.jpg")
        #         unittest.expectedFailure("test_0103_01_check")

    """合同-新增合同"""
    def test_0601_02_check(self):
        """合同-新增合同"""
        dr = self.driver
        v_spans = dr.find_elements_by_tag_name("span")
        for i in v_spans:
            if i.text == "新增":
                i.click()
                break
        timesl(2)
        wid = SAASPc.wid(self, "baseForm")
        user = dr.find_element_by_xpath("//*[@id='_mainNav_userOperate']/span[2]").text
        print(user)
        cuser = dr.find_element_by_xpath("//*[@id='" + wid + "userId']/span[1]/input").text

        print(cuser)

        # driver.get_screenshot_as_file(propath() + "picture/oa/test_0103_01_check.jpg")
        # unittest.expectedFailure("test_0103_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()