from utils.webClass import *


class ProjectApproval(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.login_setup(self)
        driver = self.driver
        WebMenu.menu_full_text(self, "项目管理", "项目立项")
        # 移动到页面顶部，防止对象遮挡
        WebForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000755")

    '''项目管理-项目立项-添加单据'''
    def test_1102_01_add(self):
        """项目管理-项目立项-添加单据功能"""
        driver = self.driver
        v_tim = time.strftime("%y%m%d%H%M")
        # 项目编号
        driver.find_element_by_id("txtProjectCode").send_keys("PRJNO_" + v_tim)
        # 项目名称
        v_project = random.choice(
            ['南方电网公司', '国家电网公司', '郑州铁路局', '湖北交通局', '广西税务局', '上海进出口局', '南昌盐业公司', '新疆烟草公司', '云南公安厅', '武汉移动通信', '南京移动通信', '青海旅游局']
        )
        driver.find_element_by_id("txtProjectName").send_keys(v_project + "21世纪信息化总建设--" + v_tim)
        # 项目类型
        driver.find_element_by_id("cbProjectType").click()
        v_type = driver.find_elements_by_class_name("x-combo-list-item")
        v_type[random.randint(0, len(v_type)-1)].click()
        # 项目经理
        driver.find_element_by_xpath("//*[@id='tfProjectManager_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winReciver_IFrame")
        v_user = driver.find_elements_by_class_name("x-grid3-row")
        v_user[random.randint(0, len(v_user)-1)].click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 项目组
        driver.find_element_by_id("cbProjectTeam").click()
        v_group = driver.find_elements_by_class_name("x-combo-list-item")
        v_group[random.randint(len(v_type), len(v_group)-1)].click()
        # 预计关闭时间
        WebForm.form_today_next(self, 1, "dateBuildsEnd", 10, 15)
        # 提前执行合同
        driver.find_element_by_id("cbIshasContract").click()
        # 甲方项目组
        driver.find_element_by_link_text("甲方项目组").click()
        time.sleep(2)
        # 行数据-姓名
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_name())
        # 行数据-电话
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_mobile())
        # 行数据-手机
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[4]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_mobile())
        # 行数据-传真
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[5]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_mobile())
        # 行数据-邮箱
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[6]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_email())
        # 行数据-职位
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[7]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_position())
        # 行数据-地址
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(data_address())
        # 行数据-邮编
        driver.find_element_by_xpath(
            "//*[@id='gpOPR4']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[9]"
        ).click()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(111111, 888888))
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "添加成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(propath() + "picture/erp/test_1102_01_add.jpg")
                print(i.text)
                unittest.expectedFailure("test_1102_01_add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    # 执行测试集合
    runner = unittest.TextTestRunner()
    runner.run(testsuit)