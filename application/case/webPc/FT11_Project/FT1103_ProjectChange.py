from public.webClass import *
from selenium.webdriver.chrome.options import Options


class ProjectChange(unittest.TestCase):
    def setUp(self):
        mobile_emulation = {"deviceName": "iPhone 6"}
        option = Options()

        option.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options = option)


        self.driver = webdriver.Chrome()
        WebLogin.submit(self)
        driver = self.driver
        # 打开菜单
        WebMenu.full_text(self, "项目管理", "项目变更")
        # 移动到页面顶部，防止对象遮挡
        WebForm.top(self, 0)
        time.sleep(2)
        driver.switch_to.frame("frame_tab_PM000756")

    # -项目管理-项目信息变更
    def test_1103_01_Add(self):
        """项目管理-项目信息变更-新增变更功能检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='trProjectCode_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winProjectNo_IFrame")
        # 查询筛选数据
        driver.find_element_by_id("txtSearchText").send_keys("PRJ")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        v_list[random.randint(0, len(v_list) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 项目类型
        driver.find_element_by_id("cbProjectType").click()
        time.sleep(1)
        v_project_type = driver.find_elements_by_class_name("x-combo-list-item")
        if len(v_project_type) > 1:
            driver.find_elements_by_class_name("x-combo-list-item")[1].click()
        # 项目经理
        driver.find_element_by_xpath("//*[@id='tfProjectManager_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winReciver_IFrame")
        v_list_user = driver.find_elements_by_class_name("x-grid3-row")
        v_list_user[random.randint(0, len(v_list_user) - 1)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 立项时间
        WebForm.today(self, "dateBuildsData")
        # 计划开始日期
        WebForm.today(self, "dateBuildsStart")
        # 预计关闭日期
        WebForm.today(self, "dateBuildsEnd")
        # 合同编号
        driver.find_element_by_xpath("//*[@id='trContractNo_Container']/div/span").click()
        time.sleep(2)
        driver.switch_to.frame("winContact_IFrame")
        v_list_contract = driver.find_elements_by_class_name("x-grid3-row")
        v_list_contract[random.randint(0, len(v_list_contract) - 1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 保存单据
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        for i in driver.find_elements_by_tag_name("span"):
            if i.text == "添加成功":
                print(i.text)
                break

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(ProjectChange("test_1103_01_Add"))
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)