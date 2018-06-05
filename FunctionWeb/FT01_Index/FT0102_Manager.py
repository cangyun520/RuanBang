
from PubliCode.webClass import *


class Manager(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        ClasLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        ClasMenu.menu_part_text(self, "首页", "管理驾驶舱")
        # 移动到页面底部，防止对象遮挡
        ClasForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001048")

    """首页-管理驾驶舱页面检查"""
    def test_0102_01_check(self):
        """首页-管理驾驶舱页面检查"""
        driver = self.driver
        v_check = driver.find_elements_by_class_name("widget-thumb-heading")
        for i in v_check:
            # print(i.text)
            if "新增客户数" in i.text:
                print(i.text)
                break
            else:
                driver.get_screenshot_as_file(propath() + "TestPicture/oa/test_0102_01_check.jpg")
                unittest.expectedFailure("test_0102_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()