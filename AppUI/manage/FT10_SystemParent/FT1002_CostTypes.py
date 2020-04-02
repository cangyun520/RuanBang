# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from common.webClass import *


class CostTypes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self, "manage", "刘朗洲", "YUANDINGYUN", "368739960423059456")
        # 打开菜单
        WebMenu.f_menu(self, "系统设置")
        WebMenu.menu(self, '//*[@id="/manage/SystemParent$Menu"]/li[2]')

    """费用类型-行数据添加"""
    def test_1002_01_add(self):
        """费用类型-行数据添加"""
        dr = self.driver
        cy_check = dr.find_element_by_class_name("ant-breadcrumb-link")

        if "费用类型" in cy_check.text:
            print(cy_check)
        else:
            dr.get_screenshot_as_file(SCREENSHOT_PATH + "System/test_1002_01_add.png")
            unittest.expectedFailure("test_1002_01_add")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
