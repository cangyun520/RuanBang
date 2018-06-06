from utils.webClass import *


class Competitor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        WebMenu.menu_full_text(self, "客户关系", "售前管理", "竞争对手维护")
        # 移动到页面底部，防止对象遮挡
        WebForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001073")

    '''客户关系-销售管理-竞争对手维护数据添加'''
    def test_1201_01_Add(self):
        """客户关系-竞争对手维护--新增单据功能"""
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()
        time.sleep(1)
        # 竞争对手名称-公司
        v_company = data_company()
        driver.find_element_by_id("txtCompetiName").send_keys(v_company)
        # 省份
        driver.find_element_by_id("txtProvince").send_keys(data_province())
        # 地址
        driver.find_element_by_id("txtAddress").send_keys(data_address())
        # 网址
        driver.find_element_by_id("txtWebsite").send_keys(data_www())
        # 人数
        driver.find_element_by_id("txtCompanyNum").send_keys(random.randint(1, 9000))
        driver.find_element_by_id("btnDataSubmit").click()
        time.sleep(1)
        print(v_company)

    '''客户关系-销售管理-批量删除按钮校验'''
    def test_1201_02_Batchdelete(self):
        """客户关系-销售管理-批量删除按钮校验"""
        driver = self.driver
        driver.find_element_by_id("btnBatchDel").click()
        time.sleep(1)
        v_tip = driver.find_elements_by_class_name("bootbox-body")
        for i in v_tip:
            if "请选择" in i.text:
                print(i.text)
            else:
                print(i.text)
                unittest.expectedFailure("test_1201_02_Batchdelete")

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