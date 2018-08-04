# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *
from public.config import *


class HomeManag(unittest.TestCase):
    def setUp(self):
        # 指定浏览器
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self, "homePage", "0KPTYTUA7R0UQBR3P4IF")
        # 打开菜单
        WebMenu.full_text(self, "钉钉定制", "首页管理")

    """首页管理-行数据删除"""
    def test_0101_01_deleteGroup(self):
        """应收款情况-行数据删除"""
        dr = self.driver
        n = 0
        num = 3     # 后续通过数据库查询获取值
        try:
            while n < num:
                bs = dr.find_elements_by_css_selector(".rb-row-buttons>span.rb-row-button")
                for b in bs:
                    if b.text == "删除" and b.get_attribute("data-itemid") == "deleteGroup":
                        b.click()
                        # 删除确认
                        qs = dr.find_elements_by_css_selector(".rb-button.active")
                        for a in qs:
                            if a.get_attribute("data-id") == "ok":
                                a.click()
                                timesl(2)
                                break
                        break
                n += 1
        except Exception as e:
            dr.get_screenshot_as_file(REPORT_PATH + "homePage/test_0101_01_deleteGroup.png")
            unittest.expectedFailure("test_0101_01_deleteGroup")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
