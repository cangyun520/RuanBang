from PubliCode.webClass import *


class ServiceCall(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_full_text(self, "客户关系", "售后管理", "服务呼叫")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000277")
        # 排除自定义字段遮挡干扰
        ClasForm.form_field_hide(self)

    '''客户关系-售后管理-服务呼叫'''
    def test_1205_01_Add(self):
        """客户关系-售后管理-服务呼叫-新增单据功能"""
        driver = self.driver
        # 选择业务伙伴-客户
        driver.find_element_by_xpath("//*[@id='customer_Container']/div/span").click()
        time.sleep(4)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(2)
        # 联系人
        driver.find_element_by_id("contctCode").click()
        time.sleep(1)
        v_userlist = driver.find_elements_by_class_name("x-combo-list-item")
        if len(v_userlist) != 0:
            v_userlist[0].click()
        else:
            pass
        # 优先级
        driver.find_element_by_id("priority").click()
        time.sleep(1)
        v_priority = driver.find_elements_by_class_name("x-combo-list-item")
        if len(v_priority) != 0:
            for i in v_priority:
                if i.text == "中":
                    i.click()
                    break
        # 来源
        driver.find_element_by_id("origin").click()
        time.sleep(1)
        v_source = driver.find_elements_by_class_name("x-combo-list-item")
        if len(v_source) != 0:
            for i in v_source:
                if i.text == "电话号码":
                    i.click()
                    break
        # 处理人
        driver.find_element_by_id("rdoAssignee").click()
        time.sleep(1)
        driver.find_element_by_id("assigneeName").click()
        time.sleep(1)
        v_person = driver.find_elements_by_class_name("x-combo-list-item")
        if len(v_person) != 0:
            for i in v_person:
                if i.text == "销售代表：李慧":
                    i.click()
                    break
        # 主题
        driver.find_element_by_id("subject").send_keys(data_character(100, 200))
        driver.find_element_by_id("btnSave").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(propath() + "TestPicture/erp/test_1205_01_Add.jpg")
                unittest.expectedFailure("test_1205_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ServiceCall("test_1205_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)