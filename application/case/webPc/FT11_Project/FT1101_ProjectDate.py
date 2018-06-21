from selenium.webdriver.common.action_chains import ActionChains
from public.webClass import *


class ProjectDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome
        driver = self.driver
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "项目管理", "项目主数据")
        WebForm.top(self, 0)
        driver.switch_to.frame("frame_tab_PM000753")

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

if __name__ == "__main__":
    unittest.main()
