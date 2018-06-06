
from utils.webClass import *


class HRreport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        WebLogin.login_setup(self)
        driver = self.driver
        # 打开菜单
        WebMenu.menu_part_text(self, "首页", "HR首页")
        # 移动到页面底部，防止对象遮挡
        WebForm.form_top(self, 0)
        driver.switch_to.frame("frame_tab_PM001007")

    """首页-HR首页检查"""
    def test_0103_01_check(self):
        """首页-HR首页检查"""
        driver = self.driver
        v_check = driver.find_elements_by_tag_name("a")
        for i in v_check:
            # print(i.text)
            if "按年龄" in i.text:
                break
            else:
                driver.get_screenshot_as_file(propath() + "picture/oa/test_0103_01_check.jpg")
                unittest.expectedFailure("test_0103_01_check")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()