# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from common.webClass import *


class ContractBudget(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self, "manage", "刘朗洲", "YUANDINGYUN", "368739960423059456")
        # 打开菜单
        WebMenu.f_menu(self, "预算管理")
        WebMenu.menu(self, '//*[@id="/manage/BudgetManager$Menu"]/li[1]')

    """合同预算-行数据添加"""
    def test_0201_01_add(self):
        """主数据-行数据添加"""
        dr = self.driver
        cy_check = dr.find_element_by_class_name("ant-breadcrumb-link")

        if "合同预算" in cy_check.text:
            print(cy_check)
        else:
            dr.get_screenshot_as_file(SCREENSHOT_PATH + "Budget/test_0201_01_add.png")
            unittest.expectedFailure("test_0201_01_add")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
