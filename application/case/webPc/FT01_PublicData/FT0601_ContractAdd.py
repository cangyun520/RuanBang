# encoding:utf-8
from public.webClass import *


class ContractAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "基础数据", "客户库")

    """客户库-新增"""
    def test_0101_01_Add(self):
        """合同-新增合同"""
        dr = self.driver
        v_spans = dr.find_elements_by_tag_name("span")
        for i in v_spans:
            if i.text == "新增":
                i.click()
                break
        timesl(2)
        wid = SAASPc.wid(self)
        print(wid)
        dr.close()
        v_cloun = dr.find_elements_by_class_name("selected")
        v_cloun[1].click()
        timesl(1)

        v_sjdv = SAASPc.popup(self, "gridEdit", "parentId")
        # dr.find_element_by_id(v_sjdv).click()
        print(v_sjdv)

        v_sjdv_lis = dr.find_elements_by_css_selector(".rowData")
        v_sjdv_lis[random.randint(0, (len(v_sjdv_lis)-1))].click()

        a = dr.find_elements_by_class_name("rb-row-button")
        a[-1].click()
        timesl(10)




        # driver.get_screenshot_as_file(propath() + "picture/oa/test_0103_01_check.jpg")
        # unittest.expectedFailure("test_0103_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()