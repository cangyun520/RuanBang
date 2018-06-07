from public.webClass import *


class Solution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.submit(self)
        driver = self.driver
        # 打开菜单
        WebMenu.full_text(self, "客户关系", "售后管理", "解决方案")
        # 移动到页面底部，防止对象遮挡
        WebForm.top(self, 0)
        driver.switch_to.frame("frame_tab_PM000279")

    '''客户关系-销售管理-解决方案'''
    def test_1203_01_Add(self):
        """客户关系-售后管理-解决方案-新增单据功能"""
        driver = self.driver
        # 选择物料
        driver.find_element_by_xpath("//*[@id='ItemCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_elements_by_class_name("x-grid3-row")[1].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        # 状体
        driver.find_element_by_id("c_Status").click()
        v_status = driver.find_elements_by_class_name("x-combo-list-item")
        v_status[random.randint(0, len(v_status) - 1)].click()
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")
        # 解决方案
        driver.find_element_by_id("Subject").send_keys(v_tim + data_character(50, 100))
        # 主题
        driver.find_element_by_id("Symptom").send_keys(data_character(100, 150))
        # 原因
        driver.find_element_by_id("Cause").send_keys(data_character(150, 200))
        # 备注
        driver.find_element_by_id("Descriptio").send_keys(data_character(200, 400))
        time.sleep(1)
        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(propath() + "picture/erp/test_1203_01_Add.jpg")
                unittest.expectedFailure("test_1203_01_Add")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Solution("test_1203_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)