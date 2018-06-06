
from selenium.webdriver.common.action_chains import ActionChains

from utils.webClass import *


class ProjectDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        WebMenu.menu_full_text(self, "项目管理", "项目主数据")
        WebForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM000753")

    '''项目管理-项目主数据-同步项目主数据功能'''

    def test_1101_01_Update(self):
        """项目管理-项目主数据-同步项目主数据功能"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        if len(v_list) <= 0:
            print("列表数据为空，不用检查")
        else:
            ActionChains(driver).double_click(v_list[0]).perform()
            time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000754")
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "已经保持相同记录" in i.text:
                print(i.text)
            elif "同步项目信息成功" in i.text:
                print(i.text)
            else:
                driver.get_screenshot_as_file(propath() + "picture/erp/test_1101_01_Update.jpg")
                print(i.text)
                unittest.expectedFailure("test_1101_01_Update")

    """项目管理-项目主数据-数据查看"""
    def test_1101_02_look(self):
        """项目管理-项目主数据-数据查看"""
        driver = self.driver
        v_list = driver.find_elements_by_class_name("x-grid3-row")
        ActionChains(driver).double_click(v_list[random.randint(0, len(v_list)-1)]).perform()
        time.sleep(4)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000754")
        v_button = driver.find_elements_by_tag_name("button")
        for i in v_button:
            print(i.text)
            if "打印" in i.text:
                print(i.text)
                break
            else:
                unittest.expectedFailure("test_1101_02_look")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
